from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time


import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from tqdm import tqdm
def get_all_user_reviews(movie_url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
    driver = webdriver.Chrome()

    # Load the IMDb movie page
    driver.get(movie_url)
    time.sleep(2)  # Allow time for the page to load

    # Click on "User Reviews" to access all reviews
    try:
        user_review_link = driver.find_element(By.XPATH,"//a[@href='#titleUserReviews']")
        user_review_link.click()
        time.sleep(2)  # Allow time for the user reviews to load
    except Exception as e:
        print(f"Error: {e}")

    # Extract all user reviews
    user_reviews = []
    while True:
        try:
            show_more_button = driver.find_element(By.XPATH, "//button[@class='ipl-load-more__button']")
            show_more_button.click()
            time.sleep(2)  # Allow time for more reviews to load
        except Exception:
            break

    # Parse the HTML and extract the review text
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    reviews = soup.find_all("span", class_="text show-more__control")
    for review in reviews:
        user_reviews.append(review.text.strip())

    driver.quit()
    return user_reviews

if __name__ == "__main__":
    # Replace 'MOVIE_URL' with the IMDb URL of the movie you want to scrape
    movie_url = 'https://www.imdb.com/title/tt0241527/reviews/?ref_=tt_ql_2'
    all_user_reviews = get_all_user_reviews(movie_url)

    for idx, review in enumerate(all_user_reviews, 1):
        print(f"Review {idx}: {review}\n")
