# Tweepyライブラリをインポート
import tweepy

# 各種キーをセット
CONSUMER_KEY = 'YOURS'
CONSUMER_SECRET = 'YOURS'
ACCESS_TOKEN = 'YOURS'
ACCESS_SECRET = 'YOURS'


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)


#APIインスタンスを作成
api = tweepy.API(auth)

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

#APIインスタンスを作成
api = tweepy.API(auth)
