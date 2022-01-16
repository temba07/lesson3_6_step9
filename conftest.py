from selenium.webdriver.chrome.options import Options
import pytest
from selenium import webdriver

options = Options()
options.add_experimental_option('prefs', {'intl.accept_languages': 'es'})
browser = webdriver.Chrome(options=options)


@pytest.fixture()
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
