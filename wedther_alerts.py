# wedther_alerts
# Checks for weather alerts and tweets them.

from get_weather import get_alerts

def main():

    # Get the current alert message.
    alert = get_alerts()

    # If there is an alert, tweet it.
    # Otherwise, nothing to do.
    if alert != 'No Alerts in effect.':

        # Twitter stuff.
        auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
        auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
        api = tweepy.API(auth)

        # Make the tweet!
        tweet = 'ALERT ' + alert

        # Tweet the tweet!
        api.update_status(tweet)
