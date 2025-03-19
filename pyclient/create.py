import requests

endpoint = "http://localhost:8000/api/salestrakav2/branches/"

data = {
    "branchname": "ikeja",
    "address": "gbera",
    "mobile": "9023416389"
}

# Your authorization token (replace this with your actual token)
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQyMzk1NjQ4LCJpYXQiOjE3NDIzOTM4NDgsImp0aSI6IjlmZTBlODE5Yjk2MzQxZGU4MzE1OTNhYjQ2ZjA3YTk1IiwidXNlcl9pZCI6M30.Vj_rrsZD5ux2X1kIEh9YNOmvLM45Jv1--u2mV-8LvWA"

# Define headers to include the token
headers = {
    "Authorization": f"Bearer {auth_token}"
}

get_response = requests.post(endpoint, json=data, headers=headers)

print(get_response.json())

# data = {
#     "email": "panda@gmail.com",
#     "password": "1234567"
# }

# data = {
#     "orderid": "652fa563dce245",
#     "productid": 2,
#     "quantity": 1,
#     "action": "Replace",
#     "userid": 1,
#     "branchid": 1
# }

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
#     "branchid": 1,
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