from time import sleep
from selenium.webdriver.support.color import Color
from utilities.BaseClass import BaseClass
from pageObjects.homePage import HomePage

class TestAssessment(BaseClass):
    def test_full_flow(self):
        homePage = HomePage(self.driver)
        homeButtonColor = homePage.getHomeButton().value_of_css_property("color")
        print(homeButtonColor)
        homePage.getItem().click()
        homePage.continueShopping().click()
        homePage.getCart().click()

        sleep(5)