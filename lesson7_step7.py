import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Chrome()

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))
try:
    browser.get(link)
    treasure = browser.find_element(By.ID, "treasure")
    treasure_value = treasure.get_attribute('valuex')
    input_res = browser.find_element(By.ID, "answer")
    click_btn = browser.find_element(By.TAG_NAME, "button")
    chek_box = browser.find_element(By.TAG_NAME, 'input[type="checkbox"]')
    robotsRule_radio = browser.find_element(By.ID, "robotsRule")
    input_res.send_keys(calc(treasure_value))
    chek_box.click()
    robotsRule_radio.click()
    click_btn.click()
finally:
    time.sleep(5)
    browser.quit()