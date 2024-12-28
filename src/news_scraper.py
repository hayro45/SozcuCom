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

class NewsScraper:
    def __init__(self):
        self.base_url = "https://www.sozcu.com.tr/"
        
        options = Options()
        options.add_argument("--disable-notifications")
        options.add_extension("../extensions/AdBlock.crx")
        options.add_argument("--disable-popup-blocking")
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()

        self.links = {}
        self.news = {}
        # AdBlock uzantısının sayfasını kapatma
        time.sleep(5)  # Uzantının sayfasının açılması için bekle
        if len(self.driver.window_handles) > 1:
            self.driver.switch_to.window(self.driver.window_handles[1])
            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

    def load_links(self):
        with open('links.json', 'r') as json_file:
            self.links = json.load(json_file)

    def scrape_news(self):
        for category, links in self.links.items():
            category_news = []
            for link in links:
                self.driver.get(link)
                try:
                    WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "news-body"))
                    )
                    news_body = self.driver.find_element(By.CLASS_NAME, "news-body")
                    
                    title = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.TAG_NAME, "h1"))
                    ).text

                    # Describe bölümünü bulma
                    try:
                        describe = news_body.find_element(By.CLASS_NAME, "description").text
                    except:
                        describe = "No description available"

                    # Author bölümünü bulma
                    try:
                        author = news_body.find_element(By.CLASS_NAME, "content-meta-name").text
                    except:
                        author = "No author available"

                    # Created date bölümünü bulma
                    try:
                        created_date = news_body.find_element(By.TAG_NAME, "time").get_attribute("datetime")
                    except:
                        created_date = "No date available"

                    # Content bölümünü bulma
                    try:
                        content = "\n\n".join([p.text for p in news_body.find_elements(By.TAG_NAME, "p") if p.text.strip() != ""])
                    except:
                        content = "No content available"

                    news_item = {
                        "title": title,
                        "content": content,
                        "describe": describe,
                        "author": author,
                        "created_date": created_date,
                        "url": link
                    }
                    category_news.append(news_item)
                    print(f"Scraped: {title}")
                except Exception as e:
                    print(f"Failed to scrape {link}: {e}")

            self.news[category] = category_news

        # JSON dosyasına kaydet
        with open('news.json', 'w', encoding='utf-8') as json_file:
            json.dump(self.news, json_file, ensure_ascii=False, indent=4)

    def __del__(self):
        self.driver.quit()

scraper = NewsScraper()
scraper.load_links()
scraper.scrape_news()