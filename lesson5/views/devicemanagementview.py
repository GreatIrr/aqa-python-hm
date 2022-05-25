from appium.webdriver.common.appiumby import AppiumBy

from util.helpers import swipe_and_click_element
from views.standardview import StandardView


class DeviceManagementView(StandardView):

    def __init__(self):
        super().__init__()

    def is_active(self):
        return self._driver.find_element(AppiumBy.IOS_PREDICATE, self._title_locator % 'Device Management').is_displayed()

    def click_bot_home(self):
        self._driver.find_element(AppiumBy.IOS_PREDICATE, "name like 'Bot*'").click()

    def scroll_and_click_title(self, cell):
        swipe_and_click_element(self._driver, self._driver.find_element(AppiumBy.IOS_PREDICATE, self._cell_locator % cell))


