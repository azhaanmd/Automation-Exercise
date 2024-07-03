from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.BaseClass import BaseClass



class SignupPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    titleMaleRadioButton = (By.ID, "id_gender1")
    titleFemaleRadioButton = (By.ID, "id_gender2")
    nameField = (By.ID, "name")
    emailField = (By.ID, "email")
    passwordField = (By.ID, "password")
    dateDropdown = (By.ID, "days")
    monthDropdown = (By.ID, "months")
    yearDropdown = (By.ID, "years")
    newsletterCheckbox = (By.ID, "newsletter")
    firstNameField = (By.ID, "first_name")
    lastNameField = (By.ID, "last_name")
    companyField = (By.ID, "company")
    address1Field = (By.ID, "address1")
    address2Field = (By.ID, "address2")
    countryDropdown = (By.ID, "country")
    stateField = (By.ID, "state")
    cityField = (By.ID, "city")
    zipCodeField = (By.ID, "zipcode")
    mobileNumberField = (By.ID, "mobile_number")
    createAccountButton = (By.CSS_SELECTOR, "button[type='submit']")

    def getTitle(self, isMale):
        if isMale:
            return self.driver.find_element(*SignupPage.titleMaleRadioButton).click()
        else:
            return self.driver.find_element(*SignupPage.titleFemaleRadioButton).click()

    def getName(self, name):
        if self.driver.find_element(*SignupPage.nameField).get_attribute("value") == name:
            return
        else:
            self.driver.find_element(*SignupPage.nameField).clear()
            return self.driver.find_element(*SignupPage.nameField).send_keys(name)


    def getPassword(self, password):
        return self.driver.find_element(*SignupPage.passwordField).send_keys(password)

    def selectDate(self, date):
        self.selectOptionByText(SignupPage.dateDropdown, date)

    def selectMonth(self, month):
        self.selectOptionByText(SignupPage.monthDropdown, month)

    def selectYear(self, year):
        self.selectOptionByText(SignupPage.yearDropdown, year)

    def checkNewsletter(self, requireNewsletter):
        if requireNewsletter:
            return self.driver.find_element(*SignupPage.newsletterCheckbox).click()
        else:
            return

    def getFirstName(self, firstname):
        return self.driver.find_element(*SignupPage.firstNameField).send_keys(firstname)

    def getLastName(self, lastname):
        return self.driver.find_element(*SignupPage.lastNameField).send_keys(lastname)

    def getCompany(self, company):
        return self.driver.find_element(*SignupPage.companyField).send_keys(company)

    def gerAddress(self, address):
        return self.driver.find_element(*SignupPage.address1Field).send_keys(address)

    def getAddress2(self, address2):
        return self.driver.find_element(*SignupPage.address2Field).send_keys(address2)

    def selectCountry(self, country):
        self.selectOptionByText((SignupPage.countryDropdown), country)

    def getState(self, state):
        return self.driver.find_element(*SignupPage.stateField).send_keys(state)

    def getCity(self, city):
        return self.driver.find_element(*SignupPage.cityField).send_keys(city)

    def getZipCode(self, zipcode):
        return self.driver.find_element(*SignupPage.zipCodeField).send_keys(zipcode)

    def getMobileNumber(self, mobile):
        return self.driver.find_element(*SignupPage.mobileNumberField).send_keys(mobile)

    def fillSignUpFullForm(self, isMale, name, password, date, month, year, requireNewsletter,
                           firstname, lastname, company, address, address2, country, state, city, zipcode, mobile):
        self.getTitle(isMale)
        self.getName(name)
        self.getPassword(password)
        self.selectDate(date)
        self.selectMonth(month)
        self.selectYear(year)
        self.checkNewsletter(requireNewsletter)
        self.getFirstName(firstname)
        self.getLastName(lastname)
        self.getCompany(company)
        self.gerAddress(address)
        self.getAddress2(address2)
        self.selectCountry(country)
        self.getState(state)
        self.getCity(city)
        self.getZipCode(zipcode)
        self.getMobileNumber(mobile)

    def getCreateAccountButton(self):
        return self.driver.find_element(*SignupPage.createAccountButton)








