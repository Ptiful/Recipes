import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["recipes_database"]
collection = db["recipes_collection"]

def build_query(desired_ingredients=None, recipe_name=None):
    query = {}
    if desired_ingredients:
        query['$or'] = [{'ingredients.' + ingredient: {'$exists': True}} for ingredient in desired_ingredients]
    if recipe_name:
        query['_id'] = recipe_name
    return query

desired_ingredients = ['Oignon']
recipe_name = None #"mijote-de-legumes-a-la-marocaine-et-fromage-grec-fbdefb"

query = build_query(desired_ingredients, recipe_name)
recipe_data = collection.find(query)

for recipe in recipe_data:
    print("Recipe Name:", recipe['_id'])
    print("Ingredients:")
    for ingredient, qty in recipe['ingredients'].items():
        print(f"- {ingredient}: {qty}")
    print("Instructions:")
    for instruction in recipe['instructions']:
        print(instruction)
    print("\n")

