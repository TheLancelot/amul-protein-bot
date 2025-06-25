# products.py

# List of all products with their IDs and names (description & image omitted for backend use)
PRODUCTS = [
    {"id": "1", "name": "Amul Kool Protein Milkshake | Chocolate, 180 mL | Pack of 30"},
    {"id": "2", "name": "Amul Kool Protein Milkshake | Arabica Coffee, 180 mL | Pack of 8"},
    {"id": "3", "name": "Amul Kool Protein Milkshake | Arabica Coffee, 180 mL | Pack of 30"},
    {"id": "4", "name": "Amul Kool Protein Milkshake | Kesar, 180 mL | Pack of 8"},
    {"id": "5", "name": "Amul Kool Protein Milkshake | Kesar, 180 mL | Pack of 30"},
    {"id": "6", "name": "Amul High Protein Blueberry Shake, 200 mL | Pack of 30"},
    {"id": "7", "name": "Amul High Protein Paneer, 400 g | Pack of 24"},
    {"id": "8", "name": "Amul High Protein Paneer, 400 g | Pack of 2"},
    {"id": "9", "name": "Amul Whey Protein Gift Pack, 32 g | Pack of 10 sachets"},
    {"id": "10", "name": "Amul Whey Protein, 32 g | Pack of 30 Sachets"},
    {"id": "11", "name": "Amul Whey Protein, 32 g | Pack of 60 Sachets"},
    {"id": "12", "name": "Amul Chocolate Whey Protein Gift Pack, 34 g | Pack of 10 sachets"},
    {"id": "13", "name": "Amul Chocolate Whey Protein, 34 g | Pack of 30 sachets"},
    {"id": "14", "name": "Amul Chocolate Whey Protein, 34 g | Pack of 60 sachets"},
    {"id": "15", "name": "Amul High Protein Plain Lassi, 200 mL | Pack of 30"},
    {"id": "16", "name": "Amul High Protein Buttermilk, 200 mL | Pack of 30"},
    {"id": "17", "name": "Amul High Protein Rose Lassi, 200 mL | Pack of 30"},
    {"id": "18", "name": "Amul High Protein Milk, 250 mL | Pack of 8"},
    {"id": "19", "name": "Amul High Protein Milk, 250 mL | Pack of 32"},
]

# Mapping from ID → name
ID_TO_NAME = {p["id"]: p["name"] for p in PRODUCTS}

# Mapping from name → ID
NAME_TO_ID = {p["name"]: p["id"] for p in PRODUCTS}

# Utility to get all valid product IDs
VALID_IDS = set(ID_TO_NAME.keys())
