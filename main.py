from amul_api import get_amul_data_api, get_amul_data_selenium
from tweet_utils import generate_amul_tweet, post_tweet, send_twilio_message

if __name__ == "__main__":
    response = get_amul_data_api()
    if response:
        tweet_data = response["data"]
    else:
        selenium_data = get_amul_data_selenium()
        tweet_data = selenium_data["data"] if selenium_data else []
    tweet_text = generate_amul_tweet(tweet_data)
    if tweet_text:
        print(tweet_text)
        post_tweet(tweet_text)
        # send_twilio_message(tweet_text)  # Uncomment to enable WhatsApp notification
        print("Successfully tweeted!")
    else:
        print("No Changes in availability — skipping tweet") 
