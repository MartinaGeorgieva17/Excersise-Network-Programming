import requests

url = "https://pepina.bg/product/damski-bejovi-boti-velur-2"
filename = "pepina.html"

headers = {"User-Agent": "Mozilla/5.0"}

try:
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Content saved to {filename}")
except requests.exceptions.RequestException as e:
    print(f"Exception: {e}")

# if response.ok:
#     with open(filename, "w", encoding="utf-8") as f:
#         f.write(response.text)
#     print(f"Content saved to {filename}")
# else:
#     print("Failed to retrieve content:", response.status_code)
#     print(response.text)