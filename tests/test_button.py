from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.chrome.options import Options  # это для безголового режим
import allure

#что бы установить, нужно прописать pip3 install allure-pytest
#что бы запустить allure, нужно прописать pytest -s -v --alluredir results
#что бы собрать отчет, нужно прописать allure serve results
#что бы собрать папку с отчетом, пишем allure generate results


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--headless')  # так мы запускаем безголовый режим. Нужен для запуска автотестов в гитхабе
    crome_browser = webdriver.Chrome(options=options)
    return crome_browser

@pytest.mark.first_test
@allure.feature('first_test')#Так мы указываем, в какую группу попадет данный тест. Можно писать название стори или фичи.
# первый тест
@allure.story('displayed')# Это уже идет как подкатегория. Тут можно писать элементы стори или фичи
def test_button_exist_1(browser):
    browser.get('https://www.qa-practice.com/elements/button/simple')
    assert browser.find_element(By.ID, 'submit-id-submit').is_displayed()


@pytest.mark.first_test
@allure.feature('second_test')
# второй тест
@allure.story('displayed_2')
def test_button_exist_2(browser):
    with allure.step('Open the page'):#Так мы можем указывать шаги, которые выполняются
        browser.get('https://www.qa-practice.com/elements/button/like_a_button')
    with allure.step('Click'):
        assert browser.find_element(By.PARTIAL_LINK_TEXT, 'Click').is_displayed()
