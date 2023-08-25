from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from calc_func import calc

browser = webdriver.Chrome()

try:
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()
    window_1 = browser.window_handles[1]
    browser.switch_to.window(window_1)
    number = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(number)
    browser.find_element(By.CSS_SELECTOR, "[type=submit]").click()
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    alert.accept()
    print(answer)

    time.sleep(5)


except Exception as e:
    print(e)

finally:
    browser.quit()
