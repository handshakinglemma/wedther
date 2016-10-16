# wedther
# Generates tweets for the current weather in Edmonton, AB.
# Tweets the current temperature and an emoji that represents the
# current weather conditions.
# If there is a current weather alert, it also tweets that.

import tweepy
from secret import *
from get_weather import get_weather

def main():

    # Weather dictionary that assigns an emoji to each condition.
    weather_dict = {'Chance of showers':'chance of \u2614', 'Partly cloudy':'\u26C5', 'A mix of sun and clouds':'a mix of \u2600 and \u2601', 'Sunny':'\u2600', 'Rain':'\u2614', 'Snow':'\u2603', 'Thunderstorm':'\u26C8', 'A mix of sun and cloud':'\u26C5', 'Mainly sunny':'mainly \u2600', 'Cloudy':'\u2601', 'Mainly cloudy':'mainly \u2601'}

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

    # Store the tweet in a file.
    tweet_file = open('last_tweet.txt', 'r+')
    last_tweet = tweet_file.readline().strip()

    num_duplicates = 1

    if last_tweet == tweet:
        duplicates = tweet_file.readline().strip()
        num_duplicates = len(duplicates)
        num_duplicates += 1

    if num_duplicates > 1 and num_duplicates % 2 == 0:
        tweet = 'The weather remains ' + temperature + ' and ' + weather_picture
    elif num_duplicates > 1 and num_duplicates % 2 != 0:
        tweet = 'The weather is still ' + temperature + ' and ' + weather_picture

    tweet_file.close()
    tweet_file = open('last_tweet.txt', 'w')
    tweet_file.write(tweet + '\n')
    tweet_file.write('x' * num_duplicates)

    tweet_file.close()
    
    # Tweet the tweet!
    api.update_status(tweet)
    

main()
