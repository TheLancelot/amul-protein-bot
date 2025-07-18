# products.py

# List of all products with their IDs and names (description & image omitted for backend use)
# PRODUCTS = [
#     {"id": "1", "name": "Amul Kool Protein Milkshake | Chocolate, 180 mL | Pack of 30"},
#     {"id": "2", "name": "Amul Kool Protein Milkshake | Arabica Coffee, 180 mL | Pack of 8"},
#     {"id": "3", "name": "Amul Kool Protein Milkshake | Arabica Coffee, 180 mL | Pack of 30"},
#     {"id": "4", "name": "Amul Kool Protein Milkshake | Kesar, 180 mL | Pack of 8"},
#     {"id": "5", "name": "Amul Kool Protein Milkshake | Kesar, 180 mL | Pack of 30"},
#     {"id": "6", "name": "Amul High Protein Blueberry Shake, 200 mL | Pack of 30"},
#     {"id": "7", "name": "Amul High Protein Paneer, 400 g | Pack of 24"},
#     {"id": "8", "name": "Amul High Protein Paneer, 400 g | Pack of 2"},
#     {"id": "9", "name": "Amul Whey Protein Gift Pack, 32 g | Pack of 10 sachets"},
#     {"id": "10", "name": "Amul Whey Protein, 32 g | Pack of 30 Sachets"},
#     {"id": "11", "name": "Amul Whey Protein, 32 g | Pack of 60 Sachets"},
#     {"id": "12", "name": "Amul Chocolate Whey Protein Gift Pack, 34 g | Pack of 10 sachets"},
#     {"id": "13", "name": "Amul Chocolate Whey Protein, 34 g | Pack of 30 sachets"},
#     {"id": "14", "name": "Amul Chocolate Whey Protein, 34 g | Pack of 60 sachets"},
#     {"id": "15", "name": "Amul High Protein Plain Lassi, 200 mL | Pack of 30"},
#     {"id": "16", "name": "Amul High Protein Buttermilk, 200 mL | Pack of 30"},
#     {"id": "17", "name": "Amul High Protein Rose Lassi, 200 mL | Pack of 30"},
#     {"id": "18", "name": "Amul High Protein Milk, 250 mL | Pack of 8"},
#     {"id": "19", "name": "Amul High Protein Milk, 250 mL | Pack of 32"},
# ]

# # Mapping from ID → name
# ID_TO_NAME = {p["id"]: p["name"] for p in PRODUCTS}

# products.py

PRODUCTS = [
    {"id": "1", "name": "Amul Kool Protein Milkshake | Chocolate, 180 mL | Pack of 30", 
     "alias": "amul-kool-protein-milkshake-or-chocolate-180-ml-or-pack-of-30"},
    {"id": "2", "name": "Amul Kool Protein Milkshake | Arabica Coffee, 180 mL | Pack of 8",   
     "alias": "amul-kool-protein-milkshake-or-arabica-coffee-180-ml-or-pack-of-8"},
    {"id": "3", "name": "Amul Kool Protein Milkshake | Arabica Coffee, 180 mL | Pack of 30",  
     "alias": "amul-kool-protein-milkshake-or-arabica-coffee-180-ml-or-pack-of-30"},
    {"id": "4", "name": "Amul Kool Protein Milkshake | Kesar, 180 mL | Pack of 8",           
     "alias": "amul-kool-protein-milkshake-or-kesar-180-ml-or-pack-of-8"},
    {"id": "5", "name": "Amul Kool Protein Milkshake | Kesar, 180 mL | Pack of 30",          
     "alias": "amul-kool-protein-milkshake-or-kesar-180-ml-or-pack-of-30"},
    {"id": "6", "name": "Amul High Protein Blueberry Shake, 200 mL | Pack of 30",           
     "alias": "amul-high-protein-blueberry-shake-200-ml-or-pack-of-30"},
    {"id": "7", "name": "Amul High Protein Paneer, 400 g | Pack of 24",                    
     "alias": "amul-high-protein-paneer-400-g-or-pack-of-24"},
    {"id": "8", "name": "Amul High Protein Paneer, 400 g | Pack of 2",                     
     "alias": "amul-high-protein-paneer-400-g-or-pack-of-2"},
    {"id": "9", "name": "Amul Whey Protein Gift Pack, 32 g | Pack of 10 sachets",          
     "alias": "amul-whey-protein-gift-pack-32-g-or-pack-of-10-sachets"},
    {"id": "10","name": "Amul Whey Protein, 32 g | Pack of 30 Sachets",                    
     "alias": "amul-whey-protein-32-g-or-pack-of-30-sachets"},
    {"id": "11","name": "Amul Whey Protein, 32 g | Pack of 60 Sachets",                    
     "alias": "amul-whey-protein-32-g-or-pack-of-60-sachets"},
    {"id": "12","name": "Amul Chocolate Whey Protein Gift Pack, 34 g | Pack of 10 sachets",
     "alias": "amul-chocolate-whey-protein-gift-pack-34-g-or-pack-of-10-sachets"},
    {"id": "13","name": "Amul Chocolate Whey Protein, 34 g | Pack of 30 sachets",          
     "alias": "amul-chocolate-whey-protein-34-g-or-pack-of-30-sachets"},
    {"id": "14","name": "Amul Chocolate Whey Protein, 34 g | Pack of 60 sachets",          
     "alias": "amul-chocolate-whey-protein-34-g-or-pack-of-60-sachets"},
    {"id": "15","name": "Amul High Protein Plain Lassi, 200 mL | Pack of 30",              
     "alias": "amul-high-protein-plain-lassi-200-ml-or-pack-of-30"},
    {"id": "16","name": "Amul High Protein Buttermilk, 200 mL | Pack of 30",               
     "alias": "amul-high-protein-buttermilk-200-ml-or-pack-of-30"},
    {"id": "17","name": "Amul High Protein Rose Lassi, 200 mL | Pack of 30",                
     "alias": "amul-high-protein-rose-lassi-200-ml-or-pack-of-30"},
    {"id": "18","name": "Amul High Protein Milk, 250 mL | Pack of 8",                      
     "alias": "amul-high-protein-milk-250-ml-or-pack-of-8"},
    {"id": "19","name": "Amul High Protein Milk, 250 mL | Pack of 32",                     
     "alias": "amul-high-protein-milk-250-ml-or-pack-of-32"},
]

ID_TO_NAME  = {p["id"]: p["name"]  for p in PRODUCTS}
ID_TO_ALIAS = {p["id"]: p["alias"] for p in PRODUCTS}

# Mapping from name → ID
NAME_TO_ID = {p["name"]: p["id"] for p in PRODUCTS}

# Utility to get all valid product IDs
VALID_IDS = set(ID_TO_NAME.keys())
