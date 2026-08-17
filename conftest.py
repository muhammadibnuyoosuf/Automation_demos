import os

import pytest
from selenium import webdriver
import allure


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    if os.environ.get("HEADLESS", "").lower() in ("1", "true", "yes"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    if not options.arguments:
        driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(hookwrapper=True)

def pytest_runtest_makereport(item, call):

    outcome = yield

    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs['driver']

        screenshot_path = "failure.png"

        driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )