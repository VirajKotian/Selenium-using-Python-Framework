from selenium.webdriver.common.by import By


class ConfirmPage:
     country = (By.ID, "country")
     search = (By.LINK_TEXT, "India")
     checkBox = (By.XPATH, "//label[@for='checkbox2']")
     purchased = (By.CSS_SELECTOR, "input[class='btn btn-success btn-lg']")
     success = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")



     def __init__(self, driver):
          self.driver = driver


     def Country1(self):
         return self.driver.find_element(*ConfirmPage.country)

     def Search1(self):
          return self.driver.find_element(*ConfirmPage.search)

     def CheckBox1(self):
          return self.driver.find_element(*ConfirmPage.checkBox)


     def Purchased1(self):
          return self.driver.find_element(*ConfirmPage.purchased)


     def Success1(self):
          SuccessMsg = self.driver.find_element(*ConfirmPage.success).text
          print(SuccessMsg)
          assert "Success! Thank you!" in SuccessMsg
          return SuccessMsg




