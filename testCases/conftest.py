# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
#
# @pytest.fixture()
# def setup():
#     options = Options()  # ✅ Create a ChromeOptions instance
#     options.add_argument("--start-maximized")  # ✅ Open browser in maximized mode
#     options.add_argument("--disable-notifications")  # ✅ Disable pop-up notifications
#     options.add_argument("--ignore-certificate-errors")  # ✅ Ignore SSL certificate issues
#
#     service = Service(ChromeDriverManager().install())  # ✅ Correct way to install ChromeDriver
#     driver = webdriver.Chrome(service=service, options=options)  # ✅ Pass options correctly
#
#     yield driver
#     driver.quit()

import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

# ✅ Fixture to Set Up WebDriver Based on CLI Input
@pytest.fixture()
def setup(request):
    browser = request.config.getoption("--browser")  # Get browser value from CLI

    if browser == 'edge':
        driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        print("🚀 Launching Edge Browser")
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        print("🚀 Launching Firefox Browser")
    else:
        options = webdriver.ChromeOptions()
        options.add_argument("--ignore-certificate-errors")  # ✅ Bypass SSL errors
        options.add_argument("--disable-web-security")       # ✅ Disable web security warnings
        options.add_argument("--allow-running-insecure-content")  # ✅ Allow mixed content
        options.add_argument("--no-sandbox")  # ✅ Bypass OS security model
        options.add_argument("--disable-gpu")  # ✅ Disable GPU for stability
        options.add_argument("--disable-dev-shm-usage")  # ✅ Fix shared memory issues
        #options.add_argument("--incognito")  # ✅ Run in incognito mode
        #options.add_argument("--headless=new")  # ✅ Run in headless mode (optional)

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        print("🚀 Launching Chrome Browser with SSL Bypass")

    yield driver
    driver.quit()  # ✅ Close browser after test execution

# ✅ Get Browser Name from CLI
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, edge, firefox")

# ✅ Hook to Add Metadata to HTML Report
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # ✅ Store metadata correctly for Pytest 8+
    config.stash[pytest.StashKey[str]] = {
        "Project Name": "Magento_eCommerce",
        "Module Name": "User Account Creation Page",
        "Tester Name": "Manikandan"
    }

    # ✅ Create Reports Directory
    report_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(report_dir, exist_ok=True)  # ✅ Ensure the reports folder exists

    # ✅ Set HTML Report Path with Timestamp
    report_file = os.path.join(report_dir, datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".html")
    config.option.htmlpath = report_file

# ✅ Hook to Modify/Delete Metadata in HTML Report
@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    metadata = session.config.stash.get(pytest.StashKey[str], {})  # ✅ Fetch metadata safely
    if isinstance(metadata, dict):  # ✅ Ensure it's a dictionary
        metadata.pop("JAVA_HOME", None)
        metadata.pop("Plugins", None)



