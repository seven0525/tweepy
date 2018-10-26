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


q = "Pygame"
count = 100
search_results = api.search(q=q, count=count)

for result in search_results:
    username = result.user._json['screen_name']
    user_id = result.id #ツイートのstatusオブジェクトから、ツイートidを取得
    print(user_id)
    user = result.user.name #ツイートのstatusオブジェクトから、userオブジェクトを取り出し、名前を取得する
    print(user)
    tweet = result.text
    print(tweet)
    time = result.created_at
    print(time)
    try:
        api.create_favorite(user_id) #favする
        print(user)
        print("にfavしました")
    except:
        print("既にfavしてます！")
    print("##################")
