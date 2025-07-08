import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service  

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--window-size=1920x1080")

service = Service('./chromedriver-win64/chromedriver.exe')

driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://en.prothomalo.com/")
time.sleep(5)  # wait for page to load
print(driver.title)
driver.quit()