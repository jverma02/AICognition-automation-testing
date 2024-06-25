import pytest
from selenium import webdriver
from selenium.webdriver.chrome import options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--password")
    parser.addoption("--username")
  

@pytest.fixture(scope='function')
def password():
 password1 = "Vvedansh$20244"
 return password1

@pytest.fixture(scope='function')
def username():
 username1 = "jverma02"
 return username1
    
