import requests

headers = {
    "user-agent": "My Python Client"
    
}

response = requests.request("GET", "http://httpbin.org/")

# print(response.headers)
# print(response.ok)
# print(response.status_code)
# print(response.request)
print("~"*30)
print(response.text)
# print("~"*30)
# print(response.content)
