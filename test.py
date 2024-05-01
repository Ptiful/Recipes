import requests
from bs4 import BeautifulSoup
import re

import re

url = "https://www.hellofresh.be/recipes/mijote-de-pois-chiches-epices-avec-pain-pita-complet-et-yaourt-658d7d98f9d1ffb514ddb653/?locale=fr-BE"

recipies_instructions = []

r = requests.get(url).text
soup = BeautifulSoup(r, features="html.parser")
instruction = soup.find_all("div", {"class" : "sc-9394dad-0 iYWTFs"})
for element in instruction:
        recipies_instructions.append(element.get_text(strip=True))

print(recipies_instructions)