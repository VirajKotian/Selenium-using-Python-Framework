from selenium.webdriver.common.by import By

from PageObjects.ConfirmPage import ConfirmPage


class CheckOutpage:

    phones = (By.XPATH, "//div[@class='card h-100']")
    productname =(By.XPATH, "div/h4/a")
    blueberry = (By.XPATH, "div/button")
    add = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    checkout = (By.XPATH, "//button[@class='btn btn-success']")


    def __init__(self, driver):     #The Driver argument to extracted from Parent classTestOne() as imported this class there
        self.driver = driver        #we declare driver as a variable

    def phones1(self):
        Phones = self.driver.find_elements(*CheckOutpage.phones)
        print(len(Phones))
        for Blackberry in Phones:
            ProductName = Blackberry.find_element(*CheckOutpage.productname).text


            if ProductName == "Blackberry":
                return Blackberry.find_element(*CheckOutpage.blueberry).click()
        print(Blackberry.text)


    def Add1(self):
        return self.driver.find_element(*CheckOutpage.add)

    def CheckOut1(self):
        self.driver.find_element(*CheckOutpage.checkout).click()
        confirmpage = ConfirmPage(self.driver)
        return confirmpage

















