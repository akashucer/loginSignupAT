🔹 Workflow

POM → pages/ folder keeps all locators + actions.

Faker → utils/data_generator.py generates random data (name, email, gender).

Pytest Fixtures → conftest.py creates driver instance, attaches screenshots on failure, integrates with allure.

Tests → use page objects + faker data.

Allure → generate HTML reports with steps, screenshots, logs.