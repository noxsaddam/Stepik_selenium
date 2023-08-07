from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/math.html")
    out = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(out)
    browser.find_element(By.CSS_SELECTOR, "[for = 'robotCheckbox']").click()
    browser.find_element(By.CSS_SELECTOR, "[for = 'robotsRule']").click()

    print(browser.find_element(By.ID, "robotsRule").get_attribute("type"))

    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
    time.sleep(5)



finally:
    browser.quit()
