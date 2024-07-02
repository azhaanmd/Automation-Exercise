from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    item = (By.CSS_SELECTOR, "a[data-product-id='11']")
    continueShoppingButton = (By.CSS_SELECTOR, ".btn.btn-success.close-modal.btn-block")
    cartLink = (By.CSS_SELECTOR, "a[href*='/view_cart']")
    homeButton = (By.CSS_SELECTOR, "a[href*='/']")
    slider = (By.ID, "slider-carousel")
    loggedInText = (By.XPATH, "//*[contains(text(), 'Logged in')]")
    slider = (By.ID, "slider-carousel")

    def getHomeButton(self):
        return self.driver.find_element(*HomePage.homeButton)

    def getItem(self):
        return self.driver.find_element(*HomePage.item)

    def continueShopping(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(HomePage.continueShoppingButton))

    def getCart(self):
        return self.driver.find_element(*HomePage.cartLink)

    def getLoggedInUser(self):
        return self.driver.find_element(*HomePage.loggedInText).text

    def getSlider(self):
        return self.driver.find_element(*HomePage.slider)