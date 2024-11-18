from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options  # это для безголового режима


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')  # так мы запускаем безголовый режим. Нужен для запуска автотестов в гитхабе
    crome_browser = webdriver.Chrome(options=options)
    return crome_browser


# первый тест
def test_button_exist_1(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()


# второй тест
def test_button_exist_2(browser):
    browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()
