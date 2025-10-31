from conftest import driver
from data import Data
from generator import Person
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestAuthorization:

    # Вход по кнопке «Войти в аккаунт» на главной
    def test_enter_login_account_button(self, driver):

        driver.find_element(*Locators.BTN_ACC_ENTER).click()
        driver.get(Data.SB_LOGIN)
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.FIELD_EMAIL_ID).send_keys(Person.email)
        driver.find_element(*Locators.FIELD_PASS_ID).send_keys(Person.password)
        driver.find_element(*Locators.BTN_LOGIN).click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'

    # Вход через кнопку «Личный кабинет»
    def test_enter_button_personal_account(self, driver):

        driver.find_element(*Locators.BTN_P_ACC).click()
        driver.get(Data.SB_LOGIN)
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.FIELD_EMAIL_ID).send_keys(Person.email)
        driver.find_element(*Locators.FIELD_PASS_ID).send_keys(Person.password)
        driver.find_element(*Locators.BTN_LOGIN).click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'

    # Вход через кнопку в форме регистрации
    def test_button_enter_login_page(self, driver):

        driver.get(Data.SB_REG)
        driver.find_element(*Locators.LINK_LOGIN_REGFORM).click()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.FIELD_EMAIL_ID).send_keys(Person.email)
        driver.find_element(*Locators.FIELD_PASS_ID).send_keys(Person.password)
        driver.find_element(*Locators.BTN_LOGIN).click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'

    # Вход через кнопку в форме восстановления пароля
    def test_button_enter_password_recovery(self, driver):

        driver.find_element(*Locators.BTN_P_ACC).click()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.LINK_REC_PASS).click()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.LINK_LOGIN_RECPASS).click()
        WebDriverWait(driver, 3)
        driver.find_element(*Locators.FIELD_EMAIL_ID).send_keys(Person.email)
        driver.find_element(*Locators.FIELD_PASS_ID).send_keys(Person.password)
        driver.find_element(*Locators.BTN_LOGIN).click()
        order_button = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_ORDER))

        assert order_button.text == 'Оформить заказ'
        