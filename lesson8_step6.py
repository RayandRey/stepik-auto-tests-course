from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
try:
    browser.get(link)
    x = browser.find_element(By.ID, 'input_value').text
    input_answer = browser.find_element(By.ID, 'answer')
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    radio_robot = browser.find_element(By.ID, 'robotsRule')
    sub_button = browser.find_element(By.TAG_NAME, 'button')

    res = math.log(math.fabs(12*math.sin(int(x))))
    input_answer.send_keys(str(res))
    browser.execute_script("return arguments[0].scrollIntoView(true);", sub_button)
    checkbox.click()
    radio_robot.click()
    sub_button.click()
finally:
    time.sleep(3)
    browser.quit()