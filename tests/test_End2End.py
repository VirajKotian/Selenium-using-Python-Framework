#Every Test we Run must be in Pytest Standards for this Framework
#Its a good Practice to wrap all the test cases(Methods/Functions) in class and anything under class use self keyword
import time
import pytest
from webbrowser import get

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects import CheckOutPage
from PageObjects.HomePage import HomePage
from TestData.HomePageData import HomePageData
from utilities.BaseClass import BaseClass

class Test_HomeSubmit(BaseClass):                   #Import it as this child class will also hav the knowledge about the Fixture()
                                                    # check utilities -->BaseClass.py
    def test_HomePageSubmission(self, getData):
        log = self.getLogger()
        homePage = HomePage(self.driver)       #we need driver as an Arg to be send in Homepage class and Constructor will recognise it
        homePage.name1().send_keys(getData["Firstname"])
        log.info("first name is " +getData["Firstname"])
        homePage.email1().send_keys(getData["email"])
        log.info("email name is " +getData["email"])
        homePage.password1().send_keys(getData["password"])
        log.info("password is " +str(getData["password"]))
        homePage.check1().click()


        homePage.student1().click()
        homePage.date1().send_keys("24-05-2001")
        #log.info("Date of birth "+getData["DOB"])
        homePage.input1().send_keys("Message")
        log.info("Input msg " +getData["Message"])
        homePage.cleartext1().clear()


        self.SelectOptionByText(homePage.Gender1(), 0, "Female")
        # DropDown.select_by_value()                                    #For Value Dropdown
        self.driver.refresh()
        time.sleep(2)

    @pytest.fixture(params=HomePageData.getTestdata("Testcase2"))
    def getData(self, request):                              #we can use self.driver.refesh() method also
        return request.param                                 # request parameter/object to send data to browser
                                                             # We are Using Dictionary method {key : value }

    # @pytest.fixture(params=HomePageData.test_HomePage_data)
    # def getData(self, request):                              #we can use self.driver.refesh() method also
    #     return request.param                                 # request parameter/object to send data to browser
    # # We are Using Dictionary method {key : value }


class TestOne(BaseClass):
    def test_End2End(self):
        log = self.getLogger()
        homePage = HomePage(self.driver)
        homePage.submit1().click()

        message = homePage.alert1()
        print(message)
        assert "Success" in message

        checkoutpage = homePage.shopitems()
        log.info("Getting all the Card Info")
        checkoutpage.phones1()

        checkoutpage.Add1().click()

        confirmPage =  checkoutpage.CheckOut1()
        log.info("Entering Country name as ind")
        confirmPage.Country1().send_keys("ind")

        self.VerifyLinkPresence("India")

        confirmPage.Search1().click()

        confirmPage.CheckBox1().click()
        confirmPage.Purchased1().click()

        SuccessMsg = confirmPage.Success1()
        log.info("Text recieved" +SuccessMsg)
        assert "Success! Thank you!" in SuccessMsg
        # self.driver.close()        #no need as we hav Already mentioned in fixture
        time.sleep(2)




