from abc import abstractmethod
from appium.webdriver.common.appiumby import AppiumBy

from util import driver
from util.helpers import swipe_and_click_element


class StandardView:
    _title_locator = "type in {'XCUIElementTypeOther', 'XCUIElementTypeStaticText'} and name=='%s'"
    _cell_locator = "type=='XCUIElementTypeCell' and name=='%s'"

    def __init__(self):
        self._driver = driver.AppiumDriver().get_driver()

    @abstractmethod
    def is_active(self):
        return False

    def scroll_and_click_title(self, cell):
        swipe_and_click_element(self._driver,
                                self._driver.find_element(AppiumBy.IOS_PREDICATE, self._cell_locator % cell))

    def quit(self):
        self._driver.quit()

