from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    shoppingCartText = (By.CSS_SELECTOR, "li[class='active']")
    proceedToCheckoutButton = (By.CSS_SELECTOR, ".check_out")
    registerLoginLink = (By.CSS_SELECTOR, "p a[href*='/login']")

    def getShoppingCartText(self):
        return self.driver.find_element(*CartPage.shoppingCartText)

    def getProceedToCheckoutButton(self):
        return self.driver.find_element(*CartPage.proceedToCheckoutButton)

    def getRegisterLoginLink(self):
        #self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable(CartPage.registerLoginLink))