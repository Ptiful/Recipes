# Recipes

This tool, for now, only collects all recipes from [Hello Fresh](https://www.hellofresh.be/) website.
It will be design so you input the ingredients you want to eat today and it will sort out all Hello Fresh recipes.

## Tools needed

[MongoDB](https://www.mongodb.com/docs/manual/installation/) up and running  
[Python](https://www.python.org/downloads/)  
[Visual Studio Code](https://code.visualstudio.com/download)

## How to run it on first time or if you want to update the database

Open your terminal, create an venv, activate it and install the requirements.txt :
```pip install -r requirements.txt```  
Then run :
``` python3 main.py```

### How to run it second time to select your meal

Open queries.py, input what you want to eat in line 11.  
Ex : ["Rigatoni"]  
And finally run : 
```python3 queries.py```

## What to add :

Need to refactor  
Typesense ?  
Connection to MongoDb automatic ?  
Docker ?  
API ?  
