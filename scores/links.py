from bs4 import BeautifulSoup
import requests

url = "https://www.cricbuzz.com/cricket-match/live-scores"

try:
    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        pass
    else:
        print(f"server is not reachable and returned a status code:{response.status_code}")
except requests.ConnectionError:
    print("Failed to connect to the server")
except requests.HTTPError as http_err:
    print(f"http error occurred:{http_err}")
except Exception as e:
    print("An error occured:{e}")

soup = BeautifulSoup(response.content, 'html.parser')

def link_list():
    link_lst = []
    link_lst2 = []

    live = soup.find_all("a", class_ = "cb-lv-scrs-well cb-lv-scrs-well-live")
    compete = soup.find_all("a", class_ = "cb-lv-scrs-well cb-lv-scrs-well-complete")

    for link1 in live:
        link_element1 = link1.get("href")
        if link_element1:
            link_lst.append(link_element1)

    for link2 in compete:
        link_element2 = link2.get('href')
        if link_element2:
            link_lst2.append(link_element2)
    return link_lst,link_lst2[0]
link_list()
