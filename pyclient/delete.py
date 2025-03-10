import requests

endpoint = "http://localhost:8000/api/salestrakav2/sales/42/delete/"


get_response = requests.delete(endpoint)

print(get_response)