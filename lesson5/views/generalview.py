from appium.webdriver.common.appiumby import AppiumBy

from views.standardview import StandardView


class GeneralView(StandardView):

    def __init__(self):
        super().__init__()

    def is_active(self):
        return self._driver.find_element(AppiumBy.IOS_PREDICATE, self._title_locator % 'General').is_displayed()
