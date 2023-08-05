from bs4 import BeautifulSoup
import requests
import pandas as pd

import variables
from pandas import json_normalize
url = "https://api.scrapingdog.com/scrape?api_key=64c62d43faa0b9190750c755&url=https://www.linkedin.com/in/ayoub-smayen-619425222/&dynamic=false"
r1 = requests.get(f'https://api.scrapingdog.com/linkedin/?api_key=64c62d43faa0b9190750c755&type=company&linkId=google/about/').text

r = requests.get(url).text


soup=BeautifulSoup(r,'html.parser')
u=list()
l={}
try:
 l['Company']=soup.find('h1',{'class':'org-top-card-summary__title t-24 t-black truncate'}).text.replace('\n','')
except:
 l['Company']=None
 allProp = soup.find_all('dd',{'class':'org-page-details__definition-text t-14 t-black — light t-normal'})
try:
 l['website']=allProp[0].text.replace('\n','')
except:
 l['website']=None
try:
 l['Industry']=allProp[1].text.replace('\n','')
except:
 l['Industry']=None
try:
 l['Company Size']=soup.find('dd',{'class':'org-about-company-module__company-size-definition-text t-14 t-black — light mb1 fl'}).text.replace('\n','')
except:
 l['Company Size']=None
try:
 l['Address']=allProp[2].text.replace('\n','')
except:
 l['Address']=None
try:
 l['Type']=allProp[3].text.replace('\n','')
except:
 l['Type']=None
try:
 l['Specialties']=allProp[4].text.replace('\n','')
except:
 l['Specialties']=None
u.append(l)
df = json_normalize(u)
df.to_csv('linkedin.csv', index=False, encoding='utf-8')
print(df)