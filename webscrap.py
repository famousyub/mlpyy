from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import numpy as np
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Set up the webdriver, this assumes you have the chromedriver installed and in your path
driver = webdriver.Chrome()
import time 
# Get the webpage
driver.get("https://www.imdb.com/title/tt0111161/reviews") # replace this with your URL

# Ensure that the page is loaded
element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "main"))
)

html = driver.page_source

# Pass the page source to BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')


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

# Find all the reviews on the page
review_divs = soup.find_all('div', class_='imdb-user-review')



print(len(review_divs))

for review_div in review_divs:
    # Extract the username
    username_div = review_div.find('span', class_='display-name-link')
    username = username_div.get_text(strip=True)

    # Extract the review content
    review_content_div = review_div.find('div', class_='text')
    review_content = review_content_div.get_text(strip=True)

    print(f'{username}: {review_content}\n')



driver.quit()
