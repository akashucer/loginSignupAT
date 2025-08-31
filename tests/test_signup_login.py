import json
import allure
import pytest
from pages.signup_page import SignupPage
from pages.login_page import LoginPage
from utils.data_generator import generate_user
import time

#loading the JSON file
with open("utils/locators.json") as f:
    locators = json.load(f)

@pytest.fixture(scope="module")
def user_data():
    return generate_user()

@allure.feature("Signup")
@allure.description("Verify user is able to sign up successfully")
@pytest.mark.dependency()
def test_user_can_Register(driver, user_data):

    with allure.step("Initialize Signup Page"):
        signup_page = SignupPage(driver, locators)
        allure.attach(json.dumps(user_data, indent=4), name="User Data", attachment_type=allure.attachment_type.JSON)

    with allure.step("Open Signup Page"):
        signup_page.open("file:///Users/akashdeepsingh/Desktop/Ecommerce_app/index.html")
        allure.attach(driver.get_screenshot_as_png(), "Signup Page Opened", attachment_type=allure.attachment_type.PNG)

    with allure.step(f"Fill First Name: {user_data['First Name']}"):
        signup_page.enter_firstname(user_data["First Name"])

    with allure.step(f"Fill Last Name: {user_data['Last Name']}"):
        signup_page.enter_lastname(user_data["Last Name"])

    with allure.step(f"Fill Email: {user_data['Email']}"):
        signup_page.enter_email(user_data["Email"])

    with allure.step(f"Fill Phone Number: {user_data['Phone No']}"):
        signup_page.enter_phone(user_data["Phone No"])
    
    with allure.step(f"Fill Date of Birth: {user_data['DOB']}"):
        signup_page.enter_dob(user_data["DOB"])
        allure.attach(driver.get_screenshot_as_png(), "Personal Info Filled", attachment_type=allure.attachment_type.PNG)

    with allure.step(f"Fill Street Address: {user_data['Street Address']}"):
        signup_page.enter_streetadd(user_data["Street Address"])

    with allure.step(f"Fill City: {user_data['City']}"):
        signup_page.enter_city(user_data["City"])

    with allure.step(f"Fill State: {user_data['State']}"):
        signup_page.enter_state(user_data["State"])

    with allure.step(f"Fill Zip Code: {user_data['Zip Code']}"):
        signup_page.enter_zip(user_data["Zip Code"])

    with allure.step(f"Select Country: {user_data['Country']}"):
        signup_page.enter_country(user_data["Country"])
        allure.attach(driver.get_screenshot_as_png(), "Address Info Filled", attachment_type=allure.attachment_type.PNG)

    with allure.step(f"Fill Occupation: {user_data['Occupation']}"):
        signup_page.enter_occupation(user_data["Occupation"])

    with allure.step(f"Select Gender: {user_data['Gender']}"):
        signup_page.select_gender(user_data["Gender"])

    with allure.step("Fill Password and Confirm Password"):
        signup_page.enter_password(user_data["Password"])
        signup_page.enter_confirm_password(user_data["Password"])
        allure.attach(driver.get_screenshot_as_png(), "Password and Gender Filled", attachment_type=allure.attachment_type.PNG)

    with allure.step("Agree to Terms and Conditions"):
        signup_page.agree_terms()

    with allure.step("Submit Signup form"):
        signup_page.submit()

    with allure.step("Verify registration success"):
        assert signup_page.is_registration_successful(), "Registration was not successful"
        allure.attach(driver.get_screenshot_as_png(), "After Registration", attachment_type=allure.attachment_type.PNG)

@allure.feature("Login")
@allure.description("Verify registered user is able to login successfully")
@pytest.mark.dependency(depends=["test_user_can_Register"])
def test_user_can_login(driver, user_data):
    with allure.step("Initialize Login Page"):
        login_page = LoginPage(driver, locators)

    login_page.enter_email(user_data["Email"])
    login_page.enter_password(user_data["Password"])
    allure.attach(driver.get_screenshot_as_png(), name="Login Credentials Filled", attachment_type=allure.attachment_type.PNG)
    login_page.click_login()

    assert login_page.is_login_successful(), "Login was not successful"