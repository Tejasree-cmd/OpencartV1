import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.firefox.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import os
from datetime import datetime

@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver=webdriver.Edge()
        return driver
    elif browser=='firefox':
        driver=webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        return driver
    else:
        driver = webdriver.Chrome()
        return driver

def pytest_addoption(parser):  # This will get the Value from CLI hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## Pytest HTML Report #################
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Opencart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

#Specifying report folder location and save report with timestamp
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config.option.htmlpath = ".\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"