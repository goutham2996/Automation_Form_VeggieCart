import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="Chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    browser = request.config.getoption("--browser_name")
    if browser == "Chrome":
        ser_obj = Service("D:\Softwares\chromedriver-win64\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=ser_obj)
        driver.maximize_window()
    elif browser == "Edge":
        ser_obj = Service("D:\Softwares\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=ser_obj)
        driver.maximize_window()
    else:
        print("Ayyoo")
    request.cls.driver = driver
    yield
    driver.close()


