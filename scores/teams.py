from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/men/teams"

try:
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        pass
    else:
        print(f"Server is not connecter and returned a status code {response.status_code}")

except requests.ConnectionError:
    print("server is not connected")
except requests.HTTPError as httperr:
    print(f"http error is occured{httperr}")
except Exception as e:
    print(f"error occured {e}")

team_lst = []
ranking_lst = []
position_lst = []

soup = BeautifulSoup(response.content, 'html.parser')

name = soup.find_all("div", class_ = "cb-col cb-col-50 cb-lst-itm-sm text-left")
ranking = soup.find_all("div", class_ = "cb-col cb-col-14 cb-lst-itm-sm")

r = []
p = []
for i in range(0, len(ranking),2):
    r.append(ranking[i].text.strip())
for j in range(1, len(ranking), 2):
    p.append(ranking[j].text.strip())

for team,rank,pos in zip(name, r, p):
    names = team.text.strip()
    team_lst.append(names)
    ranking_lst.append(rank)
    position_lst.append(pos)

df = pd.DataFrame({"Teams":team_lst, "Rating":ranking_lst, "Position":position_lst})
df.to_csv("Teams_scores.csv",index = False)