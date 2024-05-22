from bs4 import BeautifulSoup
import requests
import re
import json

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
    recipies_url_not_parsed.append(root_url + element + "/?locale=fr-BE")

for url in recipies_url_not_parsed:
    r = requests.get(url).text
    soup = BeautifulSoup(r, features="html.parser")
    for a in soup.find_all("a", href=True):
        if a.text:
            links_with_text.append(a["href"])

recipies_url = []
recipies_url.append([i for i in links_with_text if re.search('\d+$', i)])
print("----- Getting all urls for cooking recipies from all countries done -----")

#Getting all recipies name
print("----- Getting recipies name -----")
recipies_name =[]
for url in recipies_url[0]:
    url = url.split("/recipes/")[-1]
    url = re.sub('[^a-zA-Z-]+', '', url)
    url = url.rstrip("-")
    recipies_name.append(url)
print("----- Done getting recipies name -----")

#Adding porper language to web page
proper_link = []
for link in recipies_url[0]:
    proper_link.append(link + "/?locale=fr-BE")

# #Getting all recipies's ingredients, quantity, instructions
print("----- Taking care of ingredients, quantity, instructions ------")
recipes_dictionnary = {}
for url, name in zip(proper_link, recipies_name):
    r = requests.get(url).text
    soup = BeautifulSoup(r,features="html.parser")
    ingredients = []
    ingredient = soup.find_all("p", {"class" : "sc-9394dad-0 eERBYk"})
    for element in ingredient:
        ingredients.append(element.get_text(strip=True))
    quantities = []
    quantity = soup.find_all("p", {"class" : "sc-9394dad-0 cJeggo"})
    for element in quantity :
        quantities.append(element.get_text(strip=True))

    recipe_dict = {ingredient: qty for ingredient, qty in zip(ingredients, quantities)}
    recipes_instructions = []
    instruction = soup.find_all("div", {"class" : "sc-9394dad-0 iYWTFs"})
    for element in instruction:
            recipes_instructions.append(element.get_text(strip=True))
    
    recipes_dictionnary[name] = {"ingredients": recipe_dict, "instructions": recipes_instructions}

    # recipe_dict = {ingredient: qty for ingredient, qty in zip(ingredients, quantities)}
    # recipies_dictionnary[name] = recipe_dict

print("----- Taking care of ingredients, quantity, instructions done ------")

with open("recipes.csv", "w") as f:
    json.dump(recipes_dictionnary,f)

#Rajouter MongoDB
#Rajouter Typesense
#Faire des fonctions
#MapPool
#Bar de progression