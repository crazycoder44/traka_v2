import requests

endpoint = "http://localhost:8000/api/salestrakav2/returns/"

data = {
    "orderid": "652fa563dce245",
    "productid": 2,
    "quantity": 1,
    "action": "Replace",
    "userid": 1,
    "branchid": 1
}

get_response = requests.post(endpoint, json=data)

print(get_response.json())

# data = [
#     {
#     "ordersrc": "Instagram",
#     "productid": 1,
#     "quantity": 1,
#     "unit_price": 127000.00,
#     "userid": 1,
#     "branchid": 1,
#     "payment_choice": "Cash",
# }
# ]

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
#     "branch": 1,
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