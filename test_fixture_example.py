import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://p-on.ru/login"


@pytest.fixture()
def open_page():
    print('car telemetry system')
    open_page = webdriver.Chrome()
    return open_page


class TestSearch():
    def test_p_on(self, open_page):
        open_page.get(link)
