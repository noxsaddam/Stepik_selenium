import time
import math
import pytest
from selenium.webdriver.common.by import By
import stepic_login_and_password
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait


def time_now():
    return math.log(int(time.time()))


class TestAlienMessage:
    out_text = ''
    correct_asnwer = "Correct!"
    url = """https://stepik.org/lesson/236895/step/1
        https://stepik.org/lesson/236896/step/1
        https://stepik.org/lesson/236897/step/1
        https://stepik.org/lesson/236898/step/1
        https://stepik.org/lesson/236899/step/1
        https://stepik.org/lesson/236903/step/1
        https://stepik.org/lesson/236904/step/1
        https://stepik.org/lesson/236905/step/1""".splitlines()

    def test_login_stepic(self, browser):
        browser.get('https://stepik.org/learn')
        browser.find_element(By.ID, 'id_login_email').send_keys(stepic_login_and_password.login)
        browser.find_element(By.ID, 'id_login_password').send_keys(stepic_login_and_password.password)
        browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()

        # Ожидание загрузки страницы после авторизации
        WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located(
            (By.CLASS_NAME, 'drop-down.drop-down-menu.ember-view.navbar__profile')))

    @pytest.mark.parametrize('url', url)
    def test_correct_answer(self, browser, url):
        browser.get(url)

        # Если задача уже решалась, нажатие кнопки Повторное решение(Рестарт задания)
        re_decision = browser.find_elements(By.CLASS_NAME, 'again-btn.white')
        if re_decision:
            re_decision[0].click()

        # Ожидание окна ввода
        reply_field = WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(
            (By.CLASS_NAME, 'ember-text-area')))

        # Очистка окна ввода
        if reply_field.text:
            reply_field.clear()

        reply_field.send_keys(time_now())
        browser.find_element(By.CLASS_NAME, 'submit-submission').click()
        # Ожидание ответа
        WebDriverWait(browser, 5).until(
            expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'smart-hints__hint')))
        answer = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
        check_answer = answer == self.correct_asnwer
        if not check_answer:
            self.out_text += answer
        assert answer == self.correct_asnwer, "Сообщение не совподает"

    def __del__(self):
        print(self.out_text) if self.out_text else None
