# def get_recipes_ingredients_quantity_instructions(proper_link, recipies_name):
#     #Getting all recipies's ingredients, quantity, instructions
#     print("----- Taking care of ingredients, quantity, instructions ------")
#     recipes_dictionnary = {}
#     for url, name in tqdm(zip(proper_link, recipies_name)):
#         r = requests.get(url).text
#         soup = BeautifulSoup(r,features="html.parser")
#         ingredients = []
#         ingredient = soup.find_all("p", {"class" : "sc-9394dad-0 eERBYk"})
#         for element in ingredient:
#             ingredients.append(element.get_text(strip=True))
#         quantities = []
#         quantity = soup.find_all("p", {"class" : "sc-9394dad-0 cJeggo"})
#         for element in tqdm(quantity) :
#             quantities.append(element.get_text(strip=True))
#         recipe_dict = {ingredient: qty for ingredient, qty in zip(ingredients, quantities)}
#         recipes_instructions = []
#         instruction = soup.find_all("div", {"class" : "sc-9394dad-0 iYWTFs"})
#         for element in tqdm(instruction):
#                 recipes_instructions.append(element.get_text(strip=True))
        
#         recipes_dictionnary[name] = {"ingredients": recipe_dict, "instructions": recipes_instructions}
#     print("----- Taking care of ingredients, quantity, instructions done ------")
#     return recipes_dictionnary