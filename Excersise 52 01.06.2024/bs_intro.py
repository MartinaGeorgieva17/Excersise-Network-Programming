from bs4 import BeautifulSoup

html_doc = """
<body>
    <a href="/product/1">Product 1</a>
    <a href="/product/2" class="test"><span>Product</span> 2</a>
</body>
"""
soup = BeautifulSoup(html_doc, 'html.parser')

# links = soup.find_all('a')
# for link in links:
#     print(link.text)

# test_link = soup.find('a', class_="test")
# print(test_link)
# print( test_link.text )
# print( test_link['href'] )

# Task: get all a elements hrefs into list
urls = []
links = soup.find_all('a')
for link in links:
    urls.append( link['href'])

print( urls ) # ['/product/1', '/product/2']