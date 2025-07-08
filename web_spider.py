import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By  # Added import

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

driver.quit()
