import oauth
api = oath.api

q = "python"
count = 50

# //検索実行
search_results = api.search(q=q, count=count)

# //結果を順番にフォロー
for result in search_results:
    screen_id = result.user._json['screen_name']
    print(screen_id)
    api.create_friendship(screen_id)
