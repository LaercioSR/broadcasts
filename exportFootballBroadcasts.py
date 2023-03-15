import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

matches = []

url = 'https://www.uol.com.br/esporte/futebol/central-de-jogos/'
page = driver.get(url)
html = driver.page_source
driver.quit()
soup = BeautifulSoup(html, 'lxml')

matches_tag = soup.find_all("div", {"class": "match-wrapper"})

for match_tag in matches_tag:
    match = {}
    match_data = json.loads(match_tag['data-cfg'])
    match["competition"] = match_data["competicao"]
    match["date"] = match_data["data"]

    team_home = match_tag.find("div", {"class": "team-home"})
    match["team_home_name"] = team_home.find(
        "div", {"class": "team-name"}).get_text().strip()
    match["team_home_image"] = team_home.find("img")["src"]
    team_away = match_tag.find("div", {"class": "team-away"})
    match["team_away_name"] = team_away.find(
        "div", {"class": "team-name"}).get_text().strip()
    match["team_away_image"] = team_away.find("img")["src"]

    match["transmissions"] = []
    transmissions_tag = match_tag.find("div", {"class": "transmitions"})
    if transmissions_tag:
        for transmition in transmissions_tag.find_all("a"):
            match["transmissions"].append(transmition.get_text().strip())

    matches.append(match)

with open("exports/football.json", "w") as outfile:
    json.dump(matches, outfile, indent=2, ensure_ascii=False)
