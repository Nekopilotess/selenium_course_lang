import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture
def browser(): #сделали эту функцию фикстурой, вызываем ее отдельно в каждом методе класса, функция-фикстура автоматически выполняет teardown в конце выполнения теста
    print("\nstart browser for test ..")
    browser = webdriver.Chrome()
    yield browser #остановочка, бежит выполнять тест
    #этот код выполнится после завершения теста
    print("\nQuit browser")
    browser.quit()

@pytest.fixture(autouse=True) #для каждого теста фикстура подготовки данных выполнилась без явного вызова
def prepare_data():
    print()
    print("generating data for every test")

class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        # не передаём как параметр фикстуру prepare_data, но она все равно выполняется
        print("start test 1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test 1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test 2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test 2")