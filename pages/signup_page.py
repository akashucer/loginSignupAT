from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class SignupPage:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators["signup"]

    def open(self, url):
        self.driver.get(url)
        self.driver.find_element(By.XPATH, self.locators["createAccount"]).click()
    

    def enter_firstname(self, name):
        self.driver.find_element(By.ID, self.locators["FirstName"]).send_keys(name)

    def enter_lastname(self, name):
        self.driver.find_element(By.ID, self.locators["LastName"]).send_keys(name)

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.locators["Email"]).send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(By.ID, self.locators["Phone"]).send_keys(phone)
    
    def enter_dob(self, dob):
        self.driver.find_element(By.ID, self.locators["DOB"]).send_keys(dob)

    def enter_streetadd(self, streetadd):
        self.driver.find_element(By.ID, self.locators["StreetAddress"]).send_keys(streetadd)

    def enter_city(self, city):
        self.driver.find_element(By.ID, self.locators["City"]).send_keys(city)

    def enter_state(self, state):
        self.driver.find_element(By.ID, self.locators["State"]).send_keys(state)

    def enter_zip(self, zip):
        self.driver.find_element(By.ID, self.locators["Zip"]).send_keys(zip)

    def enter_country(self, country):
        self.driver.find_element(By.ID, self.locators["Country"]).send_keys(country)

    def enter_occupation(self, occupation):
        self.driver.find_element(By.ID, self.locators["Occupation"]).send_keys(occupation)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.locators["Password"]).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(By.ID, self.locators["ConfirmPassword"]).send_keys(password)

    def select_gender(self, gender):
        select = Select(self.driver.find_element(By.ID, self.locators["Gender"]))
        select.select_by_visible_text(gender)

    def agree_terms(self):
        self.driver.find_element(By.ID, self.locators["Terms"]).click()

    def submit(self):
        self.driver.find_element(By.ID, self.locators["Submit"]).click()
