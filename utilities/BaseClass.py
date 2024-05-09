import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:

    def select_a_dropdown_by_text(self, text):
        dd = Select(self.driver.find_element(By.XPATH, "//select[@id='exampleFormControlSelect1']"))
        dd.select_by_visible_text(text)

    def waitUntilElementDisplayed(self, locator):
        wait = WebDriverWait(self.driver, 6)
        wait.until(expected_conditions.visibility_of_element_located(
            (By.XPATH, locator)))

