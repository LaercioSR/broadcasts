import urllib.request
from requests_html import HTMLSession
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = False
driver = webdriver.Firefox(options=options)

url = 'https://www.uol.com.br/esporte/futebol/central-de-jogos/'
driver.get(url)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')

matches = soup.find_all("div", {"class": "match-wrap"})

matchesFile = open("file.txt", "w")
matchesFile.write(matches)
matchesFile.close()

# pageFile = open("index.html", "w")
# pageFile.write(html)
# pageFile.close()

print(matches)

driver.quit()
