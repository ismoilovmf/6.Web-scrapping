import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = 'https://habr.com'
KEYWORDS = ['дизайн', 'фото', 'web', 'python']
lst = []
USER_AGENT = UserAgent().random

resp = requests.get(url+'/ru/all/', headers = {"User-Agent": USER_AGENT})
soup = BeautifulSoup(resp.text, features="html.parser")
posts = soup.find_all("article")

for i, post in enumerate(posts):
    for word in KEYWORDS:
        s = " ".join([hub.text for hub in post.find_all(class_='tm-article-snippet__hubs-item')])
        if word.lower() in s.lower():
            href = post.find('h2').find('a')['href']
            date = post.find("time")["title"]
            title = post.find('h2').find('a').text
            lst.append({title: [date, url+href]})

print(*lst, sep="\n")