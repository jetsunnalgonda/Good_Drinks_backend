import json

# Load the JSON data
with open('drinks.json', 'r') as json_file:
    data = json.load(json_file)

# Get the list of ingredients from the data
drinks = data['drinks']

# Create an empty set to store the unique flavors
unique_bases = set()

# Extract the bases from the ingredients and store them in a set to get unique bases
bases = set()
for drink in drinks:
    ingredients = drink['ingredients']
    for ingredient in ingredients:
        base = ingredient.get("base")
        # print(base)
        if base:
            unique_bases.add(base)
base_list = list(unique_bases)

# Print the unique bases
print(list(base_list))