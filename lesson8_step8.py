from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    browser.get(link)
    required_fields = browser.find_elements(By.CLASS_NAME, 'form-control')
    file_button = browser.find_element(By.ID, 'file')
    sub_button = browser.find_element(By.TAG_NAME, 'button')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "../file.txt"
    file_path = os.path.join(current_dir, file_name)
    for required_field in required_fields:
        required_field.send_keys('test')
    file_button.send_keys(file_path)
    sub_button.click()

finally:
    time.sleep(5)
    browser.quit()