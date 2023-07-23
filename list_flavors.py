import json

# Load the JSON data
with open('drinks.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the drinks list from the JSON
drinks = data['drinks']

# Create an empty set to store the unique flavors
unique_flavors = set()

# Iterate over the drinks and extract the flavors
for drink in drinks:
    flavors = drink['flavors']
    unique_flavors.update(flavors)

# Convert the set to a list
flavors_list = list(unique_flavors)

print(flavors_list)