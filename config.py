import os
from dotenv import load_dotenv
import json
load_dotenv(override=True)

COOKIE = os.environ["COOKIE"]
AMUL_API= os.environ["AMUL_API"]
HEADERS=json.loads(os.environ["HEADERS"])

TWITTER_CONSUMER_KEY = os.environ["TWITTER_CONSUMER_KEY"]
TWITTER_CONSUMER_SECRET = os.environ["TWITTER_CONSUMER_SECRET"]
TWITTER_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"]
TWITTER_ACCESS_TOKEN_SECRET = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]
TWILIO_ACCOUNT_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
MY_NUMBER = os.environ["MY_NUMBER"]
TWILIO_WHATSAPP_NUMBER = "whatsapp:+14155238886"
TO_WHATSAPP = f"whatsapp:{MY_NUMBER}" 