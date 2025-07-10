import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os

# Create articles directory if it doesn't exist
if not os.path.exists('articles'):
    os.makedirs('articles')

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

service = Service('./chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)

# Fetch the URL
url = "https://en.prothomalo.com/search?q=accident"
driver.get(url)
time.sleep(3)

articles = driver.find_elements(By.CSS_SELECTOR, "div.K-MQV a")
printed = 0
printed_links = set()  

for article in articles:
    href = article.get_attribute("href")
    title = article.text.strip()

    if href and title and href not in printed_links:
        print(f"{printed + 1}. {title}")
        print(f"   🔗 {href}\n")
        printed_links.add(href)
        printed += 1

    if printed == 5:
        break

for i, link in enumerate(printed_links, 1):
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")
    title = soup.find("h1").get_text(strip=True)
    content = " ".join([p.get_text(strip=True) for p in soup.find_all("p")])

    
    # Create a file name from the article title or use a default name
    # file_name = f'article_{i}.txt'
    # file_path = os.path.join('articles', file_name)
    
    # # Save the article text to a file
    # with open(file_path, 'w', encoding='utf-8') as f:
    #     f.write(content)
    # print(f"Saved article {i} to {file_path}")

driver.quit()
