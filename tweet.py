import os
import sys

from login import LeetcodeManager

import twitter


def tweet():
  api = twitter.Api(consumer_key=os.environ["CONSUMER_KEY"],
                    consumer_secret=os.environ["CONSUMER_SECRET"],
                    access_token_key=os.environ["ACCESS_TOKEN_KEY"],
                    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
                    )
  api.PostUpdate("テスト456", media="figure.png")
  return
  

if __name__=='__main__':
  lt_test = LeetcodeManager()
  lt_test.get_csrftoken()

  user_name, password = os.environ["USER_NAME"], os.environ["PASSWORD"]
  
  logi = lt_test.login(user_name, password)
  if not logi:
    print("ログインに失敗しています")
    sys.exit()

  if not lt_test.get_info():
    print("データ取得に失敗しました")
    sys.exit()

  if not lt_test.create_chart(["Easy","Medium", "Hard"], [lt_test.data["ac_easy"],lt_test.data["ac_medium"],lt_test.data["ac_hard"]], ['#ff9999','#66b3ff','#99ff99'], "解いた問題数: {}".format(lt_test.data["num_solved"])):
    print("画像生成に失敗しました。")
    sys.exit()
    
  tweet()
  
  