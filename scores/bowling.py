from bs4 import BeautifulSoup
import requests

url = "https://www.cricbuzz.com/live-cricket-scores/96177/wicxi-vs-rsa-4-day-warm-up-match-south-africa-tour-of-west-indies-2024"

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

soup = BeautifulSoup(response.content, 'html.parser')

batter_bowler = []
score_board = []

batter = soup.find_all('div', class_ = "cb-col cb-col-50")
score = soup.find_all('div', class_ = "cb-col cb-col-100 cb-min-hdr-rw cb-bg-gray")

for name in batter:
    names = name.text.strip()
    batter_bowler.append(names)

for runs in score:
    score_sheet = runs.text.strip()
    score_board.append(score_sheet)

for index,value in enumerate(batter_bowler):
    if index > 2:
        print(f"{value}")