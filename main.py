from config.auth import auth_api
import json
import tweepy

api = auth_api()

perifacode_id = "1111232059387928577"
quebradev_id = "995429424312012801"
tecnogueto_id = "1002022507413757958"


class FavRtAccounts(tweepy.StreamListener):
  def __init__(self, api):
        self.api = api
        self.me = api.me()

  def on_status(self, tweet):
    if tweet.in_reply_to_status_id is not None or \
            tweet.user.id == self.me.id:
            # Ignora caso o tweet seja feito pelo @perifatecnicos
            return
    if not tweet.favorited:
      tweet.favorite()
    if not tweet.retweeted:
      tweet.retweet()



tweets_listener = FavRtAccounts(api)
stream = tweepy.Stream(auth = api.auth, listener=tweets_listener)
stream.filter(follow=[perifacode_id, quebradev_id, tecnogueto_id])