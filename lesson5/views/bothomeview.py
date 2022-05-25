from appium.webdriver.common.appiumby import AppiumBy

from views.standardview import StandardView


class BotHomeView(StandardView):

    def __init__(self):
        super().__init__()

    def is_active(self):
        return self._driver.find_element(AppiumBy.IOS_PREDICATE,
                                         self._title_locator % 'Bot Home Automation, Inc.').is_displayed()

    def verify_app_status(self, app_name):
        return self._driver.find_element(AppiumBy.XPATH,
                                         "//*[@name='%s']/following-sibling::XCUIElementTypeStaticText" % app_name) \
                   .text == "Verified"
