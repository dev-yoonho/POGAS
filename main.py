import json
import os
import sys
import time
import dotenv
import urllib.request
from playwright.sync_api import sync_playwright

from find_opinion import find_opinion
from random_sleep import sleep_poisson

dotenv.load_dotenv()

if __name__ == "__main__":
    
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")
    encText = urllib.parse.quote("강북삼성 진료")
    url = "https://openapi.naver.com/v1/search/cafearticle?query=" + encText + "&display=10&sort=sim&start=1" # JSON 결과
    # url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()
    if(rescode==200):
        data = json.loads(response.read().decode('utf-8'))
        for item in data['items']:
            raw_title = item.get('title').replace('<b>', '').replace('</b>', '').replace('&quot;', '')
            exc_words = ["모집", "채용", "공고", "공지", "합격", "조리원"]
            if any(word in raw_title for word in exc_words):
                continue
            time.sleep(sleep_poisson())
            with sync_playwright() as p:
                content, comments = find_opinion(p, title=raw_title)
                print(content)
                print(comments)
    else:
        print("Error Code:" + rescode)