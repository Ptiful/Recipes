import Hello_Fresh_Scraper
from Hello_Fresh_Scraper import root_url

def main():
    soup = Hello_Fresh_Scraper.fetch_soup()
    links_with_text =  Hello_Fresh_Scraper.get_recipes_main_page(soup)
    
    if not links_with_text:
        print("Main recipe page not found.")
        return

    contries_recipes =  Hello_Fresh_Scraper.get_all_contries_recipes(root_url, links_with_text)
    recipes_from_contries =  Hello_Fresh_Scraper.get_all_recipes_from_collected_countries(root_url, links_with_text, contries_recipes)
    recipes_name =  Hello_Fresh_Scraper.getting_all_recipes_name(recipes_from_contries)
    french_recipes =  Hello_Fresh_Scraper.adding_french(recipes_from_contries)
    recipes_dict =  Hello_Fresh_Scraper.get_recipes_ingredients_quantity_instructions(french_recipes, recipes_name)
    Hello_Fresh_Scraper.save_to_file(recipes_dict)

if __name__ == "__main__":
    main()