from bs4 import BeautifulSoup
import requests
import re

#import Hello Fresh root url
root_url = "https://www.hellofresh.be"

r = requests.get(root_url).text
soup = BeautifulSoup(r, features="html.parser")

#Find the recipies main page
print("----- Getting the main recipe page -----")
links_with_text = []
for a in soup.find_all('a', href=True): 
    if a.text and '/recipes' in a['href']:
            links_with_text.append(a['href'])
print("----- Getting the main recipe page done -----")

#Find all type of recipies depending of their countries
print("----- Getting all country recipe page -----")
all_country_recipes = root_url + links_with_text[0]
r2 = requests.get(all_country_recipes).text
soup2 = BeautifulSoup(r2, features="html.parser")
for a in soup2.find_all('a', href=True): 
    if a.text: 
        links_with_text.append(a['href'])
country_recipies = []
country_recipies.append([i for i in links_with_text if i.startswith('/recipes/')])
not_nested_liste = country_recipies[0]
print("----- Getting all country recipe page done -----")

#Start looping over all collected urls to get to their recipies
print("----- Getting all urls for cooking recipies from all countries -----")
recipies_url_not_parsed = []
for element in not_nested_liste:
    recipies_url_not_parsed.append(root_url + element)

for url in recipies_url_not_parsed:
    r = requests.get(url).text
    soup = BeautifulSoup(r, features="html.parser")
    for a in soup.find_all("a", href=True):
        if a.text:
            links_with_text.append(a["href"])
recipies_url = []
recipies_url.append([i for i in links_with_text if re.search('\d+$', i)])
print(recipies_url)
print("----- Getting all urls for cooking recipies from all countries done -----")


print("----- Taking care of ingredients ------")
print("----- Taking care of ingredients done ------")