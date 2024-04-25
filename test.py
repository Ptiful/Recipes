import requests
from bs4 import BeautifulSoup

#p class="sc-9394dad-0 cJeggo" for quantity
#p class="sc-9394dad-0 eERBYk" for ingredient
url = 'https://www.hellofresh.be/recipes/romige-orzo-met-witloof-658d7e22f9d1ffb514ddb9f4'
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

recipe_dict = {ingredient: qty for qty, ingredient in zip(quantities, ingredients)}
print(recipe_dict)