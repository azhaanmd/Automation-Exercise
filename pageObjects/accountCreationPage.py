from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AccountCreationPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    accountCreatedText = (By.CSS_SELECTOR, "h2[data-qa='account-created']")
    continueButton = (By.CSS_SELECTOR, "a[data-qa='continue-button']")

    def getAccountCreatedText(self):
        return self.driver.find_element(*AccountCreationPage.accountCreatedText).text

    def getContinueButton(self):
        return self.driver.find_element(*AccountCreationPage.continueButton)


