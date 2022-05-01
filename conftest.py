import pytest
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope='class')
def i():
    options = Options()
    options.add_experimental_option("prefs", {
        "download.default_directory": r"download",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })
    capabilities = DesiredCapabilities.CHROME
    capabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
    driver = webdriver.Chrome(desired_capabilities=capabilities,
                              chrome_options=options)
    driver.maximize_window()
    yield driver
    driver.close()
    driver.quit()

