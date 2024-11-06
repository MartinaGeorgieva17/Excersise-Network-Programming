import requests
response = requests.get ("https://softwareacademy.bg/")
print (response.content)
print(response.headers)