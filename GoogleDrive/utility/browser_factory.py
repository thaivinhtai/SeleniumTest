"""This module help create the webdriver."""

from selenium import webdriver
from os import environ
from .tools import get_full_path
from selenium.webdriver.chrome.options import Options



def get_firefox():
    """This function establish firefox browser."""
    environ["webdriver.gecko.driver"] = get_full_path("./resource/geckodriver")
    return webdriver.Firefox()


def get_chrome():
    """This function establish chrome browser."""
    chromedriver = get_full_path("./resource/chromedriver")
    opts = Options()
    opts.binary_location = "/bin/google-chrome-stable"
    environ["webdriver.chrome.driver"] = chromedriver
    return webdriver.Chrome(chrome_options=opts,
                            executable_path=chromedriver)


def get_browser(name):
    """This function is used for quick selection of browser."""
    switcher = {
        "firefox": get_firefox,
        "chrome": get_chrome
    }
    func = switcher.get(name)
    return func()
