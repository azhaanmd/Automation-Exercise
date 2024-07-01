import pytest
from selenium.webdriver.support.ui import Select


@pytest.mark.usefixtures("browserSetup")
class BaseClass:
    def selectOptionByText(self, locator, text):
        print(locator)
        sel = Select(self.driver.find_element(*locator))
        sel.select_by_visible_text(text)