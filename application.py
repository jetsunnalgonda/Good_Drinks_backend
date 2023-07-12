from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask import send_file
from socket import gethostname
import sqlite3
import random
import os

app = Flask(__name__)
# DATABASE = 'drinks.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///drinks.db'
db = SQLAlchemy(app)
DATABASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'drinks.db')

# Create drinks table in the database
def create_table():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS drinks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 ingredients TEXT,
                 glass TEXT,
                 instructions TEXT)''')
    conn.commit()
    conn.close()


# Get all drinks
@app.route('/api/drinks', methods=['GET'])
def get_all_drinks():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM drinks")
    rows = c.fetchall()
    conn.close()
    drinks = [{'id': row[0], 'name': row[1], 'ingredients': row[2], 'glass': row[3], 'instructions': row[4]} for row in rows]
    return jsonify(drinks)

# Get drink image
@app.route('/api/drinks/image/<drink_id>', methods=['GET'])
def get_drink_image(drink_id):
    # Assuming the images are stored in a directory named "images" in the same directory as the script
    image_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
    
    # Retrieve the drink by ID from the database
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM drinks WHERE id=?", (drink_id,))
    row = c.fetchone()
    conn.close()
    
    if row:
        # Extract the drink name from the row
        drink_name = row[1]
        
        # Construct the image filename based on the drink name
        image_filename = f"{drink_name.lower().replace(' ', '_')}.jpg"
        image_path = os.path.join(image_dir, image_filename)
        
        if os.path.isfile(image_path):
            # Send the image file as a response
            return send_from_directory(image_dir, image_filename)
    
    # If the drink or image is not found, return a default image or an error message
    default_image_filename = 'default.jpg'
    default_image_path = os.path.join(image_dir, default_image_filename)
    return send_from_directory(image_dir, default_image_filename) if os.path.isfile(default_image_path) else jsonify({'message': 'Image not found'}), 404

# @app.route('/api/drinks/image/<drink_id>', methods=['GET'])
# def get_drink_image(drink_id):
#     conn = sqlite3.connect(DATABASE)
#     c = conn.cursor()
#     c.execute("SELECT image_path FROM drinks WHERE id=?", (drink_id,))
#     row = c.fetchone()
#     conn.close()
    
#     if row:
#         image_path = row[0]
#         # Assuming the images are stored in a directory named 'drink_images'
#         full_image_path = os.path.join('drink_images', image_path)

#         # Check if the image file exists
#         if os.path.exists(full_image_path):
#             return send_file(full_image_path, mimetype='image/jpeg')  # Adjust the mimetype based on your image type
#         else:
#             return jsonify({'message': 'Drink image not found'}), 404
#     else:
#         return jsonify({'message': 'Drink image not found'}), 404

# Get a random drink
@app.route('/api/drinks/random', methods=['GET'])
def get_random_drink():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM drinks")
    rows = c.fetchall()
    conn.close()
    if rows:
        random_row = random.choice(rows)
        drink = {'id': random_row[0], 'name': random_row[1], 'ingredients': random_row[2], 'glass': random_row[3], 'instructions': random_row[4]}
        return jsonify(drink)
    return jsonify({'message': 'No drinks found'}), 404

# Get a specific drink by ID
@app.route('/api/drinks/<drink_id>', methods=['GET'])
def get_drink(drink_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("SELECT * FROM drinks WHERE id=?", (drink_id,))
    row = c.fetchone()
    conn.close()
    if row:
        drink = {'id': row[0], 'name': row[1], 'ingredients': row[2], 'glass': row[3], 'instructions': row[4]}
        return jsonify(drink)
    return jsonify({'message': 'Drink not found'}), 404



# Create a new drink
@app.route('/api/drinks', methods=['POST'])
def create_drink():
    data = request.get_json()
    drink = (data['name'], data['ingredients'], data['instructions'])
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("INSERT INTO drinks (name, ingredients, instructions) VALUES (?, ?, ?)", drink)
    conn.commit()
    drink_id = c.lastrowid
    conn.close()
    new_drink = {'id': drink_id, 'name': data['name'], 'ingredients': data['ingredients'], 'instructions': data['instructions'], 'glass': data['glass']}
    return jsonify(new_drink), 201

# Update an existing drink
@app.route('/api/drinks/<drink_id>', methods=['PUT'])
def update_drink(drink_id):
    data = request.get_json()
    drink = (data['name'], data['ingredients'], data['instructions'], drink_id)
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("UPDATE drinks SET name=?, ingredients=?, instructions=? WHERE id=?", drink)
    conn.commit()
    conn.close()
    return jsonify({'message': 'Drink updated'})

# Delete a drink
@app.route('/api/drinks/<drink_id>', methods=['DELETE'])
def delete_drink(drink_id):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute("DELETE FROM drinks WHERE id=?", (drink_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Drink deleted'})

# For the local machine:
# if __name__ == '__main__':
#     create_table()
#     print(os.getcwd())
#     app.run(debug=True)

# For the www.pythonanywhere.com server
if __name__ == '__main__':
    db.create_all()
    print(os.getcwd())
    if 'liveconsole' not in gethostname():
        app.run()
