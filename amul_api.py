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
    url = AMUL_API
    
    # # Add cookie manually for authentication
    # cookie_parts = COOKIE.split(';')
    # for part in cookie_parts:
    #     if '=' in part:
    #         name, value = part.strip().split('=', 1)
    #         driver.add_cookie({"name": name, "value": value, "domain": "shop.amul.com"})
    
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