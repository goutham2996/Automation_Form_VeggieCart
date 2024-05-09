import time

from pageobjects.FormPage import FormPage
from utilities.BaseClass import BaseClass


class TestLoginForm(BaseClass):

    def test_logingform(self):
        url = "https://rahulshettyacademy.com/angularpractice/"
        user_name = "Goutham"
        user_email = "gautamspikee@gmail.com"
        user_password = "abc@123"
        gender = "Male"
        dob = "29081996"

        self.driver.get(url)
        formPage = FormPage(self.driver)
        formPage.getName().send_keys(user_name)
        formPage.getEmail().send_keys(user_email)
        formPage.getPassword().send_keys(user_password)
        formPage.clickCheckBox().click()
        self.select_a_dropdown_by_text(gender)
        formPage.clickemployeeStatus().click()
        formPage.sendDOB().send_keys(dob)
        formPage.clickSubmit().click()
        self.driver.execute_script("window.scrollTo(0,0);")
        self.waitUntilElementDisplayed("//div[@class='alert alert-success alert-dismissible']")
        self.driver.get_screenshot_as_file('Success1.png')
        formPage.clickShopLink().click()
        self.waitUntilElementDisplayed("//a[@class='nav-link btn btn-primary']")
        self.driver.get_screenshot_as_file('Success2.png')

