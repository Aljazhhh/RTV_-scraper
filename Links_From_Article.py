import requests
from bs4 import BeautifulSoup
import json

article_url = "https://api.rtvslo.si/comments/720856/list?client_id=8c5205a95060a482f0fc96b9162d9e3f&sort=rating&order=desc&pageNumber=0&pageSize=20&_=1531117677180"

request = requests.get(article_url)

data = json.loads(request.text)

print(data["response"]["comments"])