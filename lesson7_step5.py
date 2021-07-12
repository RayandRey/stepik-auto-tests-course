import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/math.html'

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser.get(link)
    x_elen = browser.find_element(By.ID, "input_value")
    input_res = browser.find_element(By.ID, "answer")
    click_btn = browser.find_element(By.TAG_NAME, "button")
    chek_box = browser.find_element(By.TAG_NAME, 'input[type="checkbox"]')
    robotsRule_radio = browser.find_element(By.ID, "robotsRule")
    x = x_elen.text
    input_res.send_keys(calc(x))
    chek_box.click()
    robotsRule_radio.click()
    click_btn.click()
finally:
    time.sleep(3)
    browser.quit()