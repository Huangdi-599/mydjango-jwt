import requests

endpoint = "http://127.0.0.1:8000/app/student"
response =  requests.get(endpoint)
print(response)
print(response.json())