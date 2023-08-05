import sqlite3
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
from tqdm import tqdm
import imdb

def get_movie_id(movie_name):
    ia = imdb.IMDb()
    movies = ia.search_movie(movie_name)
    if movies:
        movie = movies[0]
        return movie.movieID
    else:
        return None

def scrape_imdb_user_reviews(movie_name):
    movie_id = get_movie_id(movie_name)
    if movie_id is None:
        print("Movie not found.")
        return []

    imdb_url = f'https://www.imdb.com/title/tt{movie_id}/reviews/?ref_=tt_ql_2'

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    driver.get(imdb_url)
    time.sleep(2)

    sel = BeautifulSoup(driver.page_source, 'html.parser')
    review_counts = sel.select_one('.lister .header span').text.replace(',', '').split(' ')[0]
    more_review_pages = int(int(review_counts) / 25)

    r = []
    for _ in tqdm(range(more_review_pages)):
        try:
            css_selector = 'load-more-trigger'
            driver.find_element(By.ID, css_selector).click()
        except:
            pass

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    review_elements = soup.find_all('div', class_='text show-more__control')
    reviews = [review_.get_text() for review_ in review_elements]
    reviews_text = " ".join(reviews)

    driver.quit()
    return reviews_text, reviews

if __name__ == "__main__":
    film_name = input("Enter film name: ")
    all_user_reviews, review_list = scrape_imdb_user_reviews(film_name)

    print (len(review_list))

    print("\nAll User Reviews:\n")
    print(all_user_reviews)
