from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


@pytest.fixture
def driver():

    driver = webdriver.Chrome()
    driver.maximize_window()

    yield driver

    driver.quit()


def test_google_title(driver):

    driver.get("https://www.google.com")

    try:
        assert "Yahoo" in driver.title

    except AssertionError:

        screenshot_path = "failure.png"

        driver.save_screenshot(screenshot_path)

        allure.attach.file(
            screenshot_path,
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )

        raise