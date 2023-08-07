from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/execute_script.html")
    answer = calc(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    browser.find_element(By.ID, "answer").send_keys(answer)

    # Скролл страницы до кнопки
    button = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']").click()
    time.sleep(2)

    button.click()
    time.sleep(5)
    alert = browser.switch_to.alert
    out = alert.text.split()[-1]
    alert.accept()
    print(out)


finally:
    browser.quit()
