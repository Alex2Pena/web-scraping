import requests
from bs4 import BeautifulSoup

found = 0
URL = 'https://en.wikipedia.org/wiki/History_of_Mexico'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')
parent_results = soup.find_all("p")

for result in parent_results:
    citation_result = result.find(title="Wikipedia:Citation needed")
    if citation_result:
        found += 1
        print(f"FOUND CITATION: \n{result.text}")
print(f"TOTAL FOUND: {found}")
