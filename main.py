import requests
from bs4 import BeautifulSoup

url = "https://www.rtvslo.si/"
response = requests.get(url)
bs = BeautifulSoup(response.text, "html.parser")

print(bs.h1) 
