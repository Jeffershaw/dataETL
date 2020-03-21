import requests
from io import StringIO
import json
import pandas as pd
import time
from pandas.io.json import json_normalize


def getNewsKeyword(keyword):
  url = ('http://newsapi.org/v2/top-headlines?'
       'q=%s&'
       'apiKey=7417491a101e4ec3a8219b263f028ff7'%keyword)
  
  response = requests.get(url)  
  json_data = json.loads(response.text)['articles']  
  data = json_normalize(json_data, max_level=2)
  return data


def getGoogleTrends(keyword):
    google_explore_api_url = 'https://trends.google.com/trends/api/explore'
    google_explore_url = 'https://trends.google.com/trends/explore'
    sess_headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
    sess = requests.Session()
    params = {
        'q': keyword,
        'geo': 'US'
    }
    sess.get(google_explore_url,params=params,headers=sess_headers)
    params = {
        'hl': 'en-US',
        'tz': '-60',
        'req': '{"comparisonItem":[{"keyword":"%s","geo":"US","time":"today 12-m"}],"category":0,"property":""}'%keyword,
        'tz': '-60',
    }
    r = sess.get(google_explore_api_url,params=params,headers=sess_headers)
    token = json.loads(r.text.split(')]}\'\n')[-1])['widgets'][0]['token']
    print(token)

    # passed one year
    s2=time.strftime('%Y-%m-%d')
    # print(s2)
    year_bit = int(s2[:4])
    s1 = str(year_bit-1)+s2[4:]
    # print(s1)

    google_explore_csv_url = 'https://trends.google.com/trends/api/widgetdata/multiline/csv'
    params = {
        'req': '{"time":"%s %s","resolution":"WEEK","locale":"en-US","comparisonItem":[{"geo":{"country":"US"},"complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":"%s"}]}}],"requestOptions":{"property":"","backend":"IZG","category":0}}'%(s1,s2,keyword),
        'token':token,
        'tz': -60
    }
    r = sess.get(google_explore_csv_url,params=params,headers=sess_headers)

    data = StringIO(r.text)
    df = pd.read_csv(data)
    return df

