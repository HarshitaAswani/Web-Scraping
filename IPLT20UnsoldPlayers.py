import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "https://www.iplt20.com/auction"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
table = soup.find_all("table", class_="ih-td-tab auction-tbl")[12]
#print(table)

headers = table.find_all("th")
#print(headers)

titles = []
for i in headers:
    title = i.text
    titles.append(title)
#print(titles)

df = pd.DataFrame(columns=titles)
#print(df)

rows = table.find_all("tr")
for i in rows[1:]:
    data = i.find_all("td")
    row = [td.text for td in data]
    l = len(df)
    df.loc[l] = row
print(df)
#df.to_csv("output.csv")