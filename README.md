## docScraper
This script allows you to recursively scrape content from any website by extracting specific text using a user-defined XPath. It is ideal for archiving documentation or other structured content from various websites.

## Features
Recursive Scraping: Traverses through all internal links starting from a base URL.
XPath Filtering: Extracts only the desired content based on a specified XPath.
Output: Saves extracted text content into .txt files, named according to the page URL structure.
Prerequisites
Python 3.x

## Dependencies: Install the required libraries using pip:

pip install requests lxml

## Setup and Usage

Modify the Script: Open the script and update the following:

base_url: Set this to the starting URL of the site you want to scrape.
xpath_to_extract: Specify the XPath of the content you want to extract.

## How to Find the XPath:

Open the target website in a browser.
Right-click the element containing the desired content and select Inspect.
In the browser's developer tools, right-click the highlighted element and choose Copy > Copy XPath.
Replace xpath_to_extract in the script with the copied XPath.
Run the Script: Execute the script to start scraping:

python scraper.py

## Output: Extracted content will be saved as .txt files in the Docs directory.

## Example
If you're scraping from a documentation site:

Base URL: https://example.com/docs
XPath: //*[@id="main-content"]

## Update the script:

base_url = "https://example.com/docs"
xpath_to_extract = '//*[@id="main-content"]'

## Notes
Respect Robots.txt: Ensure the target site allows scraping by checking its robots.txt file.
Rate Limiting: Avoid overwhelming the server by adding delays between requests.
Disclaimer: Scrape responsibly and only from sites you have permission to access.
