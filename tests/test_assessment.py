from time import sleep
import pytest
from selenium.webdriver.support.color import Color
from utilities.BaseClass import BaseClass
from pageObjects.homePage import HomePage
from pageObjects.cartPage import CartPage
from pageObjects.registerLoginPage import RegisterLoginPage
from pageObjects.signupPage import SignupPage

class TestAssessment(BaseClass):
    @pytest.fixture(autouse=True)
    def setup(self):
        self.homePage = HomePage(self.driver)
        self.cartPage = CartPage(self.driver)
        self.registerLoginPage = RegisterLoginPage(self.driver)
        self.signupPage = SignupPage(self.driver)

    def test_verify_home_page_visibility(self):
        homeButtonColor = self.homePage.getHomeButton().value_of_css_property("color")
        print(homeButtonColor)

    def test_verify_add_product_and_cart_page_is_displayed(self):
        self.homePage.getItem().click()
        self.homePage.continueShopping().click()
        self.homePage.getCart().click()
        txt = self.cartPage.getShoppingCartText().text
        if txt == "Shopping Cart":
            assert self.cartPage.getProceedToCheckoutButton().is_displayed();

    def test_verify_account_created_after_checkout(self):
        self.cartPage.getProceedToCheckoutButton().click()

        self.cartPage.getRegisterLoginLink().click()
        self.registerLoginPage.fillSignupForm("AZTestsdf", "User@usser")
        self.registerLoginPage.getSignupButton().click()

    def test_verify_account_created_test(self):

        self.signupPage.fillSignUpFullForm(True, "nameee", "aa@aaaa.com", "1234aaaa", "8", "May", "1998", True, "firstname", "lastname",
                                      "company", "address", "address2", "Australia", "State", "City", "ZipCode", "MobileNumber")
        self.signupPage.getCreateAccountButton().click()
        sleep(20)