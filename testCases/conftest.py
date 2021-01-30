import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver = webdriver.Chrome(executable_path=".\\Configurations\\Drivers\\chromedriver.exe")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

