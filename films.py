# -*- coding: utf-8 -*-




import sqlite3
connection = sqlite3.connect('SQLITE DB')
crsr = connection.cursor()
#crsr.execute("CREATE TABLE  yourTableName( rating int, review text)")

#!pip install scrapy
#!apt-get update
#!pip install selenium
#!apt install chromium-chromedriver

from scrapy.selector import Selector
import pandas as pd
import sys
#sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
from selenium import webdriver
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm

url = 'https://www.imdb.com/title/tt0120338/reviews/?ref_=tt_ql_2'
driver.get(url)

sel = Selector(text = driver.page_source)
review_counts = sel.css('.lister .header span::text').extract_first().replace(',','').split(' ')[0]
more_review_pages = int(int(review_counts)/25)
r= []
rating_ = []
body = driver.find_element(By.CSS_SELECTOR, 'body')

body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)



for i in tqdm(range(more_review_pages)):
    try:


        css_selector = 'load-more-trigger'
        driver.find_element(By.ID, css_selector).click()
    except:
        pass

reviews = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')
first_review = reviews[0]
sel2 = Selector(text = first_review.get_attribute('innerHTML'))






def data_insert():
  crsr.execute("INSERT INTO yourTableName(rating, review) VALUES (?, ?)",
               (rating,review))


error_url_list = []
error_msg_list = []

for d in tqdm(reviews):
    try:
        sel2 = Selector(text = d.get_attribute('innerHTML'))
        try:
            rating = sel2.css('.rating-other-user-rating span::text').extract_first()
            rating_.append(rating)
        except:
            rating = np.NaN
        try:
            review = sel2.css('.text.show-more__control::text').extract_first()
            r.append(review)
        except:
            review = np.NaN


        data_insert()




    except Exception as e:
        error_url_list.append(url)
        error_msg_list.append(e)

review_df = pd.DataFrame({

    'Rating': rating_,

    'Review': r,

})

review_df.to_csv(f'potter_reviews.csv', index=False)

res = crsr.execute("SELECT* FROM yourTableName")

res.fetchall()

connection.commit()

res = crsr.execute("SELECT* FROM yourTableName")

print(res.fetchall())

j = res.fetchall()
print(type(j))

r = len(j)



for o in j :
    print (o)
connection.commit()