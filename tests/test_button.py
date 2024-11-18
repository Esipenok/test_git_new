from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options # это для безголового режима

@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless') # так мы запускаем безголовый режим. Нужен для запуска автотестов в гитхабе
    crome_browser = webdriver.Chrome(options=options)
    return crome_browser

def test_button_exist(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()