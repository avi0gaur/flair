import requests
import re
from bs4 import BeautifulSoup
import io

urls = [
    ["https://en.wikipedia.org/wiki/List_of_content_management_systems", "Comparison of web frameworks"]
    ]

for url in urls:
    text = []

    table_name = url[0].split("/")[4]

    fileName = table_name + '.txt'

    f = io.open(f'./code_gazetteers/{fileName}', 'w', encoding='utf8')

    response = requests.get(url=url[0])
    soup = BeautifulSoup(response.content, 'html.parser')

    for tag in soup.find_all("td"):
        if tag.text == url[1]:
            break
        p1 = """title=\"[^<>]*\""""
        p2 = """[>].*[<][/]a"""
        p3 = """\(\..*\)"""
        p4 = """href=\"[^<>]*\""""
        for elem in re.findall(pattern=p2, string=str(tag.contents)):
            text.append(elem)
            print(elem)

    for item in text:
        f.write("%s\n" % item)

    f.close()
