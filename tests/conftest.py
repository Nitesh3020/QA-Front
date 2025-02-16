import pytest
import os
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
import chromedriver_binary  # Ensures chromedriver is in PATH
from utilities.custom_logger import customLogger

log = customLogger()
# Replacing yield_fixture with fixture for method-level setup
@pytest.fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")

# Fixture for setting up the WebDriver
@pytest.fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one-time setUp")
    baseURL = "https://www.letskodeit.com/"

    if browser == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        print("Running tests on Firefox")
    else:
        # Chrome options
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.set_capability("goog:loggingPrefs", {"performance": "ALL"})

        # ChromeDriver Service
        chromedriver_path = os.path.join(os.path.dirname(__file__), '../Driver/chromedriver.exe')
        chrome_service = ChromeService(chromedriver_path)

        # Initialize ChromeDriver
        driver = webdriver.Chrome(service=chrome_service, options=options)
        driver.maximize_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        print("Running tests on Chrome")

    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    # Log performance data before quitting the driver
    log.info("Retrieving performance logs before teardown...")
    try:
        performance_logs = driver.get_log("performance")
        save_performance_logs(performance_logs)
    except Exception as e:
        log.error(f"Error retrieving performance logs: {e}")

    driver.quit()
    print("Running one-time tearDown")


# Adding command-line options for browser
def pytest_addoption(parser):
    parser.addoption("--browser", help="Browser to run tests on (chrome or firefox)")


# Fixture to retrieve browser option from command line
@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")


def save_performance_logs(log_entries, output_file="performance_logs.json"):
    """
    Saves performance logs to a file for debugging or reporting.
    """
    try:
        logs = []
        for entry in log_entries:
            log_data = json.loads(entry["message"])
            logs.append(log_data)
        with open(output_file, "w") as f:
            json.dump(logs, f, indent=4)
        log.info(f"Performance logs saved to {output_file}")
    except Exception as e:
        log.error(f"Error saving performance logs: {e}")