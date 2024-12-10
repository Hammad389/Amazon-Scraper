from utils.input_handler import load_queries
from utils.scraper import AmazonScraper


def main():
    # FUNCTION TO CALL THE LOAD_QUERIES() (THIS WILL LOAD THE INPUT QUERIES FROM USER_QUERIES.JSON FILE)
    queries = load_queries()

    # ORIGINAL USER-AGENT OF MY CHROME BROWSER
    custom_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"

    # BASE URL
    base_url = "https://www.amazon.com/gp/goldbox?ref_=nav_cs_gb&discounts-widget=%2522%257B%255C%2522state%255C%2522%253A%257B%255C%2522refinementFilters%255C%2522%253A%257B%257D%257D%252C%255C%2522version%255C%2522%253A1%257D%2522"

    # INITIALIZING THE AMAZONSCRAPER OBJECT
    scraper = AmazonScraper(user_agent=custom_user_agent, base_url=base_url, search_queries=queries)

    try:
        # START SCRAPING
        scraper.scrape()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == '__main__':
    main()
