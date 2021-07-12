from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

browser = webdriver.Chrome()
link1 = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(link1)
    first_button = browser.find_element(By.TAG_NAME, 'button')
    first_button.click()
    new_window = browser.window_handles
    browser.switch_to.window(new_window[1])

    x = int(browser.find_element(By.ID, 'input_value').text)
    res = str(math.log(math.fabs(12*math.sin(int(x)))))

    res_field = browser.find_element(By.ID, 'answer')
    res_field.send_keys(res)

    sub_button = browser.find_element(By.TAG_NAME, 'button')
    sub_button.click()

    alert = browser.switch_to.alert
    alert_txt = alert.text
    final_res = alert_txt.split()[-1]
    print(final_res)
    alert.accept()
finally:
    time.sleep(10)
    browser.quit()