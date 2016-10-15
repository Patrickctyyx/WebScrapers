# 使用API一般要申请账号，然后用特定的API key
# 而且有一些有访问限制(一分钟不能多于XX次)
# 1.Echo Nest API
# 注册api key的界面503了...

# 2.twitter
# 然而请求超时？是网速的问题还是梯子的问题？
from twitter import *
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))
pythonTweets = t.search.tweets(q='#python')
print(pythonTweets)

