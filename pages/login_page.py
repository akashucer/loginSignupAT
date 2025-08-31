import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver, locators):
        self.driver = driver
        self.locators = locators["Login"]
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Enter email: {email}")
    def enter_email(self, email):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.locators["Email"].split(":")[1]))).send_keys(email)

    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.locators["Password"].split(":")[1]))).send_keys(password)

    @allure.step("Click on login button")
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable((By.XPATH, self.locators["loginButton"]))).click()

    @allure.step("Verify if login is successful")
    def is_login_successful(self):
        try:
            welcome_message = self.wait.until(EC.visibility_of_element_located((By.ID, "welcomeMessage")))
            is_successful = "Welcome back" in welcome_message.text
            if is_successful:
                allure.attach(self.driver.get_screenshot_as_png(), name="Login Successful", attachment_type=allure.attachment_type.PNG)
            else:
                allure.attach(self.driver.get_screenshot_as_png(), name="Login Failed", attachment_type=allure.attachment_type.PNG)
            return is_successful
        except TimeoutException:
            allure.attach(self.driver.get_screenshot_as_png(), name="Login Failed - Timeout", attachment_type=allure.attachment_type.PNG)
            return False
