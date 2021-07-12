import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link2 = 'http://suninjuly.github.io/find_link_text'
search_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

if __name__ == "__main__":
    try:
        browser = webdriver.Chrome()
        browser.get(link2)
        new_page = browser.find_element_by_link_text(search_text)
        time.sleep(2)
        new_page.click()
        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(30)
        # закрываем браузер после всех манипуляций
        browser.quit()

