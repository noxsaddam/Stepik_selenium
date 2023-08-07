from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("https://suninjuly.github.io/selects1.html")
    answer = str(int(browser.find_element(By.ID, "num1").text) + int(browser.find_element(By.ID, "num2").text))
    select = Select(browser.find_element(By.CLASS_NAME, "custom-select"))
    select.select_by_value(answer)
    browser.find_element(By.CLASS_NAME, "btn.btn-default").click()
    time.sleep(5)
    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()



finally:
    browser.quit()