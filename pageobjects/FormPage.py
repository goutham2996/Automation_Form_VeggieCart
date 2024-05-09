from selenium.webdriver.common.by import By


class FormPage:

    def __init__(self, driver):
        self.driver = driver

    user_name = (By.XPATH, "//div[@class='form-group']//input[@name='name']")
    user_email = (By.XPATH, "//input[@name='email']")
    user_password = (By.XPATH, "//input[@id='exampleInputPassword1']")
    checkBox = (By.XPATH, "//input[@id='exampleCheck1']")
    emp_status = (By.XPATH, "//input[@id='inlineRadio1']")
    dob = (By.XPATH, "//input[@name='bday']")
    submit_button = (By.XPATH, "//input[@value='Submit']")
    shopLink = (By.XPATH, "//a[normalize-space()='Shop']")

    def getName(self):
        return self.driver.find_element(*FormPage.user_name)
    def getEmail(self):
        return self.driver.find_element(*FormPage.user_email)

    def getPassword(self):
        return self.driver.find_element(*FormPage.user_password)

    def clickCheckBox(self):
        return self.driver.find_element(*FormPage.checkBox)

    def clickemployeeStatus(self):
        return self.driver.find_element(*FormPage.emp_status)

    def sendDOB(self):
        return self.driver.find_element(*FormPage.dob)

    def clickSubmit(self):
        return self.driver.find_element(*FormPage.submit_button)

    def clickShopLink(self):
        return self.driver.find_element(*FormPage.shopLink)

