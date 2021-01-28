import pytest
from selenium import webdriver

@pytest.fixture()
def setup():
    driver=webdriver.Chrome(executable_path="C:/Users/sajan/OneDrive/PycharmProjects/nopCommerce_Hybrid/Configurations/Drivers/chromedriver.exe")
    return driver

