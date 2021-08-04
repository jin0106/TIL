import requests

url = 'https://api.agify.io/?name=jin'

response = requests.get(url).json()

print(type(response))
print(response['name'])