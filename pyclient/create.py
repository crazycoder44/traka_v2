import requests

endpoint = "http://localhost:8000/api/salestrakav2/sales/"

data = {
        "ordersrc": "Instagram",
        "productid": 3,
        "quantity": 1,
        "unit_price": 127000.00,
        "userid": 1,
        "branchid": 3,
        "payment_choice": "Transfer"
    }
    


get_response = requests.post(endpoint, json=data)

print(get_response.json())

# data = {
#     "productid": 3,
#     "userid": 1,
#     "branchid": 3,
#     "quantity": 20
# }

# data = {
#     "firstname": "panda",
#     "lastname": "hyena",
#     "gender": "Male",
#     "email": "babaitu@gmail.com",
#     "mobile": "9126751245",
#     "address": "nepa",
#     "role": "Sales Rep",
#     "branch": 4,
# }

# data = {
#     "productname": "Air Fryer",
#     "price": 127000.00
# }

# data = {
#     "branchname": "oshodi",
#     "address": "gbera",
#     "mobile": 9023416389
# }

# data = {
#     "firstname": "lamba",
#     "lastname": "waybad",
#     "gender": "Male",
#     "email": "lamba@gmail.com",
#     "mobile": 9011002000,
#     "address": "gbafuo",
#     "role": "Sales Rep",
#     "branchid": 2
# }