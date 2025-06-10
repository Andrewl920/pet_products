from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
import undetected_chromedriver as uc
import pyautogui

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
    
    def find_image(self, container):
        img = container.find_element(By.XPATH, '//div[@class= "pr_lazy_img main-img nt_img_ratio nt_bg_lz lazyloadt4sed"]')
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
    img = scraper.find_image(container)
    print(img)
