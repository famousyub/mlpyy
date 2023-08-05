from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup

# Set up the Selenium web driver
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=options)

# URL of the IMDb page with reviews
url = "https://www.imdb.com/title/tt0241527/reviews/?ref_=tt_ql_2"

# Open the page with Selenium
driver.get(url)
body = driver.find_element(By.CSS_SELECTOR, 'body')
body.send_keys(Keys.PAGE_DOWN)
time.sleep(1)


# Scroll down to load more reviews
# while True:
#     old_height = driver.execute_script("return document.body.scrollHeight")
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(2)
#     new_height = driver.execute_script("return document.body.scrollHeight")
#     if new_height == old_height:
#         break

# Click on the "Show More" buttons to expand the review content


countermax = 15000
counter  = 0
while True :
    try:
        more_buttons = driver.find_elements(By.CLASS_NAME, "expander-icon-wrapper.show-more__control")
        more_buttons[0].click()
        time.sleep(2)
        body.send_keys(Keys.PAGE_DOWN)
        try:
            css_selector = 'load-more-trigger'
            driver.find_element(By.ID, css_selector).click()
        except:
            pass
    except:
        pass
    if counter == countermax :
        break





# Get the HTML content of the page
html_content = driver.page_source

# Close the web driver
driver.quit()

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Now you can use BeautifulSoup to extract the review content or other information you need from the page.
# For example, to extract review titles and review comments:
reviews = soup.find_all('div', class_='text show-more__control')
for review in reviews:
    review_title = review.find('a', class_='title')
    if review_title is not  None:
        review_title = review_title[0].text.strip()
    else:
        review_title=""
    review_comment = review.find('div', class_='text')
    if review_comment is not None :
        review_comment = review_comment[0].text.strip()
    else :
        review_comment=""

    print("Review Title:", review_title)
    print("Review Comment:", review_comment)
    print()
