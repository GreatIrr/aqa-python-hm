from appium.webdriver.common.appiumby import AppiumBy

from util.helpers import swipe_and_click_element
from views.standardview import StandardView


class SettingsView(StandardView):

    def __init__(self):
        super().__init__()

    def is_active(self):
        return self._driver.find_element(AppiumBy.IOS_PREDICATE, self._title_locator % 'Settings').is_displayed()

    def scroll_and_click_title(self, cell):
        swipe_and_click_element(self._driver, self._driver.find_element(AppiumBy.IOS_PREDICATE, self._cell_locator % cell))
