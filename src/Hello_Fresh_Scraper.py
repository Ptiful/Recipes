from bs4 import BeautifulSoup
import requests
import re
import json
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from typing import Tuple, List, Dict, Union

root_url = "https://www.hellofresh.be"
def fetch_soup() -> BeautifulSoup: 
    r = requests.get(root_url).text
    soup = BeautifulSoup(r, features="html.parser")
    return soup

def get_recipes_main_page(soup: BeautifulSoup) -> List[str]:
    links_with_text = []
    for a in tqdm(soup.find_all("a", href=True), desc="Finding main recipe page links"): 
        if a.text and "/recipes" in a["href"]:
            links_with_text.append(a["href"])
    return links_with_text

def get_all_contries_recipes(root_url: str, links_with_text: List[str]) -> List[str]:
    all_country_recipes = root_url + links_with_text[0]
    r2 = requests.get(all_country_recipes).text
    soup2 = BeautifulSoup(r2, features="html.parser")
    for a in tqdm(soup2.find_all("a", href=True), desc="Getting all country recipe page"): 
        if a.text: 
            links_with_text.append(a["href"])
    country_recipies = [i for i in links_with_text if i.startswith("/recipes/")]
    return country_recipies

def get_all_recipes_from_collected_countries(root_url: str, country_recipes: List[str],links_with_text: List[str]) -> List[str]:
    recipes_url_not_parsed = []
    for element in tqdm(country_recipes, desc="Getting all urls for cooking recipes from all countries"):
        recipes_url_not_parsed.append(root_url + element + "/?locale=fr-BE")

    for url in tqdm(recipes_url_not_parsed):
        r = requests.get(url).text
        soup = BeautifulSoup(r, features="html.parser")
        for a in soup.find_all("a", href=True):
            if a.text:
                links_with_text.append(a["href"])

    recipes_url = [i for i in links_with_text if re.search(r"\d+$", i)]
    return recipes_url

def getting_all_recipes_name(recipes_url: List[str]) -> List[str]:
    recipes_name = []
    for url in tqdm(recipes_url, desc="Getting recipes name"):
        url = url.split("/recipes/")[-1]
        url = re.sub("[^a-zA-Z-]+", "", url)
        url = url.rstrip("-")
        recipes_name.append(url)
    return recipes_name

def adding_french(recipes_url: List[str]) -> List[str]:
    proper_link = []
    for link in tqdm(recipes_url, desc="Adding French language to recipes"):
        proper_link.append(link + "/?locale=fr-BE")
    return proper_link

def fetch_recipe_details(args: Tuple[str, str]) -> Tuple[str, Dict[str, Union[Dict[str, str], List[str]]]]:
    url, name = args
    r = requests.get(url).text
    soup = BeautifulSoup(r, features="html.parser")
    
    ingredients = []
    ingredient = soup.find_all("p", {"class": "sc-9394dad-0 eERBYk"})
    for element in ingredient:
        ingredients.append(element.get_text(strip=True))
    
    quantities = []
    quantity = soup.find_all("p", {"class": "sc-9394dad-0 cJeggo"})
    for element in quantity:
        quantities.append(element.get_text(strip=True))
    
    recipe_dict = {ingredient: qty for ingredient, qty in zip(ingredients, quantities)}
    
    recipes_instructions = []
    instruction = soup.find_all("div", {"class": "sc-9394dad-0 iYWTFs"})
    for element in instruction:
        recipes_instructions.append(element.get_text(strip=True))
    
    return name, {"ingredients": recipe_dict, "instructions": recipes_instructions}

def get_recipes_ingredients_quantity_instructions(proper_link: List[str], recipies_name: List[str], collection) -> Dict:
    recipes_dictionnary = {}

    with Pool(cpu_count()) as p:
        for name, details in tqdm(p.imap(fetch_recipe_details, zip(proper_link, recipies_name)), total=len(recipies_name), desc="Fetching recipes details"):
            recipes_dictionnary[name] = details

            collection.update_one(
                {"_id": name},
                {"$set": details},
                upsert=True
            )

    return recipes_dictionnary

def save_to_file(data, filename="recipes.json"):
    with open(filename, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# def main():
#     root_url = "https://www.hellofresh.be"
#     client = pymongo.MongoClient("mongodb://localhost:27017")
#     db = client["recipes_database"]
#     collection = db["recipes_collection"]

#     soup = fetch_soup()
#     links_with_text = get_recipes_main_page(soup)
#     country_recipes = get_all_contries_recipes(root_url, links_with_text)
#     all_recipe_links = get_all_recipes_from_collected_countries(root_url, country_recipes)
#     recipe_names = getting_all_recipes_name(all_recipe_links)
#     french_links = adding_french(all_recipe_links)
#     recipes_details = get_recipes_ingredients_quantity_instructions(french_links, recipe_names)
#     # save_to_file(recipes_details)
#     collection.create_index("ingredients")
#     collection.create_index("_id")

# if __name__ == "__main__":
#     main()
