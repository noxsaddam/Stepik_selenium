import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--language", action='store', default=None, help="Choose language")


@pytest.fixture()
def browser(request):
    language_param = request.config.getoption("language")
    print(language_param)
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language_param})
    options.add_argument("start-maximized")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(5)
    yield browser
    browser.quit()
