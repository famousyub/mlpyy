








def scrapping25(url):
    import requests
    from urllib.parse import urljoin
    from bs4 import BeautifulSoup
    import time

    res = requests.get(url)
    soup = BeautifulSoup(res.text, "lxml")

    main_content = urljoin(url, soup.select(".load-more-data")[0][
        'data-ajaxurl'])  ##extracting the link leading to the page containing everything available here
    response = requests.get(main_content)
    broth = BeautifulSoup(response.text, "lxml")

    return broth


    # for item in broth.select(".review-container"):
    #     title = item.select(".title")[0].text
    #     review = item.select(".text")[0].text
    #     print("Title: {}\n\nReview: {}\n\n".format(title, review))
    #
    # time.sleep(20)





import sqlite3

from bs4 import BeautifulSoup

connection = sqlite3.connect('SQLITE DB')
crsr = connection.cursor()
#crsr.execute("CREATE TABLE  yub( rating int, review text)")

# !pip install scrapy
# !apt-get update
# !pip install selenium
# !apt install chromium-chromedriver

from scrapy.selector import Selector
import pandas as pd
import sys
# sys.path.insert(0,'/usr/lib/chromium-browser/chromedriver')
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

import  imdb
def get_movie_id(movie_name):
    ia = imdb.IMDb()
    movies = ia.search_movie(movie_name)
    if movies:
        movie = movies[0]
        return movie.movieID
    else:
        return None

film_name = input("Enter film name:  ")

i = get_movie_id(film_name)
if i is None:
    print("Movie not found.")
    exit(1)

i = f"tt{i}"


print (i.strip())
url = f'https://www.imdb.com/title/{i}/reviews/?ref_=tt_ql_2'
url2= "https://www.imdb.com/title/tt0241527/reviews/?ref_=tt_ql_2"
driver.get(url)

sel = Selector(text=driver.page_source)
review_counts = sel.css('.lister .header span::text').extract_first().replace(',', '').split(' ')[0]
more_review_pages = int(int(review_counts) / 25)
r = []
rating_ = []
body = driver.find_element(By.CSS_SELECTOR, 'body')
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)

body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)
body.send_keys(Keys.PAGE_DOWN)



while True:
    old_height = driver.execute_script("return document.body.scrollHeight")
    body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == old_height:
        break



sel = Selector(text=driver.page_source)
review_counts = sel.css('.lister .header span::text').extract_first().replace(',', '').split(' ')[0]
try:
    more_review_pages1 = int(int(review_counts) / 25)
except Exception as e:
    print(str(e))
    exit(1)

for _ in tqdm(range(more_review_pages)):
    try:
        css_selector = 'load-more-trigger'
        driver.find_element(By.ID, css_selector).click()

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
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)



    except:
        pass

rating_list = []
review_date_list = []
review_title_list = []
author_list = []
review_list = []
review_url_list = []
error_url_list = []
error_msg_list = []
reviews = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')
soup = BeautifulSoup(driver.page_source, 'html.parser')
review_elements = soup.find_all('div', class_='text show-more__control')





for i in tqdm(range(more_review_pages)):
    try:


        css_selector = 'load-more-trigger'
        driver.find_element(By.ID, css_selector).click()

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
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
        body.send_keys(Keys.PAGE_DOWN)
    except:
        pass

reviews = driver.find_elements(By.CSS_SELECTOR, 'div.review-container')
first_review = reviews[0]
sel2 = Selector(text=first_review.get_attribute('innerHTML'))


def data_insert():
    crsr.execute("INSERT INTO yourTableName(rating, review) VALUES (?, ?)",
                 (rating, review))


error_url_list = []
error_msg_list = []

for d in tqdm(reviews):
    try:
        sel2 = Selector(text=d.get_attribute('innerHTML'))
        time.sleep(2)

        try :
            more_buttons = driver.find_elements(By.CLASS_NAME, "expander-icon-wrapper.show-more__control")
            more_buttons[0].click()
            time.sleep(2)
        except:
            pass
        try :
            css_ ="expander-icon-wrapper spoiler-warning__control"
            btn = driver.find_element(By.CLASS_NAME, css_)
            btn.click()

            time.sleep(2)
        except:
            btn= np.NaN
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

            try:
                rating = sel2.css('.rating-other-user-rating span::text').extract_first()
            except:
                rating = np.NaN
            try:

                reviews = sel2.css('.text.show-more__control::text').extract_first()



            except:
                reviews = np.NaN
            try:
                review_date = sel2.css('.review-date::text').extract_first()
            except:
                review_date = np.NaN
            try:
                author = sel2.css('.display-name-link a::text').extract_first()
            except:
                author = np.NaN
            try:
                review_title = sel2.css('a.title::text').extract_first()
            except:
                review_title = np.NaN
            try:
                review_url = sel2.css('a.title::attr(href)').extract_first()
            except:
                review_url = np.NaN

            rating_list.append(rating)
            review_date_list.append(review_date)
            review_title_list.append(review_title)
            author_list.append(author)

            review_url_list.append(review_url)






        data_insert()




    except Exception as e:
        error_url_list.append(url)
        error_msg_list.append(e)

review_df = pd.DataFrame({

    'Rating': rating_,

    'Review': r,

})



review_df_ = pd.DataFrame({

    'Rating': rating_,

    'Review': r,

})

review_df_.to_csv(f'{film_name}lm_reviews.csv', index=False)  # Save the CSV with a more descriptive name


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



