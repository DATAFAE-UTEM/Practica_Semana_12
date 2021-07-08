import pandas as pd
import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/VISA.VI/key-statistics?p=VISA.VI&guccounter=1'

r = requests.get(url)
html = r.text

soup = BeautifulSoup(html)
table = soup.find('table', {"class": "W(100%) Bdcl(c) "})
rows = table.find_all('tr')
data = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

result = pd.DataFrame(data, columns=['Valuation_measures', 'Values'])

print(result)