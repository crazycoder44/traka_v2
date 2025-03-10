from django.db import models, transaction
from django.contrib.auth.hashers import make_password
from django.utils.functional import cached_property
import uuid



class Products(models.Model):
    productname = models.CharField(max_length=150)
    desc = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2)

    STATUS_CHOICES = [
        (0, 'Unavailable'),
        (1, 'Available')
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)


    @staticmethod
    def add_product(validated_data):
        # Check if a product with the same name already exists
        product_name = validated_data.get('productname')
        if Products.objects.filter(productname=product_name).exists():
            return {"message": "A product already exists with this name."}
        
        if 'status' not in validated_data:
            validated_data['status'] = 0

        product_instance = Products(**validated_data)
        product_instance.save()
        return product_instance
    
    @staticmethod
    def update_product(validated_data):
        # Check if productname is in the validated data
        if 'productname' in validated_data:
            return {"message": "Product name update is not allowed."}

        # Retrieve product instance by id (ensure 'id' is in validated_data)
        product_id = validated_data.get("id")
        if not product_id:
            return {"message": "Product ID is required for update."}

        # Check if at least 'price' or 'desc' or 'status' is provided
        if 'price' not in validated_data and 'desc' not in validated_data and 'status' not in validated_data:
            return {"message": "Price, desc, or status values are required to perform update."}

        # Get the existing product instance
        try:
            product_instance = Products.objects.get(id=product_id)
        except Products.DoesNotExist:
            return {"message": "Product does not exist."}

        # Update only the fields present in validated_data
        if 'price' in validated_data:
            product_instance.price = validated_data['price']
        if 'desc' in validated_data:
            product_instance.desc = validated_data['desc']
        if 'status' in validated_data:
            product_instance.status = validated_data['status']

        product_instance.save()  
        return product_instance
    
    @staticmethod
    def delete_product(product_id):
        # Check for sales records with this productid
        if Sales.objects.filter(productid=product_id).exists():
            return {"message": "Products with sales or inventory records cannot be deleted."}

        # Check for inventory records with this productid
        if Inventory.objects.filter(productid=product_id).exists():
            return {"message": "Products with sales or inventory records cannot be deleted."}

        # Get the product instance and delete it
        try:
            product_instance = Products.objects.get(id=product_id)
            product_instance.delete()
            return {"message": "Product deleted successfully."}
        except Products.DoesNotExist:
            return {"message": "Product does not exist."}


class Branches(models.Model):
    branchname = models.CharField(max_length=50)
    address = models.TextField()
    mobile = models.CharField(max_length=15, null=True)
    date = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES = [
        (0, 'Unavailable'),
        (1, 'Available')
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.branchname
    
    @staticmethod
    def add_branch(validated_data):
        branchname = validated_data.get('branchname')
        address = validated_data.get('address')
        mobile = validated_data.get('mobile')

        # Check if a branch with the same name already exists
        if Branches.objects.filter(branchname=branchname).exists():
            return {"message": "A branch with this name already exists."}

        # Check if a branch with the same address already exists
        if Branches.objects.filter(address=address).exists():
            return {"message": "A branch already exists at this address."}

        # No conflicts found, create a new branch
        branch_instance = Branches(branchname=branchname, address=address, mobile=mobile)
        branch_instance.save()  # Save to the database
        return branch_instance
    
    @staticmethod
    def update_branch(branch_id, validated_data):
        if 'branchname' in validated_data:
            return {"message": "Branch names cannot be updated. Kindly delete the branch and recreate, or make it unavailable."}

        # Log the branch ID for debugging
        print("Branch ID from URL:", branch_id)

        # Retrieve branch details from the validated data
        address = validated_data.get('address')
        mobile = validated_data.get('mobile')


        # Retrieve the existing branch instance by ID
        try:
            branch_instance = Branches.objects.get(id=branch_id)
        except Branches.DoesNotExist:
            return {"message": "Branch does not exist."}

        # Check for duplicate address, excluding the current branch
        if address and Branches.objects.filter(address=address).exclude(id=branch_id).exists():
            return {"message": "A branch already exists at this address."}

        # Check for duplicate mobile number, excluding the current branch
        if mobile and Branches.objects.filter(mobile=mobile).exclude(id=branch_id).exists():
            return {"message": "A branch already exists with this mobile number."}

        # Update the branch instance with the new data
        if address is not None:
            branch_instance.address = address
        if mobile is not None:
            branch_instance.mobile = mobile

        # Save the updated instance to the database
        branch_instance.save()
        return branch_instance
    
    @staticmethod
    def delete_branch(branch_id):
        # Check for sales records with this branchid
        if Sales.objects.filter(branchid=branch_id).exists():
            return {"message": "Branches with sales or inventory records cannot be deleted."}

        # Check for inventory records with this branchid
        if Inventory.objects.filter(branchid=branch_id).exists():
            return {"message": "Branches with sales or inventory records cannot be deleted."}

        # Get the branch instance and delete it
        try:
            branch_instance = Branches.objects.get(id=branch_id)
            branch_instance.delete()
            return {"message": "Branch deleted successfully."}
        except Branches.DoesNotExist:
            return {"message": "Branch does not exist."}



class Users(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    ROLE_CHOICES = [
        ('Superadmin', 'Superadmin'),
        ('Admin', 'Admin'),
        ('Sales Rep', 'Sales Rep'),
    ]

    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    address = models.TextField()
    role = models.CharField(max_length=11, choices=ROLE_CHOICES)
    datejoined = models.DateTimeField(auto_now_add=True)
    branchid = models.ForeignKey(Branches, on_delete=models.PROTECT, null=True, blank=True)
    password = models.CharField(max_length=128, default=make_password("1234567"))

    STATUS_CHOICES = [
        (0, 'Unavailable'),
        (1, 'Available')
    ]
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

    @classmethod
    def add_user(cls, validated_data):
        # Check if a user with the given email already exists
        if cls.objects.filter(email=validated_data.get('email')).exists():
            return {"message": "A user already exists with this email."}

        # Hash the password and create a new user
        password = validated_data.get('password', "1234567")  # Default if password not in validated_data
        hashed_password = make_password(password)
        
        # Save the new user instance with hashed password
        new_user = cls(
            firstname=validated_data.get('firstname'),
            lastname=validated_data.get('lastname'),
            gender=validated_data.get('gender'),
            email=validated_data.get('email'),
            mobile=validated_data.get('mobile'),
            address=validated_data.get('address'),
            role=validated_data.get('role'),
            branchid=validated_data.get('branchid'),
            password=hashed_password
        )
        new_user.save()
        return new_user
    
    @classmethod
    def update_user(cls, user_id, validated_data):
        # Retrieve the user instance by ID
        try:
            user_instance = cls.objects.get(id=user_id)
        except cls.DoesNotExist:
            return {"message": "User does not exist."}

        # Check if a different user already has the same email
        email = validated_data.get("email")
        if email and cls.objects.filter(email=email).exclude(id=user_id).exists():
            return {"message": "A user with this email already exists."}

        # Update fields if provided in validated_data
        if 'firstname' in validated_data:
            user_instance.firstname = validated_data['firstname']
        if 'lastname' in validated_data:
            user_instance.lastname = validated_data['lastname']
        if 'gender' in validated_data:
            user_instance.gender = validated_data['gender']
        if 'email' in validated_data:
            user_instance.email = validated_data['email']
        if 'mobile' in validated_data:
            user_instance.mobile = validated_data['mobile']
        if 'address' in validated_data:
            user_instance.address = validated_data['address']
        if 'role' in validated_data:
            user_instance.role = validated_data['role']
        if 'branchid' in validated_data:
            user_instance.branchid = validated_data['branchid']
        if 'status' in validated_data:
            user_instance.status = validated_data['status']
        if 'password' in validated_data:
            password = validated_data['password']
            hashed_password = make_password(password)
            user_instance.password = hashed_password

        # Save the updated instance to the database
        user_instance.save()
        return {"message": "User updated successfully.", "user": user_instance}
    
    @staticmethod
    def delete_user(user_id):
        # Check for sales records with this branchid
        if Sales.objects.filter(userid=user_id).exists():
            return {"message": "Users with sales or inventory records cannot be deleted."}

        # Check for inventory records with this branchid
        if Inventory.objects.filter(userid=user_id).exists():
            return {"message": "Users with sales or inventory records cannot be deleted."}

        # Get the branch instance and delete it
        try:
            user_instance = Users.objects.get(id=user_id)
            user_instance.delete()
            return {"message": "User deleted successfully."}
        except Users.DoesNotExist:
            return {"message": "User does not exist."}



class Sales(models.Model):
    ORDER_SRC_CHOICES = [
        ('Facebook', 'Facebook'),
        ('Instagram', 'Instagram'),
        ('Twitter', 'Twitter'),
        ('Website', 'Website'),
        ('On premises', 'On premises'),
    ]

    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('Card', 'Card'),
        ('Transfer', 'Transfer'),
    ]


    orderid = models.CharField(max_length=20)
    ordersrc = models.CharField(max_length=15, choices=ORDER_SRC_CHOICES)
    productid = models.ForeignKey(Products, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    userid = models.ForeignKey(Users, on_delete=models.PROTECT)
    branchid = models.ForeignKey(Branches, on_delete=models.PROTECT)
    payment_choice = models.CharField(max_length=15, choices=PAYMENT_CHOICES)
    date = models.DateTimeField(auto_now_add=True)
    
    
    @cached_property
    def total_sale_price(self):
        return self.unit_price * self.quantity
    

    @cached_property
    def order_total_amount(self):
        # Sum up the total_price for all sales instances with the same orderid
        related_sales = Sales.objects.filter(orderid=self.orderid)
        total_sales_price = sum(sale.total_sale_price for sale in related_sales)

        # Subtract the return_amount from the total sales price
        return total_sales_price - self.return_amount

    

    @cached_property
    def return_amount(self):
        # Filter for return instances with the same orderid
        return_instances = Returns.objects.filter(orderid=self.orderid)

        # If there are no matching returns, return 0
        if not return_instances.exists():
            return 0

        # Filter for refund instances where action='Refund'
        refund_instances = return_instances.filter(action='Refund')
        if not refund_instances.exists():
            return 0

        # Calculate the refund amount for each refund instance by finding the matching sales unit price
        refund_total = 0
        for refund_instance in refund_instances:
            # Find the corresponding sale instance for the refund
            sale_instance = Sales.objects.filter(
                orderid=refund_instance.orderid,
                productid=refund_instance.productid
            ).first()

            # If a matching sale instance is found, calculate the refund amount for this instance
            if sale_instance:
                refund_total += sale_instance.unit_price * refund_instance.quantity

        return refund_total



    @staticmethod
    def process_sales(sales_data):
        created_sales = []
        
        with transaction.atomic(): 
            for sale_data in sales_data: 
                # Extract individual sale fields from each sale dictionary 
                order_id = sale_data['orderid']
                print(order_id)
                productid = sale_data.get("productid") 
                branchid = sale_data.get("branchid") 
                quantity = sale_data.get("quantity") 
                unit_price = sale_data.get("unit_price") 
                ordersrc = sale_data.get("ordersrc") 
                payment_choice = sale_data.get("payment_choice") 
                userid = sale_data.get("userid") 
                
                # Check if enough inventory is available 
                inventory_items = Inventory.objects.filter(productid_id=productid, branchid_id=branchid) 
                if not inventory_items.exists() or quantity > inventory_items.count(): 
                    raise ValueError(f'Insufficient goods in inventory for product {productid} in branch {branchid}') 
                
                # Create a new sale instance 
                sale_instance = Sales( 
                    orderid=order_id, 
                    productid_id=productid, 
                    branchid_id=branchid, 
                    quantity=quantity, 
                    unit_price=unit_price, 
                    ordersrc=ordersrc, 
                    payment_choice=payment_choice, 
                    userid_id=userid 
                ) 
                
                # Delete the required quantity of inventory items 
                for i, item in enumerate(inventory_items, start=1): 
                    item.delete() 
                    if i >= quantity: 
                        break 
                
                # Save the sale instance and add to the created sales list 
                sale_instance.save() 
                created_sales.append(sale_instance) 
        
        return created_sales
    
    def delete_sale(self):
        """Restore inventory when a sale instance is deleted."""
        productid = self.productid
        branchid = self.branchid
        userid = self.userid
        quantity = self.quantity

        # Create inventory instances
        inventory_instances = [
            Inventory(productid=productid, branchid=branchid, userid=userid)
            for _ in range(quantity)
        ]
        print(inventory_instances)
        # Atomic operation to ensure consistency
        with transaction.atomic():
            # Bulk create inventory instances
            Inventory.objects.bulk_create(inventory_instances)

            # Delete the sale instance
            self.delete()

        return f"Sale deleted, and {quantity} items restored to inventory."

    def __str__(self):
        return (f"Order {self.orderid} - Product ID: {self.productid} - "
                f"Source: {self.ordersrc} - Quantity: {self.quantity} - "
                f"Total Price: {self.total_price}")



class Returns(models.Model):
    ACTION_CHOICES = [
        ('Replace', 'Replace'), 
        ('Refund', 'Refund'),
    ]

    orderid = models.CharField(max_length=20)
    productid = models.ForeignKey(Products, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    action = models.CharField(max_length=7, choices=ACTION_CHOICES)
    userid = models.ForeignKey(Users, on_delete=models.PROTECT)
    branchid = models.ForeignKey(Branches, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)

    def process_return(self):
        # Query all Sales instances matching the orderid
        sale_instances = Sales.objects.filter(orderid=self.orderid)

        # If no matching sales exist, return an error
        if not sale_instances.exists():
            return 'Sale order does not exist'

        # Filter sale instances for matching product ID
        sale_instance = sale_instances.filter(productid=self.productid).first()
        
        # If no matching product found in sales, return an error
        if not sale_instance:
            return 'Returned product does not match Order product'

        # Check if the return quantity exceeds the sale quantity
        if self.quantity > sale_instance.quantity:
            return 'Return quantity exceeds Sale quantity'

        # Process inventory if action is 'Replace'
        if self.action == 'Replace':
            inventory_items = Inventory.objects.filter(productid=self.productid)[:self.quantity]

            if inventory_items.count() < self.quantity:
                return 'Insufficient goods in inventory'

            # Delete inventory items one by one for the required quantity
            for item in inventory_items:
                item.delete()

            return 'Return processed successfully'
        # For other actions, add additional handling here
        return 'Return action processed'


    def __str__(self):
        return f"Return {self.orderid} - Action: {self.action}"



class Inventory(models.Model):
    productid = models.ForeignKey(Products, on_delete=models.PROTECT)
    serialnumber = models.CharField(max_length=50, null=True, blank=True)
    userid = models.ForeignKey(Users, on_delete=models.PROTECT)
    branchid = models.ForeignKey(Branches, on_delete=models.PROTECT)
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Inventory - Product ID: {self.productid} - Serial Number: {self.serialnumber}"
