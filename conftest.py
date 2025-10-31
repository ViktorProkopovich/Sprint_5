import pytest
from selenium import webdriver
from data import Data

# Фикстура открытия браузера, переход по ссылке, выполнения теста, закрытие браузера
@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.SB_HOME)
    yield driver
    driver.quit()