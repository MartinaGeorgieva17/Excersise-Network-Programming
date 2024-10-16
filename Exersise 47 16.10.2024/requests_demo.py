import requests

response=requests.get("http://bebemax.bg")
print(response.status_code)
print(response.headers)