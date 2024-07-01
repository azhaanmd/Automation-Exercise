from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegisterLoginPage:
    def __init__(self, driver):
        self.driver = driver

    signupName = (By.CSS_SELECTOR, "input[data-qa='signup-name']")
    signupEmail = (By.CSS_SELECTOR, "input[data-qa='signup-email']")
    signupButton = (By.CSS_SELECTOR, "button[data-qa='signup-button']")

    def getSignupName(self, name):
        return self.driver.find_element(*RegisterLoginPage.signupName).send_keys(name)

    def getSignupEmail(self, email):
        return self.driver.find_element(*RegisterLoginPage.signupEmail).send_keys(email)

    def getSignupButton(self):
        return self.driver.find_element(*RegisterLoginPage.signupButton)

    def fillSignupForm(self, name, email):
        self.getSignupName(name)
        self.getSignupEmail(email)
