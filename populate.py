import json
import sqlite3

# Load the JSON data
with open('drinks.json', 'r') as json_file:
    data = json.load(json_file)

# Extract the drinks list from the JSON
drinks = data['drinks']

# Define the SQLite database path
database_path = 'drinks.db'

# Connect to the SQLite database
conn = sqlite3.connect(database_path)
c = conn.cursor()

# Create a table for drinks
c.execute('''CREATE TABLE IF NOT EXISTS drinks
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             name TEXT,
             ingredients TEXT,
             glass TEXT,
             instructions TEXT,
             flavors TEXT,
             story TEXT)''')

# Insert each drink into the drinks table
for drink in drinks:
    # Extract the drink attributes
    # item = drink['ingredients']

    name = drink['name']
    # ingredients = json.dumps({item['name']: item['measurement'] for item in drink['ingredients']})
    ingredients = json.dumps(drink['ingredients'])
    glass = drink['glass']
    instructions = drink['instructions']
    # flavors = drink['flavors']
    flavors = ', '.join(drink['flavors'])
    # flavors = json.dumps(drink['flavors'])
    story = drink['story']

    # Insert the drink into the drinks table
    c.execute("INSERT INTO drinks (name, ingredients, glass, instructions, flavors, story) VALUES (?, ?, ?, ?, ?, ?)",
              (name, ingredients, glass, instructions, flavors, story))

# Commit the changes and close the connection
conn.commit()
conn.close()
