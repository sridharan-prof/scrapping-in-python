from bs4 import BeautifulSoup
import requests

url = "https://www.cricbuzz.com/cricket-schedule/upcoming-series/international"

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

soup = BeautifulSoup(response.text, 'html.parser')

# SCHEDULE
date_lst = []
match_lst = []
team = []
timing = []

schedule_date = soup.find_all('div', class_ = "cb-lv-grn-strip text-bold")
schedule_match = soup.find_all('a', class_ = "cb-col-33 cb-col cb-mtchs-dy text-bold")
teams = soup.find_all('div', class_ = "cb-ovr-flo cb-col-60 cb-col cb-mtchs-dy-vnu cb-adjst-lst")
time = soup.find_all('div', class_ = "cb-col-40 cb-col cb-mtchs-dy-tm cb-adjst-lst")
for schedule, match,t,local in zip(schedule_date,schedule_match,teams,time):
    initial_date = schedule.text.strip()
    match_game = match.text.strip()
    vs = t.text.strip()
    clock = local.text.strip()
    date_lst.append(initial_date)
    match_lst.append(match_game)
    team.append(vs)
    timing.append(clock)


for schedule, match,t,local in zip(date_lst,match_lst,team,timing):
    print(f"Date  : {schedule}\nGame  : {match}\nTeams :{t}\nTime  :{local}")
    print()
