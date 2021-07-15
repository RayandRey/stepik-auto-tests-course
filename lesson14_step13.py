import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestPage(unittest.TestCase):
    def test_registration1(self):
        link1 = 'http://suninjuly.github.io/registration1.html'
        required_field_selectors = [".first_block .form-control.first", ".first_block .form-control.second",
                                    ".first_block .form-control.third"]
        browser = webdriver.Chrome()
        browser.get(link1)
        for field_selector in required_field_selectors:
            elements = browser.find_element(By.CSS_SELECTOR, field_selector)
            elements.send_keys("test")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_txt_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_txt_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Kek")

    def test_registration2(self):
        link2 = 'http://suninjuly.github.io/registration2.html'
        required_field_selectors = [".first_block .form-control.first", ".first_block .form-control.second",
                                    ".first_block .form-control.third"]
        browser = webdriver.Chrome()
        browser.get(link2)
        for field_selector in required_field_selectors:
            elements = browser.find_element(By.CSS_SELECTOR, field_selector)
            elements.send_keys("test")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        time.sleep(1)
        welcome_txt_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_txt_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Kek")


if __name__ == "__main__":
    unittest.main()
