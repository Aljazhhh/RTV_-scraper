import requests
from bs4 import BeautifulSoup

url = "https://www.rtvslo.si/"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

hrefs = bs.find_all("a")

for x in hrefs:
    print(x.get("href"))

