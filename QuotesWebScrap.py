import pandas as pd
import requests
from bs4 import BeautifulSoup

authors = []
quotes = []
for j in range(1, 11):
    url = "https://quotes.toscrape.com/page/{}/".format(j)
    r = requests.get(url)
    #print(r)
    soup = BeautifulSoup(r.text, "lxml")
    #print(soup)
    rows = soup.find_all("div", class_="quote")
    #print(rows)
    for i in rows:
        quote = i.find("span", class_="text").text
        quotes.append(quote)
        author = i.find("small", class_="author").text
        authors.append(author)
c = {"Quotes": quotes, "Authors": authors}
df = pd.DataFrame(c)
print(df)
#df.to_csv("output.csv")