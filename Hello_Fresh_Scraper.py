from bs4 import BeautifulSoup
import requests

main_url = "https://www.hellofresh.be/recipes?locale=fr-BE&redirectedFromAccountArea=true"

r = requests.get(main_url).text
soup = BeautifulSoup(r)
print(soup.prettify())