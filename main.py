from amul_api import get_amul_data_api, get_amul_data_selenium, get_amul_data_urllib,get_amul_data_httpx
from tweet_utils import generate_amul_tweet, post_tweet, send_twilio_message,post_to_channel
from notify import names_to_ids, dispatch_notifications

if __name__ == "__main__":
    response = get_amul_data_api()
    if response:
        tweet_data = response["data"]

    else:
        print("first api failed")
        print("trying urllib")
        response= get_amul_data_urllib()
        if len(response["data"])>0:
            tweet_data = response["data"]
        else:
            print("urllib failed")

            response= get_amul_data_httpx()
            if len(response["data"])>0:
                tweet_data = response["data"]
            else:
                print("httpx failed")
                response = get_amul_data_selenium()
                if len(response["data"]) == 0:
                    raise Exception("All APIs Failed")
                tweet_data = response["data"] if response else []
    
    tweet_text, new_names, _ = generate_amul_tweet(tweet_data)

    print(f"New item names: {new_names}")
    if tweet_text:
        print(tweet_text)

        post_tweet(tweet_text)
        # send_twilio_message(tweet_text)  # Uncomment to enable WhatsApp notification
        print("Successfully tweeted!")

        #telegram channel
        import os
        post_to_channel(os.environ["bot_token"],os.environ["channel_username"],tweet_text)
        print("Successfully telegramed")
        # Send subscriber notifications
        new_ids = names_to_ids(new_names)
        if new_ids:
            dispatch_notifications(new_ids)
        else:
            print("No subscriber notifications to send.")
    else:
        print("No changes in availability — skipping tweet & notifications")

    


