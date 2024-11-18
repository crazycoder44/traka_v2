import requests

endpoint = "http://localhost:8000/api/salestrakav2/returns/7/delete/"


get_response = requests.delete(endpoint)

print(get_response)