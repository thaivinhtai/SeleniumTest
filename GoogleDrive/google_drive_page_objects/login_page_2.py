"""This module provides web elements of login page."""

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def get_password_textbox(driver):
    """The location of input password textbox."""
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.XPATH,
                                               "//input[@type='password']")))
    wait.until(EC.visibility_of_element_located((By.XPATH,
                                                 "//input[@type='password']")))
    return driver.find_element_by_xpath("//input[@type='password']")


def get_login_button(driver):
    """The location of login button."""
    return driver.find_element_by_xpath('//*[@id="passwordNext"]')
