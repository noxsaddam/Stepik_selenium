import time
from selenium.webdriver.common.by import By

url = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket(browser):
    browser.get(url)
    # time.sleep(30)
    button = browser.find_elements(By.CLASS_NAME, 'btn.btn-lg.btn-primary.btn-add-to-basket')
    assert False if not button else True, ' no button'
