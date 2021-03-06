# Task 1 : Blurtit QA Scrapping
# => Open Website:  https://www.blurtit.com
# => Click on: Topics (From Top Menu)
# => Click on: Technology (From right side topic list)
# => Click on: Sony (From right side sub topic list)
# => Scrap and Copy all 70 Questions in one text file. (Only Questions)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

s=Service('/home/woc/Prachi/Training/Web_Scraping/Selenium/chromedriver')
browser = webdriver.Chrome(service=s)
url='https://www.blurtit.com'
browser.get(url)

topics = browser.find_element(by = By.CLASS_NAME, value = "hlink-topics")
topics.click()


xpath_technology = "/html/body/div[3]/div[2]/ul/li[2]/div[2]/p"
technology = browser.find_element(by=By.XPATH, value=xpath_technology)
technology.click()

xpath_sony = "/html/body/div[3]/div[2]/aside[2]/ul/li[6]/div[2]/p/a"
sony = browser.find_element(by=By.XPATH, value=xpath_sony)
sony.click()

for page in range(4):
    questions = browser.find_elements(by = By.XPATH,value = "//div[@class =\"feed-item-title clearfix\"]/a")
    with open("MyFile.txt","a") as file1:
        for question in questions:
            file1.write(question.text + "\n")
            # print(questions[index].text)
        if page == 3:
            break
        next = browser.find_element(by = By.XPATH,value = "/html/body/div[3]/div[1]/div/div/ul/li[7]/a")
        next.click()
file1.close()
