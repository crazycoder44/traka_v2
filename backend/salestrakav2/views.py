from rest_framework import generics, status
from rest_framework.response import Response

from .models import Products
from .models import Branches
from .models import Users
from .models import Sales
from .models import Returns
from .models import Inventory

from .serializers import ProductsSerializer
from .serializers import BranchesSerializer
from .serializers import UsersSerializer
from .serializers import SalesSerializer
from .serializers import ReturnsSerializer
from .serializers import InventorySerializer







class ProductsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer

products_list_create_view = ProductsListCreateAPIView.as_view()


class ProductsDetailAPIView(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # lookup_field = 'pk'

products_detail_view = ProductsDetailAPIView.as_view()


class ProductsUpdateAPIView(generics.UpdateAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        # Get the product instance to update
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        
        # Validate the data with the serializer
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data
        validated_data['id'] = instance.pk
        
        # Call the update_product method with validated data
        update_response = Products.update_product(serializer.validated_data)
        
        # Check if update_product returned a message (indicating no update was performed)
        if isinstance(update_response, dict) and "message" in update_response:
            return Response(update_response, status=status.HTTP_400_BAD_REQUEST)

        # If update was successful, return the updated instance data
        serializer = self.get_serializer(update_response)
        return Response(serializer.data, status=status.HTTP_200_OK)

products_update_view = ProductsUpdateAPIView.as_view()



class ProductsDestroyAPIView(generics.DestroyAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # lookup_field = 'pk'

products_destroy_view = ProductsDestroyAPIView.as_view()


class BranchesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer

branches_listcreate_view = BranchesListCreateAPIView.as_view()


class BranchesDetailAPIView(generics.RetrieveAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    lookup_field = 'id'

branches_detail_view = BranchesDetailAPIView.as_view()


class BranchesUpdateAPIView(generics.UpdateAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    # lookup_field = 'id'

branches_update_view = BranchesUpdateAPIView.as_view()


class BranchesDestroyAPIView(generics.DestroyAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchesSerializer
    # lookup_field = 'pk'

branches_destroy_view = BranchesDestroyAPIView.as_view()



class UsersListCreateAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # lookup_field = 'id'

users_listcreate_view = UsersListCreateAPIView.as_view()



class UsersDetailAPIView(generics.RetrieveAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # lookup_field = 'id'

users_detail_view = UsersDetailAPIView.as_view()


class UsersUpdateAPIView(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # lookup_field = 'id'

users_update_view = UsersUpdateAPIView.as_view()


class UsersDestroyAPIView(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    # lookup_field = 'pk'

users_destroy_view = UsersDestroyAPIView.as_view()



class SalesListCreateAPIView(generics.ListCreateAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    # lookup_field = 'id'

    def create(self, request, *args, **kwargs): 
        serializer = self.get_serializer(data=request.data, many=True) 
        serializer.is_valid(raise_exception=True) 
        self.perform_create(serializer) 
        headers = self.get_success_headers(serializer.data) 
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

sales_listcreate_view = SalesListCreateAPIView.as_view()


class SalesDetailAPIView(generics.RetrieveAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    # lookup_field = 'id'

sales_detail_view = SalesDetailAPIView.as_view()


# class SalesUpdateAPIView(generics.UpdateAPIView):
#     queryset = Sales.objects.all()
#     serializer_class = SalesSerializer
#     # lookup_field = 'id'

# sales_update_view = SalesUpdateAPIView.as_view()


class SalesDestroyAPIView(generics.DestroyAPIView):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    # lookup_field = 'pk'

    def delete(self, request, pk, *args, **kwargs):
        try:
            sale_instance = Sales.objects.get(pk=pk)
            serializer = SalesSerializer()
            result = serializer.delete(sale_instance)
            return Response(result, status=status.HTTP_200_OK)
        except Sales.DoesNotExist:
            return Response({"error": "Sale not found"}, status=status.HTTP_404_NOT_FOUND)

sales_destroy_view = SalesDestroyAPIView.as_view()



class ReturnsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Returns.objects.all()
    serializer_class = ReturnsSerializer
    # lookup_field = 'id'

returns_listcreate_view = ReturnsListCreateAPIView.as_view()



class ReturnsDetailAPIView(generics.RetrieveAPIView):
    queryset = Returns.objects.all()
    serializer_class = ReturnsSerializer
    # lookup_field = 'id'

returns_detail_view = ReturnsDetailAPIView.as_view()


class ReturnsUpdateAPIView(generics.UpdateAPIView):
    queryset = Returns.objects.all()
    serializer_class = ReturnsSerializer
    # lookup_field = 'id'

returns_update_view = ReturnsUpdateAPIView.as_view()


class ReturnsDestroyAPIView(generics.DestroyAPIView):
    queryset = Returns.objects.all()
    serializer_class = ReturnsSerializer
    # lookup_field = 'pk'

returns_destroy_view = ReturnsDestroyAPIView.as_view()




class InventoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    # lookup_field = 'id'

inventory_listcreate_view = InventoryListCreateAPIView.as_view()


class InventoryDetailAPIView(generics.RetrieveAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    # lookup_field = 'id'

inventory_detail_view = InventoryDetailAPIView.as_view()


class InventoryDestroyAPIView(generics.DestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    # lookup_field = 'pk'

inventory_destroy_view = InventoryDestroyAPIView.as_view()