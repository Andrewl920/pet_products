import scraper
import excel
import time
import requests
from openpyxl.drawing.image import Image as ExcelImage

if __name__ == "__main__":
    scraper = scraper.WebScraping()

    #search product from the shopify website
    scraper.close_popup()
    container = scraper.find_container(0)
    container.click()
    time.sleep(3)
    
    product_name = scraper.get_product_name()
    product_price = scraper.get_product_price()
    product_link = scraper.get_product_link()
    product_pic = "https:" + scraper.find_non_script()
    response = requests.get(product_pic)
    
    excel = excel.Excel()
    with open(product_name, 'wb') as f:
        f.write(response.content)
    
    img = ExcelImage(product_name)
    img.width = 100
    img.height = 100
    excel.workbook["Dog"].row_dimensions[2].height = 100
    excel.workbook["Dog"].column_dimensions["A"].width = 100
    excel.workbook["Dog"].add_image(img, "A2")
    excel.workbook.save(excel.file_path)
    