import pytest
from selene import browser
import os
from appium import webdriver
import allure
import config
from utils import attach



@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = config.to_driver_options()

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(config.remote_url,
                                                 options=options)
        browser.config.timeout = float(os.getenv("TIMEOUT"))


    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)

    if config.runs_on_bstack:
        attach.add_video(browser)


    with allure.step('Close app session'):
        browser.quit()

