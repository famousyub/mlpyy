import csv
import time
import random
import sys
import os

# selenium package
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException

import parameters

# identifiants
email_address = parameters.username
password = parameters.password
search_item = "Chief Happiness Officer"

# fonction pause
def pause():
    time_break = random.randint(3,5)
    # print "Pause de " + str(time_break) + " seconde(s)."
    return time.sleep(2)

# options
options = webdriver.ChromeOptions()
options.add_argument("--kiosk")

capa = DesiredCapabilities.CHROME
capa["pageLoadStrategy"] = "none"
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 30)
pause()


# url de depart
linkedin_url = "https://www.linkedin.com/"

# aller sur linkedin
driver.get(linkedin_url) #1 : page principale
try:
    wait.until(EC.presence_of_element_located(
                    (By.ID, "login-submit"))
                )
except (TimeoutException):
    sys.exit("Error message - loading page")
pause()


# s'identifier
driver.find_element_by_id("login-email").send_keys(email_address)
pause()
driver.find_element_by_id("login-password").send_keys(password)
pause()
driver.find_element_by_id("login-submit").click()
pause()
wait.until(EC.element_to_be_clickable(
    (By.ID, "nav-typeahead-wormhole"))
)
pause()
print ("Profil connecte a Linkedin - 1")

# lancer la recherche
driver.find_element_by_css_selector("div.nav-search-typeahead input").send_keys(search_item)
pause()
driver.find_element_by_css_selector("div.nav-search-typeahead input").send_keys(Keys.ENTER)
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "span.name.actor-name"))
)
wait.until(EC.presence_of_element_located(
    (By.CSS_SELECTOR, "h3.search-results__total")
))
pause()
print ("Fin de la recherche avec mot cle : " + search_item)

# scroll down smoothly
scheight = .1
while scheight < 1.0:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight*%s);" % scheight)
    scheight += .1
    pause()
wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, 'div.next-text')
))
try:
    print (driver.find_element_by_css_selector('div.next-text').text)
except(NoSuchElementException):
    print ('No div.next-text')
finally:
    pass

# ouvrir csv
with open('linkedin_items.csv', 'w') as csvfile:
    cwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='$', quoting=csv.QUOTE_MINIMAL)

    # prendre infos
    profils = driver.find_elements_by_css_selector("div.search-result__wrapper")

    # boucle
    for profil in profils:

        # creer tableau
        csv_row = []

        # name
        try:
            name_location = profil.find_element_by_css_selector(
                "span.name.actor-name")
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'});",
                name_location)
            name = name_location.text.encode('utf-8')
            csv_row.append(name)
        except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
            name = ''
            csv_row.append(name)
        finally:
            pass

        if name != '':

            # url
            try:
                url_profil = profil.find_element_by_css_selector("a.search-result__result-link").get_attribute('href')
                csv_row.append(url_profil)
            except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                url_profil = 'None'
                csv_row.append(url_profil)
            finally:
                pass

            # position
            try:
                position = profil.find_element_by_css_selector("p.subline-level-1").text.encode('utf-8')
                csv_row.append(position)
            except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                position = 'None'
                csv_row.append(position)
            finally:
                    pass

            # localisation
            try:
                localisation = profil.find_element_by_css_selector("p.subline-level-2").text.encode('utf-8')
                csv_row.append(localisation)
            except (NoSuchElementException, WebDriverException, StaleElementReferenceException):
                localisation = 'None'
                csv_row.append(localisation)
            finally:
                pass

        else:
            url_profil = ''
            csv_row.append(url_profil)
            position = ''
            csv_row.append(position)
            localisation = ''
            csv_row.append(localisation)

        # copier dans le csv
        try:
            cwriter.writerow(csv_row)
            print("-- SUCCESS : %s" % name)
        except(NoSuchElementException, WebDriverException, StaleElementReferenceException, UnicodeEncodeError):
            print("Error message - csv")
        finally:
            pass

# fermer les navigateurs
print("Bravo !")
driver.close()