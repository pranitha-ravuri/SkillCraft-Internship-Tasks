import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

products = []

for book in soup.find_all("article", class_="product_pod"):
    name = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    rating = book.p["class"][1]

    products.append({
        "Name": name,
        "Price": price,
        "Rating": rating
    })

df = pd.DataFrame(products)

df.to_csv("products.csv", index=False)

print("Product details saved to products.csv")