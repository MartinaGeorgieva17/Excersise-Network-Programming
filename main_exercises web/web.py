import requests
from bs4 import BeautifulSoup

def simple_crawler(url):
    # Изпращаме GET заявка към сайта
    response = requests.get(url)

    # Проверяваме дали заявката е успешна (статус код 200)
    if response.status_code == 200:
        # Парсваме HTML съдържанието на страницата с BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Извличаме заглавието на страницата
        title = soup.title.string if soup.title else "No Title"

        # Извличаме всички линкове от страницата
        links = soup.find_all('a')

        # Записваме съдържанието в HTML файл
        with open('crawler_output.html', 'w', encoding='utf-8') as file:
            file.write('<html>\n<head>\n<title>Web Crawler Results</title>\n</head>\n<body>\n')
            file.write(f'<h1>Заглавие на страницата: {title}</h1>\n')
            file.write('<ul>\n')

            # Извеждаме всеки намерен линк в списък
            for link in links:
                href = link.get('href')
                if href:
                    file.write(f'<li><a href="{href}">{href}</a></li>\n')

            file.write('</ul>\n')
            file.write('</body>\n</html>')
        
        print("Данните са записани в crawler_output.html")
    else:
        print(f"Грешка при достъпа: {response.status_code}")

# Примерно извикване на функцията
simple_crawler("http://example.com")