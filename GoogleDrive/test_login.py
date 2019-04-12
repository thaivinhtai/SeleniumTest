"""This module tests automation login to google drive using firefox."""

from google_drive_page_objects import (google_home_page, drive_home_page,
                                       login_page_1, login_page_2)
import utility


def access_google(browser='firefox', url="https://www.google.com/"):
    """
    access_google() ->  generate a webdriver and access google.

    optional argument:
        browser     --  name of browser, default is firefox.
        url         --  url to be accessed.
    """
    driver = utility.get_browser(browser)
    driver.get(url)
    driver.implicitly_wait(5)
    return driver


def navigate_google_drive(driver):
    """
    navigate_google_drive(drive)    ->  go to google drive page.
    """
    google_home_page.get_list_apps(driver).click()
    google_home_page.get_drive(driver).click()
    drive_home_page.get_access_buton(driver).click()
    driver.implicitly_wait(5)
    return driver


def login(driver):
    """
    type_user(drive)    ->  login google.
    """
    user_name = "dc4automationtest"
    login_page_1.get_user_textbox(driver).send_keys(user_name)
    login_page_1.get_next_button(driver).click()
    driver.implicitly_wait(20)
    password = "12345678x@X"
    password_field = login_page_2.get_password_textbox(driver)
    password_field.send_keys(password)
    element = login_page_2.get_login_button(driver)
    driver.execute_script("arguments[0].click();", element)
    return driver


if __name__ == "__main__":
    driver = access_google("firefox")
    driver = navigate_google_drive(driver)
    driver = login(driver)
