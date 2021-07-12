from selenium import webdriver
import time

URL = 'http://suninjuly.github.io/registration1.html'
URL2 = 'http://suninjuly.github.io/registration2.html'


def main(url: str) -> None:
    try:
        browser = _browser(url)
        # заполняем обязательные поля
        for i in range(1, 4):
            input = browser.find_element_by_tag_name(
                f'div:nth-child({i}) input')
            input.send_keys("lol")
        # нажимаем кнопку
        _button_clicker(browser, selector="button.btn")
        time.sleep(3)
        # находим элемент, содержащий текст и проверяем на совпадение
        welcome_text = browser.find_element_by_tag_name("h1").text
        assert welcome_text == "Congratulations! You have successfully registered!"
    finally:
        time.sleep(1)
        browser.quit()


def _browser(url: str) -> object:
    try:
        browser = webdriver.Chrome()
        browser.get(url)
        return browser
    except Exception as ex:
        print(f'{ex} in browser func')


def _button_clicker(browser: object, selector: str) -> None:
    try:
        button = browser.find_element_by_css_selector(selector)
        button.click()
    except Exception as ex:
        print(f'{ex} in botton_clicker func')


if __name__ == '__main__':
    main(URL2)
