from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


#@pytest.mark.usefixtures("browser_launch")
def test_google_title(driver):
    driver.get("https://www.google.com")
    assert "Yahoo" in driver.title

#@pytest.mark.usefixtures("browser_launch")
def test_automation(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")
    assert "jenkins" in driver.title

