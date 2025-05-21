from amul_api import get_amul_data_api, get_amul_data_selenium, get_amul_data_urllib
from tweet_utils import generate_amul_tweet, post_tweet, send_twilio_message

if __name__ == "__main__":
    response = get_amul_data_api()
    if response:
        tweet_data = response["data"]

    else:
        print("first api failed")
        print("trying urllib")
        urllib_repsonse = get_amul_data_urllib()
        if len(urllib_repsonse["data"])>0:
            tweet_data = urllib_repsonse["data"]
        else:
            print("urllib failed")
            selenium_data = get_amul_data_selenium()
            if len(selenium_data["data"]) == 0:
                raise Exception("All APIs Failed")
            tweet_data = selenium_data["data"] if selenium_data else []
    
    tweet_text = generate_amul_tweet(tweet_data)
    if tweet_text:
        print(tweet_text)
        # post_tweet(tweet_text)
        # send_twilio_message(tweet_text)  # Uncomment to enable WhatsApp notification
        print("Successfully tweeted!")
    else:
        print("No Changes in availability — skipping tweet") 
