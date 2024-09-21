import pandas as pd
import requests
from bs4 import BeautifulSoup

titles = []
prices = []
for i in range(1, 51):
    url = "https://books.toscrape.com/catalogue/page-{}.html".format(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
    for j in box:
        title = j.find("h3").text
        titles.append(title)
        price = j.find("p", class_="price_color").text
        prices.append(price)
c = {"Title": titles, "Price": prices}
df = pd.DataFrame(c)
print(df)