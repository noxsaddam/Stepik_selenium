from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

browser = webdriver.Chrome()

try:
    # Получаем путь текущей папки
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # Имя файла для отправки
    file_name = "out.txt"
    # получаем путь к out.txt
    file_path = os.path.join(current_dir, file_name)

    browser.get(" http://suninjuly.github.io/file_input.html")
    browser.find_element(By.NAME, "firstname").send_keys("K")
    browser.find_element(By.NAME, "lastname").send_keys("M")
    browser.find_element(By.NAME, "email").send_keys("gmail")

    # Отпарвка файла
    browser.find_element(By.ID, "file").send_keys(file_path)

    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

    alert = browser.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()



finally:
    time.sleep(3)
    browser.quit()
