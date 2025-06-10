import scraper
import excel

if __name__ == "__main__":
    scraper = scraper.WebScraping()
    excel = excel.Excel()

    container = scraper.find_container(0)
    img = scraper.find_image(container)
    print(img)