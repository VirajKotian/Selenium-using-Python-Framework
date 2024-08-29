#For Page Object Design Pattern Eg for Shop page a separate class must be created to dedicated consider that page only
#Similarly for Checkout page we will create separate class and put all the Objects in it. #for 5 pages 5 different class
from selenium.webdriver.common.by import By

from PageObjects.CheckOutPage import CheckOutpage


class HomePage:
    name = (By.NAME, "name")          #Variable should be small its a tuple
    email = (By.NAME, "email")
    password = (By.ID, "exampleInputPassword1")
    check = (By.ID, "exampleCheck1")
    student = (By.XPATH, "//input[@id='inlineRadio1']")
    date = (By.CSS_SELECTOR, "input[max='3000-12-31']")
    input = (By.XPATH, "(//input[@type='text'])[3]")
    cleartext = (By.XPATH, "(//input[@type='text'])[3]")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    alert = (By.CLASS_NAME,"alert")
    shop = (By.CSS_SELECTOR, "a[href*='shop']")


    def __init__(self, driver):     #The Driver argument to extracted from Parent classTestOne() as imported this class there
        self.driver = driver        #we declare driver as a variable

    def name1(self):
        return self.driver.find_element(*HomePage.name)      #Important to put "*" as it will consider/treat the variable as Tuple and deserialise it
         # driver.find_element(By.NAME, "name")             #To Understand the difference between class variable(we use Classname.obj)
                                                         #and Instance variable(self.)
    def email1(self):
        return self.driver.find_element(*HomePage.email)

    def password1(self):
        return self.driver.find_element(*HomePage.password)

    def check1(self):
        return self.driver.find_element(*HomePage.check)

    def student1(self):
        return self.driver.find_element(*HomePage.student)

    def date1(self):
        return self.driver.find_element(*HomePage.date)

    def input1(self):
        return self.driver.find_element(*HomePage.input)

    def cleartext1(self):
        return self.driver.find_element(*HomePage.cleartext)

    def Gender1(self):
        return self.driver.find_element(*HomePage.gender)

    def submit1(self):
        return self.driver.find_element(*HomePage.submit)

    def alert1(self):
        message = self.driver.find_element(*HomePage.alert).text
        print(message)
        assert "Success" in message
        return message

    def shopitems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutpage(self.driver)
        return checkOutPage
















