import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["recipes_database"]
collection = db["recipes_collection"]

def filter_recipe_by_ingredients(recipe_data, desired_ingredients):
    filtered_ingredients = {ingredient: qty for ingredient, qty in recipe_data['ingredients'].items() if ingredient in desired_ingredients}
    return recipe_data['name'], filtered_ingredients, recipe_data['instructions']

desired_ingredients = ['Rigatoni']

recipe_data = collection.find_one({}) 

recipe_name, filtered_ingredients, instructions = filter_recipe_by_ingredients(recipe_data, desired_ingredients)

print("Recipe Name:", recipe_name)
print("Ingredients:")
for ingredient, qty in filtered_ingredients.items():
    print(f"- {ingredient}: {qty}")
print("Instructions:")
for instruction in instructions:
    print(instruction)
