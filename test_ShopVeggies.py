import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageobjects.ShopPage import ShopPage
from utilities.BaseClass import BaseClass


class TestShopVeggies(BaseClass):

    def test_shopveggies(self):
        url = "https://rahulshettyacademy.com/seleniumPractise/#/"

        self.driver.get(url)
        shopPage = ShopPage(self.driver)
        list_of_veggies = self.driver.find_elements(By.XPATH, "//div[@class='product']")
        for i in list_of_veggies:
            veggies = i.find_element(By.XPATH, "h4").text
            if "Cucumber" in veggies:
                i.find_element(By.XPATH, "div/button").click()

        shopPage.addCart().click()
        shopPage.secBut().click()
        self.waitUntilElementDisplayed("//input[@placeholder='Enter promo code']")
        shopPage.pcText().send_keys("rahulshettyacademy")
        shopPage.appCode().click()
        self.waitUntilElementDisplayed("//span[@class='promoInfo']")
        shopPage.placeOrder().click()
        self.waitUntilElementDisplayed("//div[@class='wrapperTwo']//div//select")
        dd = Select(self.driver.find_element(By.XPATH, "//div[@class='wrapperTwo']//div//select"))
        dd.select_by_visible_text("India")
        shopPage.checkBox().click()
        shopPage.proceedButton().click()
        self.driver.get_screenshot_as_file('Ordered successfully.png')
