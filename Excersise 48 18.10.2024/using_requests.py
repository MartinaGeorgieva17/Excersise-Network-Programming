import requests

# response = requests.request("GET", 'https://httpbin.org/')
headers = {
    'user-agent': 'My Python Client',
}

params = {
    'x':1,
    'y':2
}

# response = requests.get('https://httpbin.org/?x=1&y=2', headers=headers)

response = requests.get('http://127.0.0.1:8000', headers=headers, params=params)

print(response.request.headers)
print('~'*30)
print(response.headers)
print(response.ok)
print(response.status_code)

# print(response.text)
# print('~'*30)
# print(response.content)