from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators["signup"]
        self.wait = WebDriverWait(driver, 10)

    def _find_element(self, locator):
        """Helper method to find element based on locator type"""
        if locator.startswith("//"):
            return self.wait.until(EC.presence_of_element_located((By.XPATH, locator)))
        elif locator.startswith("id:"):
            return self.wait.until(EC.presence_of_element_located((By.ID, locator.split(":", 1)[1])))
        else:
            return self.wait.until(EC.presence_of_element_located((By.ID, locator)))

    def open(self, url):
        self.driver.get(url)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.locators["createAccount"]))).click()

    def enter_firstname(self, name):
        self._find_element(self.locators["FirstName"]).send_keys(name)

    def enter_lastname(self, name):
        self._find_element(self.locators["LastName"]).send_keys(name)

    def enter_email(self, email):
        self._find_element(self.locators["Email"]).send_keys(email)

    def enter_phone(self, phone):
        self._find_element(self.locators["PhoneNo"]).send_keys(phone)
    
    def enter_dob(self, dob):
        self._find_element(self.locators["DOB"]).send_keys(dob)

    def enter_streetadd(self, streetadd):
        self._find_element(self.locators["streetAdd"]).send_keys(streetadd)

    def enter_city(self, city):
        self._find_element(self.locators["City"]).send_keys(city)

    def enter_state(self, state):
        self._find_element(self.locators["State"]).send_keys(state)

    def enter_zip(self, zip):
        self._find_element(self.locators["zipCode"]).send_keys(zip)

    def enter_country(self, country):
        element = self._find_element(self.locators["Country"])
        select = Select(element)
        select.select_by_visible_text(country)

    def enter_occupation(self, occupation):
        self._find_element(self.locators["Occupation"]).send_keys(occupation)

    def enter_password(self, password):
        self._find_element(self.locators["Password"]).send_keys(password)

    def enter_confirm_password(self, password):
        confirm_field = self._find_element(self.locators["confirmPassword"])
        self.driver.execute_script("arguments[0].value = arguments[1];", confirm_field, password)
        # Trigger change event to ensure validation works
        self.driver.execute_script("arguments[0].dispatchEvent(new Event('change'))", confirm_field)

    def select_gender(self, gender):
        # Click the select element first
        gender_select = self._find_element(self.locators["Gender"])
        self.driver.execute_script("arguments[0].click();", gender_select)
        
        # Select the option using Select class
        select = Select(gender_select)
        select.select_by_value(gender.lower())

    def agree_terms(self):
        self._find_element(self.locators["termsAndConditions"]).click()

    def submit(self):
        self._find_element(self.locators["createAccount"]).click()
