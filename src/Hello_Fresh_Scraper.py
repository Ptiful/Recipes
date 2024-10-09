from bs4 import BeautifulSoup
import requests
import re
import json
from tqdm import tqdm
from multiprocessing import Pool, cpu_count
from typing import Tuple, List, Dict, Union

root_url = "https://www.hellofresh.com"

def fetch_soup() -> BeautifulSoup: 
    #Import Hello Fresh root url
    r = requests.get(root_url).text
    soup = BeautifulSoup(r, features="html.parser")
    return soup


def get_recipes_main_page(soup:BeautifulSoup) -> List[str]:
    #Find the recipes main page
    links_with_text = []
    for a in tqdm(soup.find_all("a", href=True), desc="Finding main recipe page links"): 
        if a.text and "/recipes" in a["href"]:
                links_with_text.append(a["href"])
    return links_with_text


def get_all_contries_recipes(root_url:str, links_with_text:List[str]) -> List[str]:
    #Find all type of recipies depending of their countries
    all_country_recipes = root_url + links_with_text[0]
    r2 = requests.get(all_country_recipes).text
    soup2 = BeautifulSoup(r2, features="html.parser")
    for a in tqdm(soup2.find_all("a", href=True), desc = "Getting all country recipe page"): 
        if a.text: 
            links_with_text.append(a["href"])
    country_recipies = []
    country_recipies.extend([i for i in links_with_text if i.startswith("/recipes/")])
    return country_recipies


def get_all_recipes_from_collected_countries(root_url:str, links_with_text:List[str], country_recipies:List[str]) ->list[str]:
    #Start looping over all collected urls to get to their recipies
    recipies_url_not_parsed = []
    for element in tqdm(country_recipies, desc = "Getting all urls for cooking recipies from all countries"):
        recipies_url_not_parsed.append(root_url + element + "/?locale=fr-BE")

    for url in tqdm(recipies_url_not_parsed):
        r = requests.get(url).text
        soup = BeautifulSoup(r, features="html.parser")
        for a in soup.find_all("a", href=True):
            if a.text:
                links_with_text.append(a["href"])

    recipes_url = []
    recipes_url.extend([i for i in links_with_text if re.search("\d+$", i)])
    return recipes_url


def getting_all_recipes_name(recipes_url:List[str]) -> List[str]:
    #Getting all recipes name
    recipes_name =[]
    for url in tqdm(recipes_url, desc = "Getting recipies name"):
        url = url.split("/recipes/")[-1]
        url = re.sub("[^a-zA-Z-]+", "", url)
        url = re.sub(r'-[^-]+$', '', url)
        url = url.rstrip("-")
        recipes_name.append(url)
    return recipes_name


def fetch_recipe_details(args: Tuple[str, str]) -> Tuple[str, Dict[str, Union[Dict[str, str], List[str]]]]:
    #Collecting all ingredients, quantities and instructions to a dictionnary
    url, name = args
    r = requests.get(url).text
    soup = BeautifulSoup(r, features="html.parser")
    
    ingredients = []
    ingredient = soup.find_all("p", {"class": "sc-54d3413f-0 jELdJr"})
    for element in ingredient:
        ingredients.append(element.get_text(strip=True))
    
    quantities = []
    quantity = soup.find_all("p", {"class": "sc-54d3413f-0 ccrEYr"})
    for element in quantity:
        quantities.append(element.get_text(strip=True))
    
    recipe_dict = {ingredient: qty for ingredient, qty in zip(ingredients, quantities)}
    
    recipes_instructions = []
    instruction = soup.find_all("span", {"class": "sc-54d3413f-0 gNOFyU"})
    for element in instruction:
        recipes_instructions.append(element.get_text(strip=True))
    
    return name, {"ingredients": recipe_dict, "instructions": recipes_instructions}


def get_recipes_ingredients_quantity_instructions(proper_link:List[str], recipies_name:List[str]) ->Dict:
    #Adding all ingredients, quantities and instructions to a dictionnary
    recipes_dictionnary = {}

    with Pool(cpu_count()) as p:
        for name, details in tqdm(p.imap(fetch_recipe_details, zip(proper_link, recipies_name)), total=len(recipies_name), desc="Fetching recipes details"):
            recipes_dictionnary[name] = details

    return recipes_dictionnary


def save_to_file(data, filename="recipes.json"):
    #Save the recipes dictionary to a JSON file
    with open(filename, "w",encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
