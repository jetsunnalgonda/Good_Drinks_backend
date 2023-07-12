import json

data = { "drinks": [
    { "name": "Mojito", "ingredients": ["white rum", "lime juice", "simple syrup", "mint leaves", "soda water"], "glass": "Collins glass", "instructions": "Muddle mint leaves with lime juice and simple syrup. Add rum and ice. Top with soda water. Garnish with mint sprig." },
    { "name": "Old Fashioned", "ingredients": ["bourbon", "sugar cube", "bitters", "orange peel", "cherry"], "glass": "Rocks glass", "instructions": "Place sugar cube in glass, add bitters and splash of water. Muddle until dissolved. Add bourbon and ice. Stir gently. Garnish with orange peel and cherry." },
    { "name": "Cosmopolitan", "ingredients": ["vodka", "cranberry juice", "triple sec", "lime juice"], "glass": "Cocktail glass", "instructions": "Combine all ingredients in a shaker with ice. Shake well. Strain into a chilled cocktail glass. Garnish with lime twist." },
    { "name": "Margarita", "ingredients": ["tequila", "lime juice", "triple sec", "salt"], "glass": "Margarita glass", "instructions": "Rub the rim of the glass with lime juice and dip in salt. Combine tequila, lime juice, and triple sec in a shaker with ice. Shake well. Strain into the glass. Garnish with lime wheel." },
    { "name": "Negroni", "ingredients": ["gin", "sweet vermouth", "Campari", "orange peel"], "glass": "Rocks glass", "instructions": "Stir gin, sweet vermouth, and Campari with ice in a mixing glass. Strain into an ice-filled rocks glass. Garnish with orange peel." },
    { "name": "Martini", "ingredients": ["gin", "dry vermouth", "olive"], "glass": "Martini glass", "instructions": "Combine gin and dry vermouth in a mixing glass with ice. Stir well. Strain into a chilled martini glass. Garnish with olive." },
    { "name": "Whiskey Sour", "ingredients": ["whiskey", "lemon juice", "simple syrup", "cherry", "orange slice"], "glass": "Rocks glass", "instructions": "Combine whiskey, lemon juice, and simple syrup in a shaker with ice. Shake well. Strain into an ice-filled rocks glass. Garnish with cherry and orange slice." },
    { "name": "Piña Colada", "ingredients": ["rum", "pineapple juice", "coconut cream", "pineapple wedge", "cherry"], "glass": "Hurricane glass", "instructions": "Blend rum, pineapple juice, and coconut cream with ice in a blender until smooth. Pour into a hurricane glass. Garnish with pineapple wedge and cherry." },
    { "name": "Screwdriver", "ingredients": ["vodka", "orange juice", "orange slice"], "glass": "Highball glass", "instructions": "Pour vodka and orange juice into a highball glass filled with ice. Stir well. Garnish with orange slice." },
    { "name": "Long Island Iced Tea", "ingredients": ["vodka", "tequila", "rum", "gin", "triple sec", "lemon juice", "simple syrup", "cola"], "glass": "Collins glass", "instructions": "Combine vodka, tequila, rum, gin, triple sec, lemon juice, and simple syrup in a shaker with ice. Shake well. Strain into an ice-filled Collins glass. Top with cola. Garnish with lemon wheel." },
    { "name": "Daiquiri", "ingredients": ["rum", "lime juice", "simple syrup"], "glass": "Cocktail glass", "instructions": "Combine rum, lime juice, and simple syrup in a shaker with ice. Shake well. Strain into a chilled cocktail glass. Garnish with lime wheel." },
    { "name": "Gin and Tonic", "ingredients": ["gin", "tonic water", "lime wedge"], "glass": "Highball glass", "instructions": "Fill a highball glass with ice. Pour gin over the ice. Top with tonic water. Garnish with lime wedge." },
    { "name": "White Russian", "ingredients": ["vodka", "coffee liqueur", "cream"], "glass": "Old-fashioned glass", "instructions": "Pour vodka and coffee liqueur over ice in an old-fashioned glass. Stir gently. Float cream on top." },
    { "name": "Mai Tai", "ingredients": ["rum", "lime juice", "orange curaçao", "orgeat syrup", "dark rum", "pineapple wedge", "cherry", "mint sprig"], "glass": "Collins glass", "instructions": "Shake rum, lime juice, orange curaçao, and orgeat syrup with ice. Strain into an ice-filled Collins glass. Float dark rum on top. Garnish with pineapple wedge, cherry, and mint sprig." },
    { "name": "Bloody Mary", "ingredients": ["vodka", "tomato juice", "lemon juice", "Worcestershire sauce", "hot sauce", "celery salt", "pepper", "celery stalk", "lemon wedge"], "glass": "Highball glass", "instructions": "Combine vodka, tomato juice, lemon juice, Worcestershire sauce, hot sauce, celery salt, and pepper in a mixing glass. Stir well. Pour into a highball glass filled with ice. Garnish with celery stalk and lemon wedge." },
    { "name": "Mimosa", "ingredients": ["champagne", "orange juice"], "glass": "Champagne flute", "instructions": "Pour equal parts champagne and orange juice into a chilled champagne flute." },
    { "name": "Sangria", "ingredients": ["red wine", "orange juice", "brandy", "simple syrup", "sliced fruit", "club soda"], "glass": "Wine glass", "instructions": "In a pitcher, combine red wine, orange juice, brandy, and simple syrup. Stir well. Add sliced fruit. Refrigerate for at least 4 hours. Serve in wine glasses with a splash of club soda." },
    { "name": "Caipirinha", "ingredients": ["cachaça", "lime", "sugar"], "glass": "Old-fashioned glass", "instructions": "Cut the lime into wedges. Muddle the lime wedges and sugar in an old-fashioned glass. Fill the glass with ice. Pour cachaça over the ice. Stir gently." },
    { "name": "Amaretto Sour", "ingredients": ["amaretto", "lemon juice", "simple syrup", "cherry", "orange slice"], "glass": "Rocks glass", "instructions": "Combine amaretto, lemon juice, and simple syrup in a shaker with ice. Shake well. Strain into an ice-filled rocks glass. Garnish with cherry and orange slice." },
    { "name": "Pina Colada", "ingredients": ["rum", "pineapple juice", "coconut cream"], "glass": "Hurricane glass", "instructions": "Blend rum, pineapple juice, and coconut cream with ice in a blender until smooth. Pour into a hurricane glass. Garnish with pineapple slice and cherry." }
  ]
}

import json
import csv

# Read the JSON file
# with open('drinks.json', 'r') as file:
#     data = json.load(file)

# Extract the list of drinks
drinks = data['drinks']

# Define the field names for the CSV
fieldnames = ['Name', 'Ingredients', 'Glass', 'Instructions']

# Open the CSV file for writing
with open('drinks.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write each drink as a row
    for drink in drinks:
        writer.writerow({
            'Name': drink['name'],
            'Ingredients': ', '.join(drink['ingredients']),
            'Glass': drink['glass'],
            'Instructions': drink['instructions']
        })