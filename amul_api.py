import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import json
import time
from config import AMUL_API, COOKIE
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import requests
def get_amul_data_api():
    aurl="https://shop.amul.com/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0"
    headers = {
    "authority": "shop.amul.com",
    "method": "GET",
    "path": "/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0",
    "scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "_fbp=fb.1.1745925439066.409308632149880130; _ga_XXXXXXXXXX=GS1.1.1746017298.2.1.1746017322.0.0.0; _ga_1DPYKST0SD=GS2.2.s1746711856$o2$g1$t1746711858$j0$l0$h0; _ga=GA1.1.711881172.1745925435; jsessionid=s%3A%2FYTblr9GJpHoi7gD1bm8WyWs.rTIpD3dGSg9WuxLMvP7m%2BTU2BC4awBLSZOqVB8IXTa4; _ga_E69VZ8HPCN=GS2.1.s1755021670$o52$g1$t1755022646$j60$l0$h490980856",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}

    # response = requests.get(url,params=params,headers=headers,timeout=20)
    response= requests.get(aurl,headers=headers,timeout=20)
    if response.status_code == 200 and len(response.json()["data"])>0:
        print("Data fetched successfully!")
        print(response.json())
        return response.json()
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

def get_amul_data_selenium():
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
#
    options.add_argument("--headless")  # Use stable headless mode
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--remote-allow-origins=*")

    driver = webdriver.Chrome(service=Service(), options=options)
    AMUL_API="https://shop.amul.com/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0"

    url = AMUL_API

    # base_url="https://shop.amul.com/en/browse/protein"
    # driver.get(base_url)
    # time.sleep(3)
    # print(driver.page_source)

    driver.get(url)
    time.sleep(3)
    # print(driver.page_source)
    try:
        pre_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "pre"))
        )
        response_text = pre_element.text
    except:
        response_text = driver.page_source
    # response_text = driver.find_element("tag name", "pre").text if driver.find_elements("tag name", "pre") else driver.page_source
    
    try:
        print(response_text)
        data = json.loads(response_text)
        print("Products fetched:", len(data.get("data", [])))
    except Exception as e:
        print("Failed to parse JSON:", e)
        data = None
    driver.quit()
    return data 

import urllib.request

def get_amul_data_urllib():

    url="https://shop.amul.com/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0"

    headers = {
    "authority": "shop.amul.com",
    "method": "GET",
    "path": "/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0",
    "scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "_fbp=fb.1.1745925439066.409308632149880130; _ga_XXXXXXXXXX=GS1.1.1746017298.2.1.1746017322.0.0.0; _ga_1DPYKST0SD=GS2.2.s1746711856$o2$g1$t1746711858$j0$l0$h0; _ga=GA1.1.711881172.1745925435; jsessionid=s%3A%2FYTblr9GJpHoi7gD1bm8WyWs.rTIpD3dGSg9WuxLMvP7m%2BTU2BC4awBLSZOqVB8IXTa4; _ga_E69VZ8HPCN=GS2.1.s1755021670$o52$g1$t1755022646$j60$l0$h490980856",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print("Products fetched:", len(data.get("data", [])))
            return data
    except Exception as e:
        print("Failed to fetch or parse data:", e)
        return None
    

import httpx

def get_amul_data_httpx():
    url="https://shop.amul.com/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0"
    headers = {
    "authority": "shop.amul.com",
    "method": "GET",
    "path": "/api/1/entity/ms.products?fields[name]=1&fields[brand]=1&fields[categories]=1&fields[collections]=1&fields[alias]=1&fields[sku]=1&fields[price]=1&fields[compare_price]=1&fields[original_price]=1&fields[images]=1&fields[metafields]=1&fields[discounts]=1&fields[catalog_only]=1&fields[is_catalog]=1&fields[seller]=1&fields[available]=1&fields[inventory_quantity]=1&fields[net_quantity]=1&fields[num_reviews]=1&fields[avg_rating]=1&fields[inventory_low_stock_quantity]=1&fields[inventory_allow_out_of_stock]=1&fields[default_variant]=1&fields[variants]=1&fields[lp_seller_ids]=1&filters[0][field]=categories&filters[0][value][0]=protein&filters[0][operator]=in&filters[0][original]=1&facets=true&facetgroup=default_category_facet&limit=24&total=1&start=0",
    "scheme": "https",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9",
    "Cookie": "_fbp=fb.1.1745925439066.409308632149880130; _ga_XXXXXXXXXX=GS1.1.1746017298.2.1.1746017322.0.0.0; _ga_1DPYKST0SD=GS2.2.s1746711856$o2$g1$t1746711858$j0$l0$h0; _ga=GA1.1.711881172.1745925435; jsessionid=s%3A%2FYTblr9GJpHoi7gD1bm8WyWs.rTIpD3dGSg9WuxLMvP7m%2BTU2BC4awBLSZOqVB8IXTa4; _ga_E69VZ8HPCN=GS2.1.s1755021670$o52$g1$t1755022646$j60$l0$h490980856",
    "Priority": "u=0, i",
    "Sec-Ch-Ua": '"Not)A;Brand";v="8", "Chromium";v="138", "Google Chrome";v="138"',
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
    try:
        with httpx.Client(timeout=10) as client:
            response = client.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            print("Products fetched:", len(data.get("data", [])))
            return data
    except Exception as e:
        print("httpx request failed:", e)
        return None
