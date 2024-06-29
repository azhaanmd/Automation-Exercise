import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="class")
def browserSetup(request):
    chrome_service_obj = Service("chromedriver.exe")
    driver = webdriver.Chrome(service=chrome_service_obj)
    driver.get("http://automationexercise.com")
    request.cls.driver = driver

