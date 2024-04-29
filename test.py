import requests
from bs4 import BeautifulSoup
import re

import re

urls = ['https://www.hellofresh.be/recipes/mini-tortillas-au-ble-complet-garnies-de-pois-chiches-epices-65b107b0733ee86f886e08b5', 'https://www.hellofresh.be/recipes/salade-fusion-a-lasiatique-aux-eminces-vegetariens-65b107a4733ee86f886e0833']
recipies_name =[]
for url in urls:
    url = url.split("/recipes/")[-1]
    url = re.sub('[^a-zA-Z-]+', '', url)  # extract only alphabetic and hyphen characters
    url = url.rstrip("-")  # remove trailing hyphen, if any
    recipies_name.append(url)

print(recipies_name)
# root_url = "https://www.hellofresh.be/"

# r = requests.get(root_url).text
# soup = BeautifulSoup(r, features="html.parser")

# #Find the recipies main page
# print("----- Getting the main recipe page -----")
# links_with_text = []
# for a in soup.find_all('a', href=True): 
#     if a.text and '/recipes' in a['href']:
#             links_with_text.append(a['href'])
# print("----- Getting the main recipe page done -----")


# print("----- Getting all country recipe page -----")
# all_country_recipes = root_url + links_with_text[0]
# r2 = requests.get(all_country_recipes).text
# soup2 = BeautifulSoup(r2, features="html.parser")
# for a in soup2.find_all('a', href=True): 
#     if a.text: 
#         links_with_text.append(a['href'])
# print(links_with_text)
# country_recipies = []
# country_recipies.append([i for i in links_with_text if i.startswith('/recipes/')])
# not_nested_liste = country_recipies[0]
# print("----- Getting all country recipe page done -----")




#p class="sc-9394dad-0 cJeggo" for quantity
#p class="sc-9394dad-0 eERBYk" for ingredient
# urls = ['https://www.hellofresh.be/recipes/kruidige-kikkererwtenstoof-met-spinazie-en-witte-kaas-658d7d98f9d1ffb514ddb653', 'https://www.hellofresh.be/recipes/pikante-udon-noedels-met-gemarineerde-eieren-658d7d93f9d1ffb514ddb5f0']

# recipies_name =[]
# for url in urls:
#     recipies_name.append(url.split('/recipes/')[-1].rstrip("0123456789"))
# print(recipies_name)

# ingredients = []
# quantities = []

# for url in urls : 
#     r = requests.get(url).text
#     soup = BeautifulSoup(r,features="html.parser")
#     ingredients = []
#     ingredient = soup.find_all("p", {"class" : "sc-9394dad-0 eERBYk"})
#     for element in ingredient:
#         ingredients.append(element.get_text(strip=True))
#     quantities = []
#     quantity = soup.find_all("p", {"class" : "sc-9394dad-0 cJeggo"})
#     for element in quantity :
#         quantities.append(element.get_text(strip=True))

#     recipe_dict = {ingredient: qty for qty, ingredient in zip(quantities, ingredients)}
# print(recipe_dict)

# # Last step is to make a dictionnary with recipes name as main key, then ingredient as second key andfinal_dict = {}
# recipies_dictionnary = {recipies_name: name for name in zip(recipies_name, recipe_dict)}
# print(recipies_dictionnary)
    # for ingredient in ingredients:
    #     recipies_dictionnary[name].[ingredient]


# urls = ['https://www.hellofresh.be/recipes/kruidige-kikkererwtenstoof-met-spinazie-en-witte-kaas-658d7d98f9d1ffb514ddb653', 'https://www.hellofresh.be/recipes/pikante-udon-noedels-met-gemarineerde-eieren-658d7d93f9d1ffb514ddb5f0']

# recipies_name =[]
# for url in urls:
#     recipies_name.append(url.split('/recipes/')[-1].rstrip("0123456789"))

# recipies_dictionnary = {}

# for url, name in zip(urls, recipies_name):
#     r = requests.get(url).text
#     soup = BeautifulSoup(r,features="html.parser")
#     ingredients = []
#     ingredient = soup.find_all("p", {"class" : "sc-9394dad-0 eERBYk"})
#     for element in ingredient:
#         ingredients.append(element.get_text(strip=True))
#     quantities = []
#     quantity = soup.find_all("p", {"class" : "sc-9394dad-0 cJeggo"})
#     for element in quantity :
#         quantities.append(element.get_text(strip=True))

#     recipe_dict = {ingredient: qty for ingredient, qty in zip(ingredients, quantities)}
#     recipies_dictionnary[name] = recipe_dict

# print(recipies_dictionnary)