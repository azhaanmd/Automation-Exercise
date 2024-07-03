import random
import string
from time import sleep
import pytest
from utilities.BaseClass import BaseClass
from pageObjects.homePage import HomePage
from pageObjects.cartPage import CartPage
from pageObjects.registerLoginPage import RegisterLoginPage
from pageObjects.signupPage import SignupPage
from pageObjects.accountCreationPage import AccountCreationPage
from pageObjects.checkoutPage import CheckoutPage
from pageObjects.paymentPage import PaymentPage

class TestAssessment(BaseClass):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.homePage = HomePage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.registerLoginPage = RegisterLoginPage(self.driver)
        self.signupPage = SignupPage(self.driver)
        self.accountCreatedPage = AccountCreationPage(self.driver)
        self.checkoutPage = CheckoutPage(self.driver)
        self.paymentPage = PaymentPage(self.driver)
        self.driver.implicitly_wait(10)

    def test_verify_home_page_visibility(self):
        homeButtonColor = self.homePage.getHomeButton().value_of_css_property("color")
        slider_visible = self.homePage.getSlider().is_displayed()
        assert homeButtonColor == "rgba(66, 139, 202, 1)" and slider_visible


    def test_verify_add_product_and_cart_page_is_displayed(self):
        self.homePage.getItem().click()
        self.homePage.continueShopping().click()
        self.homePage.getCart().click()
        shoppingCartText = self.cartPage.getShoppingCartText().text
        if shoppingCartText == "Shopping Cart":
            assert self.cartPage.getProceedToCheckoutButton().is_displayed();

    def test_verify_account_created_after_checkout(self):
        self.cartPage.getProceedToCheckoutButton().click()
        self.cartPage.getRegisterLoginLink().click()
        res = ''.join(random.choices(string.ascii_lowercase +
                                     string.digits, k=10))
        random_email = str(res) + "@az112233test.com"
        self.registerLoginPage.fillSignupForm("oldddddd", random_email)
        self.registerLoginPage.getSignupButton().click()
        self.isMale = True
        self.fullAddress = ["firstname", "lastname", "company", "address", "address2", "Australia", "State", "City", "ZipCode", "MobileNumber"]
        self.signupPage.fillSignUpFullForm(self.isMale, "oldddddd", "1234aaaa", "8", "May", "1998", True, self.fullAddress[0], self.fullAddress[1],
                                      self.fullAddress[2], self.fullAddress[3], self.fullAddress[4], self.fullAddress[5], self.fullAddress[6],
                                           self.fullAddress[7], self.fullAddress[8], self.fullAddress[9])

        self.signupPage.getCreateAccountButton().click()
        accountCreatedText = self.accountCreatedPage.getAccountCreatedText()
        assert "ACCOUNT CREATED!" in accountCreatedText
        self.accountCreatedPage.getContinueButton().click()

    def test_verify_logged_in_as_username(self):
        loggedInUserText = self.homePage.getLoggedInUser()
        assert "Logged in as oldddddd" in loggedInUserText

    def test_verify_address_details(self):
        self.homePage.getCart().click()
        self.cartPage.getProceedToCheckoutButton().click()
        deliveryAddress = self.checkoutPage.getDeliveryAddressDetails()
        billingAddress = self.checkoutPage.getBillingAddressDetails()
        deliveryAddress.pop()
        billingAddress.pop()
        if deliveryAddress == billingAddress:
            if self.checkoutPage.checkAddressIsSame(deliveryAddress, self.fullAddress, self.isMale):
                assert "Address Verified"
        else:
            print("Address mismatched")

    def test_verify_payment_details_and_payment_confirmation(self):
        self.checkoutPage.getMessage("This is a comment")
        self.checkoutPage.getPlaceOrderButton().click()
        self.paymentPage.enterPaymentDetails("azhaan", "1234", "311", "05", "1998")
        self.paymentPage.getPayConfirmButton().click()
        sleep(5)
        self.driver.back()
        paymentConfirmationMessage = self.paymentPage.getPaymentConfirmationMessage()
        print("\n" + paymentConfirmationMessage)
        assert "Your order has been placed successfully!" in paymentConfirmationMessage

