import pytest
import inspect
import logging
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


#As this Parent class have knowledge about the fixtures the child class Extracting BaseClass will also hav it
@pytest.mark.usefixtures("Setup")
class BaseClass:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger.setLevel(logging.DEBUG)
        return logger

    def VerifyLinkPresence(self, text):
        Wait = WebDriverWait(self.driver, 10)
        Wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))  # Remember the 3 Bracket Mistake

    def SelectOptionByText(self, locator, index, text):
        DropDown = Select(locator)
        DropDown.select_by_index(index)                          # Here Index 0 for Male   1 for Female
        DropDown.select_by_visible_text(text)


