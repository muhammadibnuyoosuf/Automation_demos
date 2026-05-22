from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


#@pytest.mark.usefixtures("browser_launch")
@pytest.mark.regression
def test_google_title1(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

#@pytest.mark.usefixtures("browser_launch")
@pytest.mark.regression
def test_automation2(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    assert "Login" in driver.title

#@pytest.mark.usefixtures("browser_launch")
@pytest.mark.smoke
def test_google_title3(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

#@pytest.mark.usefixtures("browser_launch")
@pytest.mark.sanity
def test_automation4(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    assert "Login" in driver.title

#@pytest.mark.usefixtures("browser_launch")
@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.sanity
def test_google_title5(driver):
    driver.get("https://www.google.com")
    assert "Google" in driver.title

#@pytest.mark.usefixtures("browser_launch")
@pytest.mark.sanity
def test_automation6(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    assert "Login" in driver.title
