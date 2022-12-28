import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/fr/catalogue/coders-at-work_207/"


def test_should_see_basket_button(browser):
    browser.get(link)
    browser.find_element(By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    assert True

def test_should_see_basket_text_button(browser):
    browser.get(link)
    time.sleep(30)
    browser.find_element(By.CSS_SELECTOR, '[value="Ajouter au panier"]')
    assert True