import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json
import time
from config import AMUL_API, COOKIE

def get_amul_data_api():
    url = AMUL_API
    response = requests.get(url,timeout=20)
    if response.status_code == 200 and len(response.json().get("data", [])) > 0:
        print("Data fetched successfully!")
        return response.json()
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

def get_amul_data_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(), options=options)
    AMUL_API="https://shop.amul.com/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0&cdc=1m&substore=66505ff0998183e1b1935c75"

    url = AMUL_API
     
    driver.get(url)
    time.sleep(3)
    response_text = driver.find_element("tag name", "pre").text if driver.find_elements("tag name", "pre") else driver.page_source
    
    try:
        data = json.loads(response_text)
        print("Products fetched:", len(data.get("data", [])))
    except Exception as e:
        print("Failed to parse JSON:", e)
        data = None
    driver.quit()
    return data 

