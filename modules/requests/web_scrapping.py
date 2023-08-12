# Web Scrapping: consist of search and getting data along the internet
# bs4.BeautifulSoup: reads html data to Python objects to ease devs' life
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
import requests
from bs4 import BeautifulSoup

url = 'http://127.0.0.1:3333'
response = requests.get(url)

raw_html = response.content

parsed_html = BeautifulSoup(raw_html, 'html.parser', from_encoding='utf-8')
print(parsed_html.title.text, end='\n\n')  # type: ignore

# selecting a unique html element
top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')
print(top_jobs_heading.text, end='\n\n')  # type: ignore

# selecting html element's parent
article = top_jobs_heading.parent  # type: ignore
print(article, end='\n\n')

# selecting article paragraphs
for p in article.select('p'):  # type: ignore
    print(p.text)
