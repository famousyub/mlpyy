from ons import IMDBReviewsScraper

scraper = IMDBReviewsScraper()
scraper.scrape('harry potter', num_scrolls=1, sleep=10)