# This code will scrap the information about mobile (range under Rs. 20000) and will show the price and will make csv file.


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import csv
s=Service('/home/woc/Prachi/Training/Web_Scraping/Selenium/chromedriver')
browser = webdriver.Chrome(service=s)
url='https://www.amazon.in/'
browser.get(url)

browser.find_element(By.XPATH, value = "//input[contains(@id, \"twotabsearchtextbox\")]").send_keys("Phones under 20000")

browser.find_element(By.XPATH,value = "//span[contains(@id,\'nav-search-submit-text\')]").click()
browser.find_element(By.XPATH,value = "//span[contains(@class,\'a-size-base a-color-base\')]").click()

for page in range(15):
    browser.get("https://www.amazon.in/s?k=Phones+under+20000&page={}&crid=JJAQEX32MALC&qid=1650520689&sprefix=phones+under+20000%2Caps%2C194&ref=sr_pg_3".format(page))
    mobiles = browser.find_elements(By.XPATH, value = "//span[contains(@class,\"a-size-medium a-color-base a-text-normal\")]")
    prices = browser.find_elements(By.XPATH,value = '//span[contains(@class,"a-price-whole")]')

    with open("mobiles.csv","a") as fl:
        for mobile,price in zip(mobiles,prices):
            print(mobile.text)
            print(price.text)
            csv.writer(fl).writerow([mobile.text,price.text])
fl.close()

