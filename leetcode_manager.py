import requests
from requests_toolbelt import MultipartEncoder
import sys
import os
import json
import matplotlib
from matplotlib import rcParams
matplotlib.use('Agg') # -----(1)
import matplotlib.pyplot as plt

import datetime

user_agent = r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36'
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Hiragino Maru Gothic Pro', 'Yu Gothic', 'Meirio', 'Takao', 'IPAexGothic', 'IPAPGothic', 'VL PGothic', 'Noto Sans CJK JP']

class LeetcodeManager():
    def __init__(self):
        self.session = requests.Session()      
        self.csrftoken = ''
        self.is_login = False
        self.data = {}
    
    def get_csrftoken(self):
        url = 'https://leetcode.com'
        cookies = self.session.get(url).cookies
        for cookie in cookies:
            if cookie.name == 'csrftoken':
                self.csrftoken = cookie.value
                break

    def login(self, username, password):
        url = "https://leetcode.com/accounts/login"
        
        params_data = {
            'csrfmiddlewaretoken': self.csrftoken,
            'login': username,
            'password':password,
            'next': 'problems'
        }
        headers = {'User-Agent': user_agent, 'Connection': 'keep-alive', 'Referer': 'https://leetcode.com/accounts/login/',
        "origin": "https://leetcode.com"}
        m = MultipartEncoder(params_data)   

        headers['Content-Type'] = m.content_type
        self.session.post(url, headers = headers, data = m, timeout = 10, allow_redirects = False)
        self.is_login = self.session.cookies.get('LEETCODE_SESSION') != None
        return self.is_login

    def get_info(self):
      url = "https://leetcode.com/api/problems/all/"

      headers = {'User-Agent': user_agent, 'Connection': 'keep-alive'}
      resp = self.session.get(url, headers = headers, timeout = 10)
       
      question_list = json.loads(resp.content.decode('utf-8'))

      for col in ("num_solved", "ac_easy","ac_medium", "ac_hard"):
        self.data[col] = question_list[col]

      if self.data["num_solved"]:
        return True
      return False
    
    def create_chart(self, labels, sizes, colors, title):
      try:
        #explsion
        explode = (0.05,0.05,0.05)

        fig1, ax1 = plt.subplots()
        
        plt.pie(sizes, colors = colors, labels=labels, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode = explode)
        #draw circle
        centre_circle = plt.Circle((0,0),0.70,fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)
        # Equal aspect ratio ensures that pie is drawn as a circle
        ax1.axis('equal')  
        kwargs = dict(size=16, fontweight='bold', va='center')
        ax1.text(0, 0, title,  ha='center', **kwargs)
        ax1.set_title("{}の進捗".format(datetime.datetime.today().strftime("%Y/%m/%d")), y=1.04)
        # plt.tight_layout()
        plt.savefig('figure.png')
        return True
      except:
        return False