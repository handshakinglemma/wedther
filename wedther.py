# wedther
# Generates tweets for the current weather in Edmonton, AB.
# Tweets the current temperature and an emoji that represents the
# current weather conditions.
# If there is a current weather alert, it also tweets that.

import tweepy
from secret_wedther import *
from get_weather import get_weather

def main():

    # Weather dictionary that assigns an emoji to each condition.
    weather_dict = {'A few clouds':'a few \u2601',
                    'A mix of sun and cloud':'a mix of \u2600 and \u2601',
                    'Chance of flurries':'chance of \u2744',
                    'Chance of showers':'chance of \u2614',
                    'Clear':'clear',
                    'Cloudy':'\u2601',
                    'Mainly cloudy':'mainly \u2601',
                    'Mainly sunny':'mainly \u2600',
                    'Overcast':'\u26C5',
                    'Partly cloudy':'partly \u2601',
                    'Periods of light snow':'periods of light \u2744',
                    'Periods of snow':'periods of \u2744',
                    'Rain':'\u2614',
                    'Snow':'\u2603',
                    'Sunny':'\u2600',
                    'Thunderstorm':'\u26C8'}

    # Twitter stuff.
    auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
    auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Grab the weather information.
    weather = get_weather()
    temperature = str(weather[0])
    picture = str(weather[1])
    weather_picture = weather_dict.get(picture)

    # Make the tweet!
    tweet = 'The weather right now is ' + temperature + ' and ' + weather_picture

    # Get the last tweet from a file.
    filename = 'last_tweet.txt'
    tweet_file = open(filename, 'r+')
    last_tweet = tweet_file.readline().strip()

    # Reword the new tweet if it is a duplicate of the last tweet.
    if last_tweet == tweet:
        tweet = 'The weather remains ' + temperature + ' and ' + weather_picture
    elif 'The weather remains' in last_tweet:
        if last_tweet[20:23] == tweet[20:23]:
            tweet = 'The weather is still ' + temperature + ' and ' + weather_picture
    elif 'The weather is still' in last_tweet:
        if last_tweet[21:24] == tweet[21:24]:
            tweet = 'The weather continues to be ' + temperature + ' and ' + weather_picture

    tweet_file.close()

    # Write the new tweet to the file.
    tweet_file = open(filename, 'w')
    tweet_file.write(tweet)
    tweet_file.close()
    
    # Tweet the tweet!
    api.update_status(tweet)
    
main()
