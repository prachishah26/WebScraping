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

s=Service('/home/woc/Prachi/Training/Web_Scraping/Selenium/chromedriver')
browser = webdriver.Chrome(service=s)
url='https://www.blurtit.com'
browser.get(url)

# Topics
first_section = browser.find_element(by = By.XPATH, value = '//*[ text() = \'Topics\' ]')
first_section.click()

#Science
second_section = browser.find_element(by=By.XPATH, value='//*[ text() = \'Science\' ]')
second_section.click()

#Computer SCience
third_section = browser.find_element(by=By.XPATH, value='//*[ text() = \'Computer Science\' ]')
third_section.click()

number_of_pages = 10

for page in range(number_of_pages):
    questions = browser.find_elements(by = By.XPATH,value = "//div[@class =\"feed-item-title clearfix\"]/a")
    with open("Questions.txt","a") as question_file:
        for question in questions:
            question_file.write(question.text + "\n")
            # print(questions[index].text)
        if page == number_of_pages - 1:
            break
        next = browser.find_element(by = By.XPATH,value = '//*[ text() = \'>\' ]')
        next.click()
question_file.close()

