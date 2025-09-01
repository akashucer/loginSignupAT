import allure
import pytest
from selenium import webdriver
import platform
import sys
import os

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def save_environment_info(config):
    """Saves environment information to an Allure properties file."""
    allure_dir = config.getoption('--alluredir')
    if not allure_dir:
        return
    
    # Ensure the directory exists
    if not os.path.exists(allure_dir):
        os.makedirs(allure_dir)
    
    with open(os.path.join(allure_dir, "environment.properties"), "w") as f:
        f.write(f"Browser=Chrome\n")
        f.write(f"Browser.Version=Latest\n")
        f.write(f"OS={platform.system()} {platform.release()}\n")
        f.write(f"Python.Version={sys.version.split(' ')[0]}\n")

@pytest.fixture(scope="session", autouse=True)
def setup(request):
    """Set up test environment and save info."""
    save_environment_info(request.config)
    # Yield to allow other fixtures and tests to run
    yield