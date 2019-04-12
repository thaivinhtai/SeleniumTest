"""This module provides web elements of google home page."""


def get_list_apps(driver):
    """The location of input google apps."""
    return driver.find_element_by_xpath("/html/body/div/div[3]/div[1]/div" +
                                        "/div/div/div[2]/div[1]/div[1]/a")


def get_drive(driver):
    """The location of google drive."""
    return driver.find_element_by_xpath("/html/body/div/div[3]/div[1]" +
                                        "/div/div/div/div[2]/div[1]/div[2]" +
                                        "/ul[1]/li[7]/a/span[1]")


def get_search_box(driver):
    """The location of search textbox."""
    return driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]" +
                                        "/div/div[1]/div/div[1]/input")


def get_visit_first_page(driver):
    """The location of the "I'm Feeling Lucky" button."""
    return driver.find_element_by_xpath("/html/body/div/div[3]/form/div[2]" +
                                        "/div/div[3]/center/input[2]")
