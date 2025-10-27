from conftest import driver
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from generator import Person

class TestCrossingPages:
    
    # Переход по клику на «Личный кабинет»
    def test_cross_page_login(self, driver):
        driver.find_element(*Locators.BTN_P_ACC).click()
        WebDriverWait(driver, 3)

        assert driver.current_url == Data.SB_LOGIN

    # Переход из личного кабинета в конструктор 
    def test_cross_page_constractor(self, driver):
        driver.find_element(*Locators.BTN_P_ACC).click()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.BTN_CONSTR).click()
        WebDriverWait(driver, 10)

        assert driver.current_url == Data.SB_HOME

    # Переход по клику на логотип Stellar Burgers
    def test_cross_page_logo_sb(self, driver):
        driver.find_element(*Locators.BTN_P_ACC).click()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.BTN_LOGO_SB).click()
        WebDriverWait(driver, 3)

        assert driver.current_url == Data.SB_HOME

    # Проверка выхода из аккаунта
    def test_personal_account_exit(self, driver):
        driver.find_element(*Locators.BTN_P_ACC).click()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.FIELD_EMAIL_ID).send_keys(Person.email)
        driver.find_element(*Locators.FIELD_PASS_ID).send_keys(Person.password)
        driver.find_element(*Locators.BTN_LOGIN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))
        driver.find_element(*Locators.BTN_P_ACC).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_EXIT))
        driver.find_element(*Locators.BTN_EXIT).click()
        log_out = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BTN_LOGIN))

        assert log_out.text == "Войти"
