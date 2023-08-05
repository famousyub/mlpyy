import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import  requests
import parameters

from bs4 import BeautifulSoup


def scrape_company(driver, company_url):
    """Scrape required fields from LinkedIn Company URL"""
    driver.get(company_url + "about/")

    company_name = driver.find_element(By.CSS_SELECTOR, "h1 span").get_attribute("innerText")

    # Get company about container
    about_section = driver.find_element(By.CSS_SELECTOR, "section.org-page-details-module__card-spacing").get_attribute("innerHTML").strip()
    about_section = about_section.replace("\n", "")

    # Remove extra double spaces
    while True:
        if about_section.find("  ") > 0:
            about_section = about_section.replace("  ", " ")
        else:
            break

    # Scrape Website URL
    if about_section.find('Website </dt>') > 0:
        company_website = about_section.split('Website </dt>')[1]
        company_website = company_website.split('</dd>')[0]

        if company_website.find('href="') > 0:
            company_website = company_website.split('href="')[1]
            company_website = company_website.split('"')[0]
        else:
            company_website = ""

    # Scrape Company Industry
    if about_section.find('Industry </dt>') > 0:
        company_industry = about_section.split('Industry </dt>')[1]
        company_industry = company_industry.split('</dd>')[0]
        company_industry = company_industry.split('">')[1].strip()
    else:
        company_industry = ""

    # Scrape Company headquarter
    if about_section.find('Headquarters </dt>') > 0:
        company_headquarter = about_section.split('Headquarters </dt>')[1]
        company_headquarter = company_headquarter.split('</dd>')[0]
        company_headquarter = company_headquarter.split('">')[1].strip()
    else:
        company_headquarter = ""


    # print("Company Name: {}".format(company_name))
    # if company_website  == "":
    #     print("Website: {}".format(company_website))
    # else :
    #     print ("website none")


    print("Industry: {}".format(company_industry))
    print("Headquarter: {}".format(company_headquarter))


def scrape_profile(driver, profile_url):
    """Scrape required fields from LinkedIn company URL"""
    r = requests.get(profile_url).text

    soup = BeautifulSoup(r, 'html.parser')


    time.sleep(2)

    try :

        # Extract company name
        company_name1 = soup.select_one('span.t-14.t-normal').get_text(strip=True)

        # Extract job title
        job_title1 = soup.select_one('div.mr1.t-bold').get_text(strip=True)

        # Extract duration
        duration1 = soup.select_one('span.t-14.t-normal.t-black--light').get_text(strip=True)

        # Extract location
        location1 = soup.select_one('span.t-14.t-normal.t-black--light:nth-of-type(2)').get_text(strip=True)

        # Extract skills
        skills1 = soup.select_one('div.pv-shared-text-with-see-more').get_text(strip=True)

        # Print the extracted information
        print("Company Name:", company_name1)
        print("Job Title:", job_title1)
        print("Duration:", duration1)
        print("Location:", location1)
        print("Skills:", skills1)
    except Exception as ex :
        print(str(ex))


    job_title = soup.find('div', class_='t-bold')
    if job_title is not None :

        job_title = job_title.get_text(strip=True)
    else :
        job_title =""

    company_name = soup.find('span', class_='t-14')
    if company_name is not None:
        company_name = company_name.get_text(strip=True)
    else :
        company_name=""


    #duration = soup.find_all('span', class_='t-14 t-black--light')[1].get_text(strip=True)
    #location = soup.find_all('span', class_='t-14 t-black--light')[2].get_text(strip=True)

    # Extracting skills
    skills_container = soup.find('div', class_='inline-show-more-text')
    if skills_container is not None :
        skills = skills_container.get_text(strip=True).replace('Compétences :', '').strip().split(' · ')
    else :
        skills = []
    print("Job Title:", job_title)
    print("Company Name:", company_name)
    #print("Duration:", duration)
    #print("Location:", location)
    print("Skills:", skills)

    driver.implicitly_wait(10)

    # Find and extract the company name, job title, duration, location, and skills
    #company_name = driver.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal').text

    #duration = driver.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal.t-black--light').text
    #location = driver.find_element(By.CSS_SELECTOR, 'span.t-14.t-normal.t-black--light:nth-of-type(2)').text


    # Print the extracted information
    #print("Company Name:", company_name)

    #print("Duration:", duration)
    #print("Location:", location)

    time.sleep(2)
    driver.get(profile_url)

    profile_name = driver.find_element(By.CSS_SELECTOR, "h1.text-heading-xlarge").get_attribute("innerText")
    profile_title = driver.find_element(By.CSS_SELECTOR, "div.text-body-medium").get_attribute("innerText")
    profile_location = driver.find_element(By.CSS_SELECTOR, "span.text-body-small.inline").get_attribute("innerText")

    # Click on Contact Info link
    driver.find_element(By.ID, "top-card-text-details-contact-info").click()
    time.sleep(1)
    profile_email = driver.find_element(By.CSS_SELECTOR, "a.pv-contact-info__contact-link[href^='mailto:']").get_attribute("innerText")

    print("Profile Name: {}".format(profile_name))
    print("Title: {}".format(profile_title))
    print("Location: {}".format(profile_location))
    print("Email: {}".format(profile_email))


def scrape_jobs(driver, jobs_url):
    """Scrape required fields from LinkedIn job page"""
    driver.get(jobs_url)

    for job in driver.find_elements(By.CSS_SELECTOR, "ul#jobs-home-vertical-list__entity-list li"):
        try:
            job_title = job.find_element(By.CSS_SELECTOR, "a.job-card-list__title").get_attribute("innerText")
            company_name = job.find_element(By.CSS_SELECTOR, "span.job-card-container__primary-description").get_attribute("innerText")
            company_location = job.find_element(By.CSS_SELECTOR, "li.job-card-container__metadata-item").get_attribute("innerText")
        except:
            continue

        print("Job title: {}".format(job_title))
        print("Company name: {}".format(company_name))
        print("Company location: {}".format(company_location))


if __name__ == "__main__":
    driver = webdriver.Chrome()

    driver.implicitly_wait(10)

    driver.get('https://www.linkedin.com/login')

    # Log in LinkedIn
    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys(parameters.username)

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys(parameters.password)

    sign_in_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    sign_in_btn.click()
    test_url = "https://www.linkedin.com/in/mootez-meddeb-b35535107/"
    ui = "https://www.linkedin.com/in/ayoub-smayen-619425222/"
    scrape_profile(driver, ui)
    scrape_company(driver, "https://www.linkedin.com/company/microsoft/")
    scrape_jobs(driver, "https://www.linkedin.com/jobs/")

    driver.close()
    driver.quit()