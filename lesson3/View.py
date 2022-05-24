from appium.webdriver.common.appiumby import AppiumBy


class SettingsView:
    def __init__(self, driver):
        self.driver = driver

        self.wifi_locator = "type=='XCUIElementTypeCell' and name=='Wi-Fi'"
        self.current_wifi_locator = "type == 'XCUIElementTypeStaticText' and name !='Wi-Fi'"

    def get_current_wifi_text(self):
        wifi_element = self.driver.find_element(AppiumBy.IOS_PREDICATE, self.wifi_locator)
        return wifi_element.find_element(AppiumBy.IOS_PREDICATE, self.current_wifi_locator).text

      
