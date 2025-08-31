# Selenium Pytest UI Automation Framework

![Python](https://img.shields.io/badge/python-3.12-blue.svg)
![Pytest](https://img.shields.io/badge/pytest-8.3.5-blue.svg)
![Selenium](https://img.shields.io/badge/selenium-4.23.0-green.svg)
![Allure](https://img.shields.io/badge/allure-2.13.5-orange.svg)

This project is a robust UI test automation framework for a sample E-commerce web application, built with Python, Selenium, and Pytest. It follows the **Page Object Model (POM)** for maintainable and scalable tests and generates beautiful, interactive reports using **Allure**.

## Key Features

- **Page Object Model (POM)**: Ensures clean separation between test logic and UI interaction code, making the framework scalable and easy to maintain.
- **Data-Driven Testing**: Leverages the `Faker` library to generate dynamic, realistic test data for each test run, avoiding hardcoded values.
- **Detailed Reporting**: Integrates with `Allure Report` to provide rich, interactive HTML reports with step-by-step execution logs, screenshots on failure, and historical test data.
- **Dependency Management**: Uses `pytest-dependency` to create logical execution flows between tests, such as ensuring a user registration test passes before attempting a login test with the same user.
- **Centralized Locators**: Manages all UI element locators in a single `locators.json` file, making them easy to find and update.
- **Cross-Browser Ready**: The framework can be easily extended to run tests across different browsers like Chrome, Firefox, and Safari.

## Tech Stack

- **Core Language**: Python 3.x
- **Test Runner**: `pytest`
- **Browser Automation**: `selenium`
- **Reporting**: `allure-pytest`
- **Test Data**: `Faker`
- **Test Dependencies**: `pytest-dependency`

## Project Structure

```
.
├── pages/
│   ├── login_page.py       # Page Object for the Login Page
│   └── signup_page.py      # Page Object for the Signup Page
├── tests/
│   └── test_signup_login.py # Test cases for Signup and Login flows
├── utils/
│   ├── data_generator.py   # Utility to generate fake user data
│   └── locators.json       # Centralized UI locators
├── conftest.py             # Core Pytest fixtures (e.g., WebDriver setup)
├── index.html              # The local web application under test
├── pytest.ini              # Pytest configuration (e.g., custom markers)
└── requirements.txt        # Python package dependencies
```

## Getting Started

### Prerequisites

- Python 3.10+
- [Allure Commandline](https://allurereport.org/docs/gettingstarted-installation/) installed and available in your system's PATH.

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/akashucer/loginSignupAT.git
    cd loginSignupAT
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    # On Windows, use: .venv\Scripts\activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## Running Tests

### Execute Tests and Generate Report Data

Run the following command from the project root to execute all tests and clear any previous Allure results:

```bash
pytest --alluredir=reports --clean-alluredir
```

- `--alluredir=reports`: Specifies the directory to store Allure results.
- `--clean-alluredir`: Clears the report directory before the test run to ensure a fresh report.

### View the Allure Report

To generate and serve the HTML report, run:

```bash
allure serve reports
```

This command will open the interactive Allure Dashboard in your default web browser.

## Workflow Overview

1.  **Test Execution Starts**: `pytest` discovers and runs the tests in the `tests/` directory.
2.  **Driver Fixture**: The `conftest.py` file sets up the Selenium WebDriver instance, which is shared across tests in the module.
3.  **Data Generation**: The `user_data` fixture calls `generate_user()` from `utils/data_generator.py` to create a unique user for the test run.
4.  **Registration Test**: `test_user_can_Register` uses the `SignupPage` object to fill the registration form and submit it. It verifies success by checking for a confirmation alert.
5.  **Login Test**: `test_user_can_login` (which depends on the registration test) uses the `LoginPage` object and the *same user data* to perform a login and verify that the welcome message is displayed.
6.  **Driver Teardown**: After all tests in the module complete, the driver fixture quits the browser.
7.  **Report Generation**: Allure captures the results, steps, and attachments to create the final HTML report.
