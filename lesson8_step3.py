from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:
    browser.get(link)
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    sub_button = browser.find_element(By.TAG_NAME, 'button')
    res = int(num1)+int(num2)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(str(res))
    sub_button.click()

finally:
    time.sleep(3)
    browser.quit()