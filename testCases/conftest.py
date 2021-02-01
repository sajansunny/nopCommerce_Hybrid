import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path=".\\Configurations\\Drivers\\chromedriver.exe")
        print("Launching Chrome browser..")
    elif browser == "firefox":
        driver = webdriver.Firefox(executable_path=".\\Configurations\\Drivers\\geckodriver.exe")
        print("Launching Firefox browser..")
    else:
        driver = webdriver.Ie(executable_path=".\\Configurations\\Drivers\\IEDriverServer.exe")
        print("Launching IE browser..")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")