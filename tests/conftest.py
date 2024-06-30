import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="class")
def browserSetup(request):
    chrome_service_obj = Service("chromedriver.exe")
    chrome_options = Options()
    chrome_options.page_load_strategy = "eager"
    driver = webdriver.Chrome(service=chrome_service_obj, options=chrome_options)
    driver.get("http://automationexercise.com")
    request.cls.driver = driver

