from selenium import webdriver # pip install selenium
import time

driver = webdriver.Chrome(executable_path="C:\Program File (x86)\Google\Chrome\chromedriver.exe") # From Chrome on windows

driver.get("https://www.instagram.com/") # Любой сайт который хотите просматривать
refreshrate = int(10)

while True:
    time.sleep(refreshrate)
    driver.refresh()