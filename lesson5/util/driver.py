from appium import webdriver
from appium.webdriver.webdriver import WebDriver


class AppiumDriver:

    class __WebDriver:
        def __init__(self):
            desired_capabilities = {
                "platformName": "iOS",
                "platformVersion": "12.5.5",
                "deviceName": "iPhone 6",
                "app": "",
                "udid": "98c0e343a64b454500e81ee035740c8d212e6bfb",
                "noReset": "true",
                "derivedDataPath": "/Users/bartnytskairyna/Git/aqa-mobile-ring/build/wda/98c0e343a64b454500e81ee035740c8d212e6bfb/WebDriverAgent",
                "automationName": "XCuiTest"
            }
            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

    __driver = None

    def __init__(self):
        if not AppiumDriver.__driver:
            AppiumDriver.__driver = AppiumDriver.__WebDriver().driver

    def get_driver(self) -> WebDriver:
        return self.__driver

    @staticmethod
    def quit_driver():
        if AppiumDriver.__driver is not None:
            AppiumDriver.__driver.quit()
