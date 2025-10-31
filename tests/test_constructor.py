from conftest import driver
from locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructorCrossing:
    
    # Переход к разделу "Булки"
    def test_buns_cross(self, driver):
        driver.find_element(*Locators.BTN_SAUCES).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_SAUCES))
        driver.find_element(*Locators.BTN_BUNS)
        buns = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_BUNS))

        assert buns.text == "Булки"

    # Переход к разделу "Соусы"
    def test_sauces_cross(self, driver):
        driver.find_element(*Locators.BTN_SAUCES).click()
        sauces = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_SAUCES))

        assert sauces.text == "Соусы"

    # Переход к разделу "Начинки"
    def test_fillings_cross(self, driver):
        driver.find_element(*Locators.BTN_FILLINGS).click()
        fillings = WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.BTN_FILLINGS))

        assert fillings.text == "Начинки"
