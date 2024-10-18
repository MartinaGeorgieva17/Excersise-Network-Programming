import requests

# response = requests.Request('Get', 'https://httpbin.org/')
response = requests.get('https://httpbin.org/')
print(response.status_code)
print(response.headers)
print(response.text)