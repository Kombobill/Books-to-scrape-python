from bs4 import BeautifulSoup
import requests

# Step 1: Fetch the website content
url = "https://books.toscrape.com/catalogue/category/books/classics_6/index.html"
res = requests.get(url)
htmlData = res.content

# Step 2: Parse the HTML content with BeautifulSoup
parsedData = BeautifulSoup(htmlData, "html.parser")

# # Step 3: Find all <article> tags with the class 'product_pod'
# books = parsedData.find_all('article', class_='product_pod')

# # Step 4: Get the number of books
# num_of_books = len(books)
# print(f"Number of books: {num_of_books}")

s = parsedData.find('div', class_='col-sm-8 col-md-9')


print(s)