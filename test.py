from bs4 import BeautifulSoup

html = """</a>, <a class="btn btn-primary" 
href="https://www.rtvslo.si/odjava">Odjava</a>, 
<a class="btn btn-primary" 
href="https://www.rtvslo.si/mojrtv">mojRTV</a>"""

href = BeautifulSoup(html, "html.parser")

data = href.find_all("a")

for dat in data: 
    print(dat.get("href"))