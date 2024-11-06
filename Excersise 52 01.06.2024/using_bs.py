from bs4 import BeautifulSoup


with open('./html_intro.html') as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc, 'html.parser')

urls = []

# get element by id
div_menu = soup.find(id="menu")
ul = div_menu.find('ul')

links = ul.find_all('a')
for link in links:
    urls.append( link['href'])

print( urls )