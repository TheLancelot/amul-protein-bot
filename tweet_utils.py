import json
from config import (
    TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET,
    TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TO_WHATSAPP, TWILIO_WHATSAPP_NUMBER
)
from requests_oauthlib import OAuth1
import requests
from twilio.rest import Client

SHORT_NAME_MAP = {
    # Kool Protein Milkshakes
    "Amul Kool Protein Milkshake | Chocolate, 180 mL | Pack of 30": "Kool Choco 180×30",
    "Amul Kool Protein Milkshake | Kesar, 180 mL | Pack of 8":    "Kool Kesar 180×8",
    "Amul Kool Protein Milkshake | Kesar, 180 mL | Pack of 30":   "Kool Kesar 180×30",
    "Amul Kool Protein Milkshake | Vanilla, 180 mL | Pack of 8":    "Kool Vanilla 180×8",
    "Amul Kool Protein Milkshake | Vanilla, 180 mL | Pack of 30":   "Kool Vanilla 180×30",
    "Amul Kool Protein Milkshake | Arabica Coffee, 180 mL | Pack of 8":  "Kool Coffee 180×8",
    "Amul Kool Protein Milkshake | Arabica Coffee, 180 mL | Pack of 30": "Kool Coffee 180×30",
    # High-Protein Shakes & Drinks
    "Amul High Protein Blueberry Shake, 200 mL | Pack of 30": "Blueberry Shake 200×30",
    "Amul High Protein Plain Lassi, 200 mL | Pack of 30":    "Plain Lassi 200×30",
    "Amul High Protein Rose Lassi, 200 mL | Pack of 30":     "Rose Lassi 200×30",
    "Amul High Protein Buttermilk, 200 mL | Pack of 30":     "Buttermilk 200×30",
    "Amul High Protein Milk, 250 mL | Pack of 8":            "HP Milk 250×8",
    "Amul High Protein Milk, 250 mL | Pack of 32":           "HP Milk 250×32",
    # Paneer
    "Amul High Protein Paneer, 400 g | Pack of 2":  "Paneer 400g×2",
    "Amul High Protein Paneer, 400 g | Pack of 24": "Paneer 400g×24",
    # Whey Protein
    "Amul Whey Protein, 32 g | Pack of 30 Sachets":            "Whey 32g×30",
    "Amul Whey Protein, 32 g | Pack of 60 Sachets":            "Whey 32g×60",
    "Amul Whey Protein Gift Pack, 32 g | Pack of 10 sachets":  "Whey Gift 32g×10",
    "Amul Chocolate Whey Protein, 34 g | Pack of 30 sachets":  "Choco Whey 34g×30",
    "Amul Chocolate Whey Protein, 34 g | Pack of 60 sachets":  "Choco Whey 34g×60",
    "Amul Chocolate Whey Protein Gift Pack, 34 g | Pack of 10 sachets": "Choco Gift 34g×10",
}

def has_changes(prev_data: list, curr_data: list) -> bool:
    prev_map = {item['name']: item.get('available', 0) for item in prev_data}
    curr_map = {item['name']: item.get('available', 0) for item in curr_data}
    all_product_names = set(prev_map.keys()) | set(curr_map.keys())
    for name in all_product_names:
        prev_avail = prev_map.get(name, 0)
        curr_avail = curr_map.get(name, 0)
        if prev_avail != curr_avail:
            return True
    return False

# def generate_amul_tweet(current_data, previous_data_path="amul_prev_state.json", low_stock_threshold=10, short_map=SHORT_NAME_MAP):
#     try:
#         with open(previous_data_path, "r") as f:
#             prev = json.load(f)
#             prev_avail = {itm["name"]: itm["available"] for itm in prev}
#     except FileNotFoundError:
#         prev_avail = {}
#     new_items = []
#     normal_items = []
#     low_items = []
#     for itm in current_data:
#         if int(itm["available"]) != 1:
#             continue
#         name = itm["name"]
#         qty  = itm["inventory_quantity"]
#         disp = short_map.get(name, name)
#         was_avail = prev_avail.get(name, 0) == 1
#         if not was_avail:
#             new_items.append(disp)
#         elif qty <= low_stock_threshold:
#             low_items.append(disp)
#         else:
#             normal_items.append(disp)
#     if not has_changes(prev, current_data):
#         print("No changes- not updating json")
#         return
#     print("Saving new availability data")
#     with open(previous_data_path, "w") as f:
#         json.dump(current_data, f)
#     lines = ["Amul Protein Stock Update 🐄\n","✅ Available:"]
#     for d in new_items:
#         lines.append(f"{d}🆕")
#     for d in normal_items:
#         lines.append(f"{d}")
#     for d in low_items:
#         lines.append(f"{d}⚠️")
#     tweet = "\n".join(lines)
#     if len(tweet) > 275:
#         tweet = tweet[:270] + "tbc"
#     return tweet

def generate_amul_tweet(current_data,previous_data_path="amul_prev_state.json",low_stock_threshold=10,short_map=SHORT_NAME_MAP):
    """
    Compares current data with previous availability, generates a tweet if new products are available.
    
    Returns:
        tweet_text (str | None),
        newly_available_names (list of full product names),
        current_data (to save if needed)
    """
    # Load previous availability
    try:
        with open(previous_data_path, "r") as f:
            prev = json.load(f)
            prev_avail = {itm["name"]: itm["available"] for itm in prev}
    except FileNotFoundError:
        prev_avail = {}

    new_items = []
    new_names_raw = []  # full product names for backend ID mapping
    normal_items = []
    low_items = []

    for itm in current_data:
        if int(itm["available"]) != 1:
            continue

        name = itm["name"]
        qty = itm.get("inventory_quantity", 0)
        disp = short_map.get(name, name)
        was_avail = prev_avail.get(name, 0) == 1

        if not was_avail:
            new_names_raw.append(name)
            new_items.append(disp)
        elif qty <= low_stock_threshold:
            low_items.append(disp)
        else:
            normal_items.append(disp)

    # No changes = no tweet = no notification
    if not has_changes(prev, current_data):
        # print("No changes—skipping update & tweet")
        return None, [], current_data

    # Save current state to JSON
    print("Saving new availability data")
    with open(previous_data_path, "w") as f:
        json.dump(current_data, f)

    # Build tweet
    lines = ["Amul Protein Stock Update 🐄", "✅ Available:"]
    for d in new_items:
        lines.append(f"{d}🆕")
    for d in normal_items:
        lines.append(d)
    for d in low_items:
        lines.append(f"{d}⚠️")

    tweet = "\n".join(lines)
    if len(tweet) > 275:
        tweet = tweet[:270] + "tbc"

    return tweet, new_names_raw, current_data

def post_tweet(tweet_text):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET, TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    payload = {"text": tweet_text}
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, json=payload, auth=auth, headers=headers)
    if response.status_code == 201:
        print("Tweet posted successfully!")
        print("Response:", response.json())
    else:
        print(f"Failed to post tweet. Status code: {response.status_code}")
        print("Response:", response.text)

#telegram
import requests
def post_to_channel(bot_token, channel_username, text):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": f"@{channel_username}", "text": text, "parse_mode": "HTML"}
    resp = requests.post(url, json=payload)
    return resp.ok

def send_twilio_message(body, to=TO_WHATSAPP, from_=TWILIO_WHATSAPP_NUMBER):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        body=body,
        from_=from_,
        to=to
    )
    print(f"Message sent to {to}: SID = {message.sid}") 
