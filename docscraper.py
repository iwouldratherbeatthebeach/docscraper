import os
import requests
from lxml import html
from urllib.parse import urljoin, urlparse
import time

# Base URL of the documentation site
base_url = "https://docs.{YOURSITE}.com/Documentation"

# Create a directory to save the documentation
os.makedirs("Docs", exist_ok=True)

visited_links = set()  # To avoid visiting the same link multiple times

def fetch_page(url):
    """Fetch the content of a URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.content
    except requests.RequestException as e:
        print(f"Failed to fetch {url}: {e}")
        return None

def extract_content(page_content):
    """Extract text content from the specific XPath."""
    try:
        tree = html.fromstring(page_content)
        content = tree.xpath('//*[@id="mw-content-text"]//text()')
        return "\n".join(content).strip()
    except Exception as e:
        print(f"Failed to extract content: {e}")
        return None

def scrape_docs(url):
    """Recursively scrape documentation starting from the given URL."""
    if url in visited_links:
        return
    
    print(f"Visiting: {url}")
    visited_links.add(url)

    page_content = fetch_page(url)
    if not page_content:
        return
    
    # Extract and save content from the page
    doc_text = extract_content(page_content)
    if doc_text:
        # Save the content to a .txt file
        doc_title = urlparse(url).path.replace("/", "_").strip("_")
        with open(f"Docs/{doc_title}.txt", "w", encoding="utf-8") as file:
            file.write(doc_text)
        print(f"Saved: {doc_title}.txt")
    
    # Parse the page to find new links to follow
    tree = html.fromstring(page_content)
    links = tree.xpath('//a[contains(@href, "/Documentation/")]/@href')
    for link in links:
        full_link = urljoin(base_url, link)
        if base_url in full_link:
            scrape_docs(full_link)  # Recursive call for new links

if __name__ == "__main__":
    start_url = base_url
    scrape_docs(start_url)
