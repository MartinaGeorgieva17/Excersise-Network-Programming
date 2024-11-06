import requests

import requests

url = "https://www.youtube.com/results?search_query=html5"
filename = "youtube_html5.html"

# headers = {"User-Agent": "Mozilla/5.0"}

response = requests.get(url)

if response.ok:
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)
    print(f"Content saved to {filename}")
else:
    print("Failed to retrieve content:", response.status_code)
    print(response.text)