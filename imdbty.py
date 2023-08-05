import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Set up Selenium WebDriver (using Chrome WebDriver)
# Replace 'path_to_chromedriver' with the actual path to your Chrome WebDriver executable.
driver = webdriver.Chrome()

# Navigate to the IMDb movie page
url = 'https://www.imdb.com/title/tt0241527/reviews/?ref_=tt_ql_2'
driver.get(url)

# Simulate scrolling to load all user reviews
num_scrolls = 10
for _ in range(num_scrolls):
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(2)  # Adjust the sleep time based on the page loading speed

# Get the page source and parse it with BeautifulSoup
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# Extract the user reviews
reviews = soup.find_all('div', class_='review-container')
for review in reviews:
    # Extract the review rating
    rating_span = review.find('span', class_='rating-other-user-rating')
    rating = rating_span.find('span').text.strip() if rating_span else None

    # Extract the review title
    review_title = review.find('a', class_='title').text.strip() if review.find('a', class_='title') else None

    # Extract the reviewer's display name and review date
    display_name = review.find('span', class_='display-name-link').text.strip() if review.find('span', class_='display-name-link') else None
    review_date = review.find('span', class_='review-date').text.strip() if review.find('span', class_='review-date') else None

    # Extract the review content
    review_content = review.find('div', class_='text').text.strip() if review.find('div', class_='text') else None

    print('Rating:', rating)
    print('Review Title:', review_title)
    print('Reviewer:', display_name)
    print('Review Date:', review_date)
    print('Review Content:', review_content)
    print('-' * 50)

# Close the WebDriver when done
driver.quit()
