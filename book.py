from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/"
res = requests.get(url)
htmlData = res.content
parsedData = BeautifulSoup(htmlData, "html.parser")
print(parsedData.prettify())
