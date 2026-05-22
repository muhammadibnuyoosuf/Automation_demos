from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import allure


@pytest.mark.usefixtures("driver")
def test_google_title():
    driver.get("https://www.google.com")
    assert "Yahoo" in driver.title

@pytest.mark.usefixtures("driver")
def test_automation():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    assert "jenkins" in driver.title

