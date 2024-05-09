from selenium.webdriver.common.by import By


class ShopPage:

    def __init__(self, driver):
        self.driver = driver

    add_Cart = (By.XPATH, "//img[@alt='Cart']")
    sec_but = (By.XPATH, "//button[normalize-space()='PROCEED TO CHECKOUT']")
    pc_text = (By.XPATH, "//input[@placeholder='Enter promo code']")
    applyCode = (By.XPATH, "//button[@class='promoBtn']")
    place_order = (By.XPATH, "//button[normalize-space()='Place Order']")
    check_box = (By.XPATH, "//input[@type='checkbox']")
    proceed_button = (By.XPATH, "//button[normalize-space()='Proceed']")


    def proceedButton(self):
        return self.driver.find_element(*ShopPage.proceed_button)
    def addCart(self):
        return self.driver.find_element(*ShopPage.add_Cart)

    def secBut(self):
        return self.driver.find_element(*ShopPage.sec_but)

    def pcText(self):
        return self.driver.find_element(*ShopPage.pc_text)

    def appCode(self):
        return self.driver.find_element(*ShopPage.applyCode)

    def placeOrder(self):
        return self.driver.find_element(*ShopPage.place_order)

    def checkBox(self):
        return self.driver.find_element(*ShopPage.check_box)