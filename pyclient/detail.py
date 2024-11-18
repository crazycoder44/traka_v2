import requests

endpoint = "http://localhost:8000/api/salestrakav2/returns/2/"

get_response = requests.get(endpoint)

print(get_response.json())