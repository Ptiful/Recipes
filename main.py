from src import Hello_Fresh_Scraper
from src.Hello_Fresh_Scraper import root_url
import pymongo

def main():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["recipes_database"]
    collection = db["recipes_collection"]

    soup = Hello_Fresh_Scraper.fetch_soup()
    links_with_text = Hello_Fresh_Scraper.get_recipes_main_page(soup)
    country_recipes = Hello_Fresh_Scraper.get_all_contries_recipes(root_url, links_with_text)
    all_recipe_links = Hello_Fresh_Scraper.get_all_recipes_from_collected_countries(root_url, country_recipes,links_with_text)
    recipe_names = Hello_Fresh_Scraper.getting_all_recipes_name(all_recipe_links)
    french_links = Hello_Fresh_Scraper.adding_french(all_recipe_links)
    recipes_details = Hello_Fresh_Scraper.get_recipes_ingredients_quantity_instructions(french_links, recipe_names, collection)
    # save_to_file(recipes_details)
    collection.create_index("ingredients")
    collection.create_index("_id")

if __name__ == "__main__":
    main()