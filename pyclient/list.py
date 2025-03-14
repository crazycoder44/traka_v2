import requests

endpoint = "http://localhost:8000/api/salestrakav2/products/"


# Your authorization token (replace this with your actual token)
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQxODgzMjQyLCJpYXQiOjE3NDE4Nzg2MjEsImp0aSI6ImEyY2Q3MTc0OTFhOTQ0NDFhMGNlYTg0M2EyNDM3MzMyIiwidXNlcl9pZCI6MX0.m2e_U8DVPnE66HWfiS4YPvvY_lXtaCzFDfrtINf1Kho"

# Define headers to include the token
headers = {
    "Authorization": f"Bearer {auth_token}"
}

# Make the GET request with the authorization token
get_response = requests.get(endpoint, headers=headers)

print(get_response.json())