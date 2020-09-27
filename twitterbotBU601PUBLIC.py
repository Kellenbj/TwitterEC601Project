import tweepy
import json
import urllib3
import requests


CONSUMER_KEY = # put yours in
CONSUMER_SECRET = # put yours in
ACCESS_KEY = # put yours in 
ACCESS_SECRET = # put yours in

def weathertweets():
    weatherrequest = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Seattle{OPEN WEATHER AUTH HERE}')
    tweetdata = weatherrequest.json()
    return tweetdata

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

j = weathertweets()
#j = json.loads(dailyweather)
Ftemp = int(j['main']['temp'])*(9/5)-460
weatherlist = str(['Weather provided by OpenWeather for', j['name'],'-',j['weather'][0]['description'], 'Temperature: ',Ftemp,'F'])
send = "".join(weatherlist)

api.update_status(send)
