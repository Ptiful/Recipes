from bs4 import BeautifulSoup
import requests

main_url = "https://www.hellofresh.be/recipes?locale=fr-BE&redirectedFromAccountArea=true"

r = requests.get(main_url).text
soup = BeautifulSoup(r, features="html.parser")
most_popular = soup.find_all("h2")[0].get_text()
href = soup.find_all("div", {"class": "web-gg4vpm"})
# print(most_popular)
print(href)