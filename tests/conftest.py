#If I want to run in chrome Browser in Command Prompt
#Give the Command as >> py.test --browser_name chrome            #firefox for Firefox browser
#But for above command to work for specific Browser we need to pass Command line option to select Browser or it will select Default Browser at RunTime
# #Got from Website official documentationcommand line options in pytest
# def pytest_addoption(parser):
#     parser.addoption(
#         "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
#     )
# @pytest.fixture(scope="class")
# def Setup(request):
#     return request.config.getoption("--cmdopt")
# check the edited one below after import

import pytest
import time
from selenium import webdriver

driver = None

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):        #if we want to use different Browser using command prompt run time Variable
    parser.addoption("--browser_name", action="store", default="chrome")       #If using firefox get the firefox value in fixture


@pytest.fixture(scope="class")
def Setup(request):
    global driver
    browser_name = request.config.getoption("--browser_name")         #To retrive Browser name
    if browser_name == "chrome":
        driver = webdriver.Chrome()      #We can also use service method and give the path to downloaded chrome driver


    elif browser_name == "firefox":
        driver = webdriver.Firefox()


    elif browser_name == "Edge":
        driver = webdriver.ChromiumEdge()

    driver.implicitly_wait(5)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver                   #Here Request is use to access the Driver obj in class
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
        driver.get_screenshot_as_file(name)