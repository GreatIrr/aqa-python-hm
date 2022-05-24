from abc import abstractmethod
from appium.webdriver.common.appiumby import AppiumBy

import Driver
from Helpers import swipe_and_click_element


class StandardView:
    _title = "type in {'XCUIElementTypeOther', 'XCUIElementTypeStaticText'} and name=='%s'"
    _cell = "type=='XCUIElementTypeCell' and name=='%s'"

    def __init__(self):
        self._driver = Driver.AppiumDriver().get_driver()

    @abstractmethod
    def is_active(self):
        return False

    def get_driver(self):
        return self._driver

    def scroll_and_click_title(self, cell):
        swipe_and_click_element(self._driver, self._driver.find_element(AppiumBy.IOS_PREDICATE, self._cell % cell))

    def quit(self):
        self._driver.quit()


class SettingsView(StandardView):

    def __init__(self):
        super().__init__()

    def is_active(self):
        return self._driver.find_element(AppiumBy.IOS_PREDICATE, self._title % 'Settings').is_displayed()


class GeneralView(StandardView):

    def __init__(self):
        super().__init__()

    def is_active(self):
        return self._driver.find_element(AppiumBy.IOS_PREDICATE, self._title % 'General').is_displayed()


class DeviceManagementView(StandardView):

    def __init__(self):
        super().__init__()

    def is_active(self):
        return self._driver.find_element(AppiumBy.IOS_PREDICATE, self._title % 'Device Management').is_displayed()

    def click_bot_home(self):
        self._driver.find_element(AppiumBy.IOS_PREDICATE, "name like 'Bot*'").click()


class BotHomeView(StandardView):

    def __init__(self):
        super().__init__()

    def is_active(self):
        return self._driver.find_element(AppiumBy.IOS_PREDICATE,
                                         self._title % 'Bot Home Automation, Inc.').is_displayed()

    def verify_app_status(self, app_name):
        return self._driver.find_element(AppiumBy.XPATH,
                                         "//*[@name='%s']/following-sibling::XCUIElementTypeStaticText" % app_name) \
                   .text == "Verified"
