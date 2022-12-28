import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestReg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def fill_form(self, link):
        browser = self.driver
        browser.implicitly_wait(3)
        browser.get(link)

        browser.find_element(By.CSS_SELECTOR, '.first_block .first').send_keys('Ivan')
        browser.find_element(By.CSS_SELECTOR, '.first_block .second').send_keys('Petrov')
        browser.find_element(By.CSS_SELECTOR, '.third_class .third').send_keys('dog@cat.com')

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, 'h1').text
        return welcome_text

    def test_registration_1(self):
        link = 'http://suninjuly.github.io/registration1.html'
        result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", result)

    def test_registration_2(self):
        link = 'http://suninjuly.github.io/registration2.html'
        result = self.fill_form(link)

        self.assertEqual("Congratulations! You have successfully registered!", result)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

#pytest scripts/selenium_scripts
# найти все тесты в директории scripts/selenium_scripts

#pytest test_user_interface.py
# найти и выполнить все тесты в файле

#pytest scripts/drafts.py::test_register_new_user_parametrized
# найти тест с именем test_register_new_user_parametrized в указанном файле в указанной директории и выполнить

#дальше обходит все вложенные директории и ищет файлы, которые начинаются или заканчиваются на test_ .py

#далее находит все тесты, название которых начинается на test, которые находятся вне классов и
# далее внутри классов,имя классов начинается с Test и без метода __init__ внутри класса