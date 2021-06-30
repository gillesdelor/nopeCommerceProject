from selenium import webdriver
import pytest


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
        print("Launching Chrome browser.......................")
    elif browser == "firefox":
        driver = webdriver.Chrome()
        print("Launching Firefox browser.......................")
    else:
        driver = webdriver.Ie()
        print("Launching Internet Explorer browser..............")
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the browser value to setup method
    return request.config.getoption("--browser")


############################### Pytest HTML Report  ##########################
def pytest_configure(config):
    config._metadata["Project Name"] = "nope Commerce"
    config._metadata["Module Name"] = "Customers"
    config._metadata["Tester"] = "Zannou"


# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
