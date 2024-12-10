import random
import time
import json
import os
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


# CSS SELECTOR
amazon_search_box_css_selector = 'input[aria-label="Search Amazon"]'
search_result_items_css_selector = 'span[data-csa-c-type="item"]'
item_total_reviews_css_selector = 'div[data-csa-c-slot-id="alf-reviews"]'
item_price_css_selector = 'span[class = "a-price"] span[aria-hidden = "true"]'
item_image_link_css_selector = 'img[class = "s-image"]'
next_page_css_selector = 'span[class = "s-pagination-strip"] a[aria-label ^= "Go to next page"]'

# PRODUCT DATA MODEL
class Product:
    def __init__(self, title, total_reviews, price, image_link):
        self.title = title
        self.total_reviews = total_reviews
        self.price = price
        self.image_link = image_link

    def to_dict(self):
        return {
            "title": self.title,
            "total_reviews": self.total_reviews,
            "price": self.price,
            "image_link": self.image_link
        }

# MAIN AMAZONSCRAPER CLASS
class AmazonScraper:
    def __init__(self, user_agent, base_url, search_queries, max_pages=20): 
        self.user_agent = user_agent
        self.base_url = base_url
        self.search_queries = search_queries
        self.max_pages = max_pages

        # SETTING UP THE UNDETECTED CHROME DRIVER
        options = uc.ChromeOptions()
        # options.headless = True
        options.add_argument(f"--user-agent={self.user_agent}")
        options.add_argument('--headless')
        self.driver = uc.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 60)

    # MAIN SCRAPING FUNCTION
    def scrape(self):
        self.driver.get(self.base_url)

        for query in self.search_queries:
            print(f"Scraping products for query: {query}")

            # PERFORM SEARCH FOR FETCHED QUERY
            self.perform_search(query)

            # SCRAPE THE DATA
            data = self.scrape_data()

            # SAVING THE DATA FOR THE RELEVANT QUERY
            self.save_data_to_json(data, query)

            # RANDOM DELAY
            time.sleep(random.uniform(10, 20))

        self.driver.quit()

    # FUNCTION TO PERFORM SEARCH
    def perform_search(self, query):
        # WAITING FOR THE SEARCH BOX TO BE VISIBLE
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, amazon_search_box_css_selector)))

        # CLEARING THE SEARCH BAR
        search_bar = self.driver.find_element(By.CSS_SELECTOR, amazon_search_box_css_selector)
        search_bar.clear()
        time.sleep(1)

        # USING THE HUMAN SPEED TO TYPE TO STAY UNDETECTED
        for char in query:
            search_bar.send_keys(char)
            time.sleep(0.4)

        # PRESS ENTER TO SEARCH
        search_bar.send_keys(Keys.RETURN)
        time.sleep(random.uniform(2, 4))  # Wait for the results to load

    # FUNCTION TO HANDLE MOVING TO NEXT PAGE (HITTING THE NEXT PAGE BUTTON)
    def next_page(self):
        try:
            button = self.driver.find_element(By.CSS_SELECTOR, next_page_css_selector)
            button.click()
            time.sleep(random.uniform(3, 5))
            return True
        except NoSuchElementException:
            print("No next page button found or reached the last page.")
            return False

    # FUNCTION TO SAVE THE SCRAPED DATA
    def save_data_to_json(self, data, query):
        folder_path = 'scraped_data'

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # FILE PATH
        file_path = os.path.join(folder_path, f"{query}.json")

        # SAVING THE DATA TO THE FILE
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

        print(f"Data saved for query '{query}' in folder '{folder_path}'")

    # FUNCTION TO START SCRAPING
    def scrape_data(self):
        data = []  # LIST TO STORE DATA
        page_count = 0

        while page_count < self.max_pages:
            try:
                self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, search_result_items_css_selector)))
                result_items = self.driver.find_elements(By.CSS_SELECTOR, search_result_items_css_selector)

                for item in result_items:
                    try:
                        title = item.find_element(By.CSS_SELECTOR, 'h2').text
                    except NoSuchElementException:
                        title = 'None'
                    try:
                        total_reviews = item.find_element(By.CSS_SELECTOR,
                                                          item_total_reviews_css_selector).text
                    except NoSuchElementException:
                        total_reviews = 'None'
                    try:
                        price = item.find_element(By.CSS_SELECTOR,
                                                  item_price_css_selector).text.replace('\n','.')
                    except NoSuchElementException:
                        price = 'None'
                    try:
                        image_link = item.find_element(By.CSS_SELECTOR, item_image_link_css_selector).get_attribute(
                            'src')
                    except NoSuchElementException:
                        image_link = 'None'

                    time.sleep(1)
                    # ADDING THE DATA IN THE FORM DICTIONARY TO DATA LIST
                    product = Product(title, total_reviews, price, image_link)
                    data.append(product.to_dict())

                # MOVE TO NEXT PAGE
                time.sleep(random.uniform(3, 7)) # TO ADD RANDOM DELAYS
                if not self.next_page():  # IF THERE IS NO NEXT BUTTON IT WILL BREAK THE LOOP
                    break
                page_count += 1

            except:
                print("No more products found or navigation error.")
                break

        return data


