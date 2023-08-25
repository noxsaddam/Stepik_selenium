from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from calc_func import calc

browser = webdriver.Chrome()

try:
    browser.implicitly_wait(5)  # Время ожидания всех объектов
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 10).until(ec.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()
    number = calc(browser.find_element(By.ID, "input_value").text)
    browser.find_element(By.ID, "answer").send_keys(number)
    browser.find_element(By.ID, "solve").click()
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    alert.accept()
    print(answer)
    time.sleep(5)


except Exception as e:
    print(e)

finally:
    browser.quit()
