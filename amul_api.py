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

# def get_amul_data_selenium():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     options.add_argument("window-size=1920,1080")
#     driver = webdriver.Chrome(service=Service(), options=options)
#     url = AMUL_API

#     driver.get(url)
#     time.sleep(3)
#     response_text = driver.find_element("tag name", "pre").text if driver.find_elements("tag name", "pre") else driver.page_source
    
#     try:
#         data = json.loads(response_text)
#         print("Products fetched:", len(data.get("data", [])))
#     except Exception as e:
#         print("Failed to parse JSON:", e)
#         data = None
#     driver.quit()
#     return data 

import os
import time
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_amul_data_selenium():
    AMUL_API = os.environ.get("AMUL_API")
    print("AMUL_API:", AMUL_API)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("window-size=1920,1080")
    options.binary_location = "/usr/bin/google-chrome"

    service = Service("/usr/local/bin/chromedriver")
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get(AMUL_API)

        # Wait for <pre> tag or fallback to delay
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "pre"))
            )
        except:
            time.sleep(3)

        response_text = driver.find_element(By.TAG_NAME, "pre").text if driver.find_elements(By.TAG_NAME, "pre") else driver.page_source

        try:
            data = json.loads(response_text)
            print("Products fetched:", len(data.get("data", [])))
        except Exception as e:
            print("Failed to parse JSON:", e)
            print("Response snippet:", response_text[:500])
            data = None

    finally:
        driver.quit()

    return data
