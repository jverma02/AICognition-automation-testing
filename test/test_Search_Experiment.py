import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import logging
import sys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from test_aicog_login import test_login

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


def SearchExperiment():
   driver = webdriver.Chrome(chrome_options)
   driver.maximize_window()
     
   print("search experiment")
   prompt_discovery_tab = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/header/div[1]/div[2]')

 


 
     