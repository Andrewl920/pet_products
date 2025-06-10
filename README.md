# Web Scraper

A Python-based web scraper that can extract product information from websites and save it to a CSV file.

## Features

- Scrapes multiple pages of product listings
- Extracts product titles, prices, and URLs
- Saves data to CSV format
- Includes error handling and logging
- Respects websites by implementing random delays between requests

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Open `scraper.py` and modify the following:
   - Update the `base_url` in the `main()` function to your target website
   - Adjust the CSS selectors in the `scrape_products()` method to match your target website's HTML structure
   - Modify the number of pages to scrape by changing the `num_pages` parameter

2. Run the script:
```bash
python scraper.py
```

The script will create a `products.csv` file with the scraped data.

## Important Notes

- Always check the website's robots.txt and terms of service before scraping
- Implement appropriate delays between requests to avoid overwhelming the server
- Some websites may require additional headers or authentication
- The script includes basic error handling, but you may need to adjust it based on your specific needs

## Dependencies

- requests: For making HTTP requests
- beautifulsoup4: For parsing HTML
- pandas: For data manipulation and CSV export
- lxml: For faster HTML parsing 