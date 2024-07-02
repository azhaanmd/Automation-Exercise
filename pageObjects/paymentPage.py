from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    nameOnCardField = (By.CSS_SELECTOR, "input[name='name_on_card']")
    cardNumberField = (By.CSS_SELECTOR, "input[name='card_number']")
    cvcField = (By.CSS_SELECTOR, "input[name='cvc']")
    expiryMonthField = (By.CSS_SELECTOR, "input[name='expiry_month']")
    expiryYearField = (By.CSS_SELECTOR, "input[name='expiry_year']")
    confirmationMessage = (By.CSS_SELECTOR, "div[id='success_message'] div.alert-success.alert")
    payConfirmButton = (By.CSS_SELECTOR, ".form-control.btn.btn-primary.submit-button")

    def enterPaymentDetails(self, name, number, cvc, month, year):
        self.driver.find_element(*PaymentPage.nameOnCardField).send_keys(name)
        self.driver.find_element(*PaymentPage.cardNumberField).send_keys(number)
        self.driver.find_element(*PaymentPage.cvcField).send_keys(cvc)
        self.driver.find_element(*PaymentPage.expiryMonthField).send_keys(month)
        self.driver.find_element(*PaymentPage.expiryYearField).send_keys(year)

    def getPaymentConfirmationMessage(self):
        return self.driver.find_element(*PaymentPage.confirmationMessage).text


    def getPayConfirmButton(self):
        return self.driver.find_element(*PaymentPage.payConfirmButton)


