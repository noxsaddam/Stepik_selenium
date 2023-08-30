from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest
import pytest


def get_text(url):
    with webdriver.Chrome() as browser:
        browser.get(url)
        # Ваш код, который заполняет обязательные поля
        browser.find_element(By.CLASS_NAME, "first_block > .form-group.first_class > .form-control.first").send_keys(
            "K")
        browser.find_element(By.CLASS_NAME, "first_block > .form-group.second_class > .form-control.second").send_keys(
            "M")
        browser.find_element(By.CLASS_NAME, "first_block > .form-group.third_class > .form-control.third").send_keys(
            "mail")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        browser.quit()
        return welcome_text


class Test(unittest.TestCase):
    def test_welcome_text1(self):
        welcome_text = get_text("http://suninjuly.github.io/registration1.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")

    def test_welcome_text2(self):
        welcome_text = get_text("http://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    unittest.main()
