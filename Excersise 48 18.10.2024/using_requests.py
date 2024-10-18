import requests

headers = {
    "user-agent": "My Python Client"

}
params = {
    "x": 1,
    "y":2
}
response = requests.get("GET", "http://httpbin.org/x=1&y=2", headers=headers)

response = requests.get("GET", "127.0.0.1:8080", headers=headers, params=params)

# print(response.headers)
# print(response.ok)
# print(response.status_code)
# print(response.request)
print("~"*30)
print(response.text)
# print("~"*30)
# print(response.content)
