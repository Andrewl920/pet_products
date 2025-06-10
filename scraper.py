from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import pyautogui
import os
import requests
from bs4 import BeautifulSoup

class WebScraping:
    def __init__(self, page_number = 1):
        self.options = uc.ChromeOptions()
        self.options.headless = False
        self.driver = uc.Chrome(options=self.options)
        self.url = "https://petsthing.com.hk/collections/dog"
        self.driver.execute_cdp_cmd("Network.setBlockedURLs", {"urls": ["*doubleclick.net*", "*ads.google.com*"]})
        self.driver.get(self.url)

        if page_number == 1:
            self.url = self.url
        else: 
            self.url = self.url + "?page=" + str(page_number)

        self.driver.get(self.url)
    
    def change_to_cat(self):
        self.url = "https://petsthing.com.hk/collections/cat"

    def find_container(self, number):
        time.sleep(5)
        large_container = self.driver.find_elements(By.CLASS_NAME, "product-inner")[number]
        return large_container
    
    def find_non_script(self):
        html = self.driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        noscripts = soup.find_all("noscript")
        for tag in noscripts:
            img = tag.find("img")
            if img and img.get("src"):
                print("Image src found:", img["src"])
                break
    
    def find_product_name(self):
        product_name = self.driver.find_element(By.XPATH, "//h1[@class = 'product_title entry-title']")
        return product_name.text
        
    def find_image(self):
        img = self.driver.find_element(By.XPATH, '//div[@class= "t4s-img-noscript"]')
        return img
    
    def close_popup(self):
        try:
            close_picture = r"C:\Users\stars\OneDrive\Desktop\shopify_scrapping\pictures\close_button.png"
            time.sleep(5)
            close_location = pyautogui.locateOnScreen(close_picture)
            pyautogui.click(close_location)
            time.sleep(2)
        except:
            pass

if __name__ == "__main__":
    scraper = WebScraping()
    scraper.close_popup()
    container = scraper.find_container(0)
    container.click()
    time.sleep(5)
    product_name = scraper.find_product_name()
    scraper.find_non_script()
    # img = scraper.find_image()
    # src = img.get_attribute("src")
    # filename =os.makedirs("downloaded_images", src.split("/")[-1])
    # response = requests.get(src)
    # time.sleep(5)
    # if response.status_code == 200:
    #     with open(filename, "wb") as f:
    #         f.write(response.content)
    #     print(f"Image saved to: {filename}")
