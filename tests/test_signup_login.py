import json
import allure
from pages.signup_page import SignupPage
from utils.data_generator import generate_user
import time

#loading the JSON file
with open("utils/locators.json") as f:
    locators = json.load(f)

@allure.feature("Signup")
@allure.description("Verify user is able to sign up successfully")
def test_user_can_Register(driver):
    signup_page = SignupPage(driver, locators)
    user_data = generate_user()
    with allure.step("Open Signup Page"):
        signup_page.open("file:///Users/akashdeepsingh/Desktop/Ecommerce_app/index.html")
        allure.attach(
            driver.get_screenshot_as_png(),
            "Signup Page",
            attachment_type = allure.attachment_type.PNG
        )

    with allure.step("Fill Signup form"):
        signup_page.enter_firstname(user_data["First Name"])
        signup_page.enter_lastname(user_data["Last Name"])
        signup_page.enter_email(user_data["Email"])
        signup_page.enter_phone(user_data["Phone No"])
        allure.attach(
            driver.get_screenshot_as_png(),
            "Signup Form Filled",
            attachment_type=allure.attachment_type.PNG
        )
        signup_page.enter_dob(user_data["DOB"])
        signup_page.enter_streetadd(user_data["Street Address"])
        signup_page.enter_city(user_data["City"])
        signup_page.enter_state(user_data["State"])
        signup_page.enter_zip(user_data["Zip Code"])
        signup_page.enter_country(user_data["Country"])
        signup_page.enter_occupation(user_data["Occupation"])
        password = user_data["Password"]
        signup_page.enter_password(password)
        signup_page.enter_confirm_password(password)  # Use the same password variable
        allure.attach(  # Using the same password
        
            driver.get_screenshot_as_png(),
            "Password Fields Filled",
            attachment_type=allure.attachment_type.PNG
        )
        signup_page.select_gender(user_data["Gender"])  # Using gender from user data
        signup_page.agree_terms()

    with allure.step("Submit Signup form"):
        allure.attach(
            driver.get_screenshot_as_png(),
            "Signup Form Submitted",
            attachment_type=allure.attachment_type.PNG
        )
        signup_page.submit()

    #with allure.step("Verify registration success message"):
     #   assert "success" in driver.page_source.lower()