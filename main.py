from src import Hello_Fresh_Scraper
from src.Hello_Fresh_Scraper import root_url
import pymongo


def main():
    soup = Hello_Fresh_Scraper.fetch_soup()
    links_with_text =  Hello_Fresh_Scraper.get_recipes_main_page(soup)
    
    if not links_with_text:
        print("Main recipe page not found.")
        return

    contries_recipes =  Hello_Fresh_Scraper.get_all_contries_recipes(root_url, links_with_text)
    recipes_from_contries =  Hello_Fresh_Scraper.get_all_recipes_from_collected_countries(root_url, links_with_text, contries_recipes)
    recipes_name =  Hello_Fresh_Scraper.getting_all_recipes_name(recipes_from_contries)
    recipes_dict =  Hello_Fresh_Scraper.get_recipes_ingredients_quantity_instructions(recipes_from_contries, recipes_name)
    # Hello_Fresh_Scraper.save_to_file(recipes_dict)

    print("Sending data to MongoDb")
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client["recipes_database"]
    collection = db["recipes_collection"]
    recipes = recipes_dict
    collection.insert_one(recipes)
    print("Data has been published.")

if __name__ == "__main__":
    main()