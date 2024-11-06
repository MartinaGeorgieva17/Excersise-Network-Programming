from urllib.parse import urljoin

BASE_URL = "https://pepina.bg"
page_url = "/products/kolekciya-esen-zima-2024"
href = "/product/damski-chehli-s-vulna-1"

page_full_url = urljoin(BASE_URL, page_url)
product_full_url = urljoin(BASE_URL, href)

print(page_full_url)
print(product_full_url)