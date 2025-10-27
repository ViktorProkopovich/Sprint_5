from conftest import driver
from data import Data
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from generator import Random


class TestRegistration:

    # Успешная регистрация
    def test_registration_successful(self, driver):

        driver.find_element(*Locators.BTN_P_ACC).click()
        WebDriverWait(driver, 10)
        driver.find_element(*Locators.LINK_REG).click()
        WebDriverWait(driver, 10)
        driver.find_element(*Locators.FIELD_REG_NAME).send_keys(Random.user_name)
        driver.find_element(*Locators.FIELD_REG_EMAIL).send_keys(Random.email)
        driver.find_element(*Locators.FIELD_REG_PASSWORD).send_keys(Random.password)
        driver.find_element(*Locators.BTN_REG).click()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.BTN_LOGIN_iN_ACC))

        assert driver.current_url == Data.SB_LOGIN

    # Ошибка для некорректного пароля
    def test_registration_unsuccessful(self, driver):
        driver.find_element(*Locators.BTN_P_ACC).click()
        WebDriverWait(driver, 10)
        driver.find_element(*Locators.LINK_REG).click()
        WebDriverWait(driver, 10)
        driver.find_element(*Locators.FIELD_REG_NAME).send_keys(Random.user_name)
        driver.find_element(*Locators.FIELD_REG_EMAIL).send_keys(Random.email)
        driver.find_element(*Locators.FIELD_REG_PASSWORD).send_keys("qwert")
        driver.find_element(*Locators.BTN_REG).click()
        incorrect_password = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(Locators.MSG_PASS_ERROR))

        assert incorrect_password.text == "Некорректный пароль"
