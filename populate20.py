import sqlite3
import json

# Read the JSON file
with open('drinks.json', 'r') as file:
    data = json.load(file)

# Extract the list of drinks
drinks = data['drinks']

# Connect to the SQLite database
conn = sqlite3.connect('data.db')
cursor = conn.cursor()

# Create a table for drinks
cursor.execute('CREATE TABLE IF NOT EXISTS drinks (id INTEGER PRIMARY KEY, name TEXT, ingredients TEXT, glass TEXT, instructions TEXT)')

# Insert each drink into the table
for drink in drinks:
    name = drink['name']
    ingredients = ', '.join(drink['ingredients'])
    glass = drink['glass']
    instructions = drink['instructions']

    # Insert the drink into the table
    cursor.execute('INSERT INTO drinks (name, ingredients, glass, instructions) VALUES (?, ?, ?, ?)', (name, ingredients, glass, instructions))

# Commit the changes and close the connection
conn.commit()
conn.close()