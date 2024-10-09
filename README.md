# Recipes

This tool, for now, only collects all recipes from [Hello Fresh](https://www.hellofresh.be/) website.
It will be designed for  you to input the ingredients you want to eat today and it will sort out all the possible Hello Fresh recipes.

## Tools needed

[MongoDB](https://www.mongodb.com/docs/manual/installation/) up and running  
[Python 3.11](https://www.python.org/downloads/)  

## How to run it on first time or if you want to update the database

Open your terminal, create an venv, activate it and install the requirements.txt :
```pip install -r requirements.txt```  
Then run :
``` python3 main.py```

### How to run it second time to select your meal

Open queries.py, input what you want to eat in line 15.  
```desired_ingredients = ['Oignon']```  
Or if you know the name of the recipe, juste change ```recipe_name = "Carbonara"``` line 16 and replace line 15 by ```desired_ingredients = None```

And finally run : 
```python3 queries.py```

## What to add :

Need to refactor  
Typesense ?  
Automatic connection to MongoDb ?  
Docker ?  
API ?  
