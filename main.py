import scraper
import excel
import time

if __name__ == "__main__":
    scraper = scraper.WebScraping()
    product_info = {}
    products = []

    #search product from the shopify website
    scraper.close_popup()
    container = scraper.find_container(0)
    container.click()
    time.sleep(3)
    
    product_name = scraper.get_product_name()
    product_price = scraper.get_product_price()
    product_link = scraper.get_product_link()
    product_pic = "https:" + scraper.find_non_script()
    
    product_info["Name"] = product_name
    product_info["Price"] = product_price 
    product_info["Picture"] = product_pic
    product_info["Link"] = product_link 
    
    excel = excel.Excel()
    last_row = excel.find_last_row("Dog")
    excel.fill_in_value("Dog", last_row, product_info, pic)
    
    
    