from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.action_chains import ActionChains


class LinkScraper:
    def __init__(self):
        self.base_url = "https://www.sozcu.com.tr/"
        
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_extension("../extensions/AdBlock.crx")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

        self.news_categories = [
            'gundem', 'dunya', 'ekonomi', 'bilim-teknoloji', 'saglik', 'egitim', 'otomotiv', "gunun-icinden"
        ]
        self.links = {}

    
    def scroll_browser(self, action):
        while True:
            try:
                load_more_button = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "loadmore"))
                )
                action.move_to_element(load_more_button).perform()
                action.scroll_by_amount(0, 100).perform()  # Scroll down by 100 pixels
                load_more_button.click()
                time.sleep(2)
            except:
                break

    def scrape(self):

        for category in self.news_categories:
            url = f"{self.base_url}{category}/"
            self.driver.get(url)
            time.sleep(7)

            # Load more butonunu görene kadar scroll yap ve tıkla
            action = ActionChains(self.driver)
            self.scroll_browser(action)
           
            # Get all news links
            list_content = self.driver.find_element(By.CLASS_NAME, "list-content")
            count_of_divs = len(list_content.find_elements(By.XPATH, "./div"))
            category_links = []
            for i in range(1, count_of_divs + 1):
                news = list_content.find_element(By.XPATH, f"./div[{i}]")
                link = news.find_element(By.TAG_NAME, "a").get_attribute("href")
                category_links.append(link)
                print(link, i)  # Print the link to the console

            self.links[category] = category_links
        
        with open("links1.json", "w") as file:    
            json.dump(self.links, file, indent=4)

    def __del__(self):
        self.driver.quit()

        
app = LinkScraper()
app.scrape()