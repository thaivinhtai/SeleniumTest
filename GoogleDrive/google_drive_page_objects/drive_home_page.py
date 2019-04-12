"""This module provides web elements of google drive home page."""


def get_access_buton(driver):
    """The location of access google drive buton."""
    return driver.find_element_by_xpath("/html/body/section/div[2]/div/a")
