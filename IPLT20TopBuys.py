import pandas as pd
import requests
from bs4 import BeautifulSoup
url = "https://www.iplt20.com/auction/2024"
r = requests.get(url)
soup = BeautifulSoup(r.text, "lxml")
table = soup.find_all("table", class_="ih-td-tab auction-tbl")[11]
#print(table)

headers = table.find_all("th")
#print(headers)

titles = []
for i in headers:
    title = i.text
    titles.append(title)
#print(titles)

df = pd.DataFrame(columns = titles)
#print(df)

rows = table.find_all("tr")
for i in rows[1:]:
    first_td = i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data = i.find_all("td")[1:]
    row = [td.text for td in data]
    row.insert(0, first_td)
    l = len(df)
    df.loc[l]=row
print(df)
#df.to_csv("output.csv")