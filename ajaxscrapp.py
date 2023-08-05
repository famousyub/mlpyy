import requests
from bs4 import BeautifulSoup
import time

def scrape_imdb_reviews(movie_id):
    base_url = f"https://www.imdb.com/title/{movie_id}/reviews/_ajax"

    all_reviews = []

    # Set an initial pagination key as None to start scraping from the first page.
    pagination_key = None

    while True:
        # Add the pagination key to the request parameters to fetch the next page.
        params = {
            "ref_": "undefined",
        }
        if pagination_key:
            params["paginationKey"] = pagination_key

        response = requests.get(base_url, params=params)

        try:
            data = response.json()
        except ValueError as e:
            print(f"Error: Failed to parse JSON data. Response content: {response.content}")
            break

        html_content = data.get('html')

        # If no reviews are found on the current page, we've reached the end.
        if not html_content:
            break

        soup = BeautifulSoup(html_content, 'html.parser')
        reviews = soup.find_all('div', class_='lister-item-content')

        for review in reviews:
            user = review.find('span', class_='display-name-link').text.strip()
            review_title = review.find('a', class_='title').text.strip()
            review_comment = review.find('div', class_='text').text.strip()

            review_data = {
                'user': user,
                'review_title': review_title,
                'review_comment': review_comment,
            }
            all_reviews.append(review_data)

        # Update the pagination key for the next page.
        pagination_key = data.get('paginationKey')

        # Add a delay to avoid overloading the server.
        time.sleep(2)

    return all_reviews

if __name__ == "__main__":
    movie_id = "tt0241527"  # IMDb movie ID of "Harry Potter and the Sorcerer's Stone"

    reviews = scrape_imdb_reviews(movie_id)
    for review in reviews:
        print(f"User: {review['user']}")
        print(f"Review Title: {review['review_title']}")
        print(f"Review Comment: {review['review_comment']}")
        print()
