from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/get_attribute.html")
    out = calc(browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex"))
    browser.find_element(By.ID, "answer").send_keys(out)
    browser.find_element(By.ID, "robotCheckbox").click()
    browser.find_element(By.ID, "robotsRule").click()
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()
    time.sleep(5)



finally:
    browser.quit()