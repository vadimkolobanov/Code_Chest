import requests
import json

response = requests.get('https://apicodechest.herokuapp.com/api/projects/')
print(response.status_code)
print(response.json())
