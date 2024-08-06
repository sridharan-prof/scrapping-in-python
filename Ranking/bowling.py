from bs4 import BeautifulSoup
import requests
import pandas as pd

df = None
url = "https://www.cricbuzz.com/cricket-stats/icc-rankings/men/bowling"

try:
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        pass
    else:
        print(f"Server is not reachable and returned a status code {response.status_code}")
except requests.ConnectionError:
    print("Failed to Connect to the server")
except requests.HTTPError as http_err:
    print(f"Http error occured {http_err}")
except Exception as e:
    print(f"An error is occured {e}")

soup = BeautifulSoup(response.content, 'html.parser')

header_lst = []
num_list = []
player_list = []
rating_list = []

number = soup.find_all("div", class_ = "cb-col cb-col-16 cb-rank-tbl cb-font-16")
Name = soup.find_all("a", class_ = "text-hvr-underline text-bold cb-font-16")
Ranking = soup.find_all("div", class_ = "cb-col cb-col-17 cb-rank-tbl pull-right")

position = soup.find("div", class_ = "cb-col cb-col-16 text-left cb-rank-plyr")
player = soup.find("div", class_ = "cb-col cb-col-50 text-left")
rating = soup.find("div", class_ = "cb-col cb-col-17 pull-right")

for position1, player1, rating1 in zip(position,player,rating):
    position_name = position1.text.strip()
    player_name = player1.text.strip()
    rating_name = rating1.text.strip()
    header_lst.append(position_name)
    header_lst.append(rating_name)
    header_lst.append(player_name)
    print(f"{position_name}\t\t{player_name}\t\t\t{rating_name}")
    print()

for number_tag, Name_tag, rank_tag in zip(number,Name,Ranking):
    number_element = number_tag.text.strip()
    name_element = Name_tag.text.strip()
    ranking_element = rank_tag.text.strip()
    num_list.append(number_element)
    player_list.append(name_element)
    rating_list.append(ranking_element)
    
df = pd.DataFrame({"Position":num_list, "Player":player_list, "Rating":rating_list})
df.to_csv("bowling.csv",index = False)
