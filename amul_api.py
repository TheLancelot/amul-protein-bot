import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
from config import AMUL_API, COOKIE

def get_amul_data_api():
    url = AMUL_API
    response = requests.get(url)
    if response.status_code == 200 and len(response.json().get("data", [])) > 0:
        print("Data fetched successfully!")
        return response.json()
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

def get_amul_data_selenium():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    url = AMUL_API
    driver.get(url)
    time.sleep(3)
    response_text = driver.find_element("tag name", "pre").text if driver.find_elements("tag name", "pre") else driver.page_source
    try:
        data = json.loads(response_text)
        print(url)
        print("Products fetched:", len(data.get("data", [])))
    except Exception as e:
        print("Failed to parse JSON:", e)
        data = None
    driver.quit()
    return data 