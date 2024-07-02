from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    deliveryAddress = (By.CSS_SELECTOR, "ul[id='address_delivery']")
    billingAddress = (By.CSS_SELECTOR, "ul[id='address_invoice']")
    messageTextArea = (By.NAME, "message")
    placeOrderButton = (By.XPATH, "//a[contains(text(), 'Place Order')]")

    def getDeliveryAddressDetails(self):
        deliveryDetails = []
        deliveryAddressList = self.driver.find_element(*CheckoutPage.deliveryAddress)
        deliveryAddressItems = deliveryAddressList.find_elements(By.TAG_NAME, "li")
        for item in deliveryAddressItems:
            deliveryDetails.append(item.text)
        return deliveryDetails

    def getBillingAddressDetails(self):
        billingDetails = []
        billingAddressList = self.driver.find_element(*CheckoutPage.billingAddress)
        billingAddressItems = billingAddressList.find_elements(By.TAG_NAME, "li")
        for item in billingAddressItems:
            billingDetails.append(item.text)
        return billingDetails

    def getMessage(self, comment):
        return self.driver.find_element(*CheckoutPage.messageTextArea).send_keys(comment)

    def getPlaceOrderButton(self):
        return self.driver.find_element(*CheckoutPage.placeOrderButton)







