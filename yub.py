









import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time
url = 'http://www.imdb.com/title/tt0371746/reviews?ref_=tt_urv'
res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")

main_content = urljoin(url,soup.select(".load-more-data")[0]['data-ajaxurl'])  ##extracting the link leading to the page containing everything available here
response = requests.get(main_content)
broth = BeautifulSoup(response.text,"lxml")

l = len(broth.select(".review-container"))
print(l)
time.sleep(12)

for item in broth.select(".review-container"):
    title = item.select(".title")[0].text
    review = item.select(".text")[0].text
    print("Title: {}\n\nReview: {}\n\n".format(title,review))

time.sleep(20)




from imdb import IMDb
ia = IMDb()
theMatrix = ia.get_movie('0133093')
from bs4 import BeautifulSoup
theMatrix = ia.get_movie('0133093',['reviews'])
print(theMatrix.current_info)
import re
import  requests

print(len(theMatrix['reviews']))

import  time
time.sleep(2)


def Extract_Budget_UserReview( imdbID):


    url = 'http://www.imdb.com/title/{}/?ref_=fn_al_nm_1a'.format(imdbID)
    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')
    Budget = 0
    userReview = ""

    # Extracting the user Review of the movie
    movie = soup.findAll('div', {'class': 'content'})
    for res in movie:
        print (res)
        time.sleep(1)
        userReview = res.text
        if userReview is None:
            userReview = 'N/A'


    return  userReview



h = Extract_Budget_UserReview("tt0133093")






print(len(h))




print (h)

time.sleep(10)
print(theMatrix['reviews'])

import requests

url = "https://online-movie-database.p.rapidapi.com/title/get-user-reviews"

querystring = {"tconst":"tt0133093"}

headers = {
	"X-RapidAPI-Key": "61ac53b62cmsha56e31422b9d820p1737c1jsn2c44d79cfa3b",
	"X-RapidAPI-Host": "online-movie-database.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())