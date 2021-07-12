import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'
wait = WebDriverWait(browser, 10)

def math_calc():
    x = int(browser.find_element(By.ID, 'input_value').text)
    res = str(math.log(math.fabs(12 * math.sin(int(x)))))
    return res

def alert_parsing():
    alert = browser.switch_to.alert
    alert_txt = alert.text
    final_res = alert_txt.split()[-1]
    return final_res

try:
    browser.get(link)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()
    answer = math_calc()
    answer_field = browser.find_element(By.ID, 'answer')
    answer_field.send_keys(answer)
    sub_button = browser.find_element(By.ID, 'solve')
    sub_button.click()
finally:
    time.sleep(10)
    browser.quit()