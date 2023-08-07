from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/alert_accept.html")
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    number = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(number)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    time.sleep(3)

    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    alert.accept()
    print(answer)

except Exception as e:
    print(e)

finally:
    browser.quit()
