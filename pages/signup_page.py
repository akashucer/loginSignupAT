from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


class SignupPage:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators["signup"]
        self.wait = WebDriverWait(driver, 20)

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
        element = self._find_element(self.locators["DOB"])
        self.driver.execute_script("arguments[0].value = arguments[1];", element, dob)

    def enter_streetadd(self, streetadd):
        self._find_element(self.locators["streetAdd"]).send_keys(streetadd)

    def enter_city(self, city):
        self._find_element(self.locators["City"]).send_keys(city)

    def enter_state(self, state):
        self._find_element(self.locators["State"]).send_keys(state)

    def enter_zip(self, zip_code):
        self._find_element(self.locators["zipCode"]).send_keys(zip_code)

    def enter_country(self, country):
        element = self._find_element(self.locators["Country"])
        select = Select(element)
        select.select_by_visible_text(country)

    def enter_occupation(self, occupation):
        self._find_element(self.locators["Occupation"]).send_keys(occupation)

    def enter_password(self, password):
        elem = self._find_element(self.locators["Password"])
        elem.clear()
        elem.send_keys(password)

    def enter_confirm_password(self, password):
        elem = self._find_element(self.locators["confirmPassword"])
        elem.clear()
        elem.send_keys(password)

    def select_gender(self, gender):
        element = self._find_element(self.locators["Gender"])
        select = Select(element)
        select.select_by_value(gender.lower())

    def agree_terms(self):
        element = self._find_element(self.locators["termsAndConditions"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def submit(self):
        element = self._find_element(self.locators["submitButton"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_registration_successful(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            if alert.text == 'Registration successful! You can now login with your credentials.':
                alert.accept()
                # After accepting the alert, the page should show the login form.
                # We need to wait for the login section to be visible.
                login_section = self.wait.until(
                    EC.visibility_of_element_located((By.ID, "loginSection"))
                )
                return login_section.is_displayed()
            else:
                # If alert text is wrong, accept it anyway to not block the browser
                alert.accept()
                return False
        except TimeoutException:
            # This means the alert did not appear in time.
            return False

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
        element = self._find_element(self.locators["DOB"])
        self.driver.execute_script("arguments[0].value = arguments[1];", element, dob)

    def enter_streetadd(self, streetadd):
        self._find_element(self.locators["streetAdd"]).send_keys(streetadd)

    def enter_city(self, city):
        self._find_element(self.locators["City"]).send_keys(city)

    def enter_state(self, state):
        self._find_element(self.locators["State"]).send_keys(state)

    def enter_zip(self, zip_code):
        self._find_element(self.locators["zipCode"]).send_keys(zip_code)

    def enter_country(self, country):
        element = self._find_element(self.locators["Country"])
        select = Select(element)
        select.select_by_visible_text(country)

    def enter_occupation(self, occupation):
        self._find_element(self.locators["Occupation"]).send_keys(occupation)

    def enter_password(self, password):
        elem = self._find_element(self.locators["Password"])
        elem.clear()
        elem.send_keys(password)

    def enter_confirm_password(self, password):
        elem = self._find_element(self.locators["confirmPassword"])
        elem.clear()
        elem.send_keys(password)

    def select_gender(self, gender):
        element = self._find_element(self.locators["Gender"])
        select = Select(element)
        select.select_by_value(gender.lower())

    def agree_terms(self):
        element = self._find_element(self.locators["termsAndConditions"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def submit(self):
        element = self._find_element(self.locators["submitButton"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_registration_successful(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            if alert.text == 'Registration successful! You can now login with your credentials.':
                alert.accept()
                # After accepting the alert, the page should show the login form.
                # We need to wait for the login section to be visible.
                login_section = self.wait.until(
                    EC.visibility_of_element_located((By.ID, "loginSection"))
                )
                return login_section.is_displayed()
            else:
                # If alert text is wrong, accept it anyway to not block the browser
                alert.accept()
                return False
        except TimeoutException:
            # This means the alert did not appear in time.
            return False

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
        element = self._find_element(self.locators["DOB"])
        self.driver.execute_script("arguments[0].value = arguments[1];", element, dob)

    def enter_streetadd(self, streetadd):
        self._find_element(self.locators["streetAdd"]).send_keys(streetadd)

    def enter_city(self, city):
        self._find_element(self.locators["City"]).send_keys(city)

    def enter_state(self, state):
        self._find_element(self.locators["State"]).send_keys(state)

    def enter_zip(self, zip_code):
        self._find_element(self.locators["zipCode"]).send_keys(zip_code)

    def enter_country(self, country):
        element = self._find_element(self.locators["Country"])
        select = Select(element)
        select.select_by_visible_text(country)

    def enter_occupation(self, occupation):
        self._find_element(self.locators["Occupation"]).send_keys(occupation)

    def enter_password(self, password):
        elem = self._find_element(self.locators["Password"])
        elem.clear()
        elem.send_keys(password)

    def enter_confirm_password(self, password):
        elem = self._find_element(self.locators["confirmPassword"])
        elem.clear()
        elem.send_keys(password)

    def select_gender(self, gender):
        element = self._find_element(self.locators["Gender"])
        select = Select(element)
        select.select_by_value(gender.lower())

    def agree_terms(self):
        element = self._find_element(self.locators["termsAndConditions"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def submit(self):
        element = self._find_element(self.locators["submitButton"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_registration_successful(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            if alert.text == 'Registration successful! You can now login with your credentials.':
                alert.accept()
                # After accepting the alert, the page should show the login form.
                # We need to wait for the login section to be visible.
                login_section = self.wait.until(
                    EC.visibility_of_element_located((By.ID, "loginSection"))
                )
                return login_section.is_displayed()
            else:
                # If alert text is wrong, accept it anyway to not block the browser
                alert.accept()
                return False
        except TimeoutException:
            # This means the alert did not appear in time.
            return False

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
        element = self._find_element(self.locators["DOB"])
        self.driver.execute_script("arguments[0].value = arguments[1];", element, dob)

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
        elem = self._find_element(self.locators["Password"])
        elem.clear()
        elem.send_keys(password)

    def enter_confirm_password(self, password):
        elem = self._find_element(self.locators["confirmPassword"])
        elem.clear()
        elem.send_keys(password)

    def select_gender(self, gender):
        element = self._find_element(self.locators["Gender"])
        select = Select(element)
        select.select_by_value(gender.lower())

    def agree_terms(self):
        element = self._find_element(self.locators["termsAndConditions"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def submit(self):
        element = self._find_element(self.locators["submitButton"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_registration_successful(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            if alert.text == 'Registration successful! You can now login with your credentials.':
                alert.accept()
                # After accepting the alert, the page should show the login form.
                # We need to wait for the login section to be visible.
                login_section = self.wait.until(
                    EC.visibility_of_element_located((By.ID, "loginSection"))
                )
                return login_section.is_displayed()
            else:
                # If alert text is wrong, accept it anyway to not block the browser
                alert.accept()
                return False
        except TimeoutException:
            # This means the alert did not appear in time.
            return False

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
        element = self._find_element(self.locators["DOB"])
        self.driver.execute_script("arguments[0].value = arguments[1];", element, dob)

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
        elem = self._find_element(self.locators["Password"])
        elem.clear()
        elem.send_keys(password)

    def enter_confirm_password(self, password):
        elem = self._find_element(self.locators["confirmPassword"])
        elem.clear()
        elem.send_keys(password)

    def select_gender(self, gender):
        element = self._find_element(self.locators["Gender"])
        select = Select(element)
        select.select_by_value(gender.lower())

    def agree_terms(self):
        element = self._find_element(self.locators["termsAndConditions"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def submit(self):
        element = self._find_element(self.locators["submitButton"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_registration_successful(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            if alert.text == 'Registration successful! You can now login with your credentials.':
                alert.accept()
                # After accepting the alert, the page should show the login form.
                # We need to wait for the login section to be visible.
                login_section = self.wait.until(
                    EC.visibility_of_element_located((By.ID, "loginSection"))
                )
                return login_section.is_displayed()
            else:
                # If alert text is wrong, accept it anyway to not block the browser
                alert.accept()
                return False
        except TimeoutException:
            # This means the alert did not appear in time.
            return False

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
        element = self._find_element(self.locators["DOB"])
        self.driver.execute_script("arguments[0].value = arguments[1];", element, dob)

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
        elem = self._find_element(self.locators["Password"])
        elem.clear()
        elem.send_keys(password)

    def enter_confirm_password(self, password):
        elem = self._find_element(self.locators["confirmPassword"])
        elem.clear()
        elem.send_keys(password)

    def select_gender(self, gender):
        element = self._find_element(self.locators["Gender"])
        select = Select(element)
        select.select_by_value(gender.lower())

    def agree_terms(self):
        element = self._find_element(self.locators["termsAndConditions"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def submit(self):
        element = self._find_element(self.locators["submitButton"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_registration_successful(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            if alert.text == 'Registration successful! You can now login with your credentials.':
                alert.accept()
                # After accepting the alert, the page should show the login form.
                # We need to wait for the login section to be visible.
                login_section = self.wait.until(
                    EC.visibility_of_element_located((By.ID, "loginSection"))
                )
                return login_section.is_displayed()
            else:
                # If alert text is wrong, accept it anyway to not block the browser
                alert.accept()
                return False
        except TimeoutException:
            # This means the alert did not appear in time.
            return False

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
        element = self._find_element(self.locators["DOB"])
        self.driver.execute_script("arguments[0].value = arguments[1];", element, dob)

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
        elem = self._find_element(self.locators["Password"])
        elem.clear()
        elem.send_keys(password)

    def enter_confirm_password(self, password):
        elem = self._find_element(self.locators["confirmPassword"])
        elem.clear()
        elem.send_keys(password)

    def select_gender(self, gender):
        element = self._find_element(self.locators["Gender"])
        select = Select(element)
        select.select_by_value(gender.lower())

    def agree_terms(self):
        element = self._find_element(self.locators["termsAndConditions"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def submit(self):
        element = self._find_element(self.locators["submitButton"])
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        self.driver.execute_script("arguments[0].click();", element)

    def is_registration_successful(self):
        try:
            alert = self.wait.until(EC.alert_is_present())
            if alert.text == 'Registration successful! You can now login with your credentials.':
                alert.accept()
                # After accepting the alert, the page should show the login form.
                # We need to wait for the login section to be visible.
                login_section = self.wait.until(
                    EC.visibility_of_element_located((By.ID, "loginSection"))
                )
                return login_section.is_displayed()
            else:
                # If alert text is wrong, accept it anyway to not block the browser
                alert.accept()
                return False
        except TimeoutException:
            # This means the alert did not appear in time.
            return False
