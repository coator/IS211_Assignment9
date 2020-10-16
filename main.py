from bs4 import BeautifulSoup
import requests

r = requests.get("https://www.cbssports.com/nfl/stats/player/scoring/nfl/regular/qualifiers")

soup = BeautifulSoup(r.text, 'html.parser')

d = soup.find_all('tr', {"class": 'TableBase-bodyTr'})

for dd in d:
    print(dd)