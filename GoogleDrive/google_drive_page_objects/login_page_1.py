"""This module provides web elements of login page."""


def get_user_textbox(driver):
    """The location of input user textbox."""
    return driver.find_element_by_xpath('//*[@id="identifierId"]')


def get_next_button(driver):
    """The location of the 'next' button."""
    return driver.find_element_by_xpath('//*[@id="identifierNext"]')
