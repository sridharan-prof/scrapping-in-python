from bs4 import BeautifulSoup
import requests

url ="https://www.cricbuzz.com/cricket-match/live-scores"

try:
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        pass
    else:
        print(f"server is not reachable and returned a status code: {response.status_code}")
except requests.ConnectionError:
    print("Failed to connect to the server")
except requests.HTTPError as http_err:
    print(f"http error occered:{http_err}")
except Exception as e:
    print("An error occured:{e}")

soup = BeautifulSoup(response.content,'html.parser')

team = []
two_teams = []

match = soup.find_all('div', class_ = "cb-col-100 cb-col cb-schdl cb-billing-plans-text")
team_1_vs_team_2 = soup.find_all('div', class_ = "cb-scr-wll-chvrn cb-lv-scrs-col")

for matches in match:
    game = matches.text.strip()
    team.append(game)
    
for vs in team_1_vs_team_2:
    live_team = vs.text.strip()
    two_teams.append(live_team)


for matches,vs in zip(team,two_teams):
    print(f"Live Match  : {matches}")
    print(f"Scored      : {vs}")
    print()
