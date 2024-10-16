import requests

url = "https://books.toscrape.com/"
res = requests.get(url)
htmlData = res.content
print(htmlData)