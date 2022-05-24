import logging

import Driver
from views import Views
from views.Views import StandardView


class StandardSteps:

    log = logging.getLogger(__name__)

    @staticmethod
    def _is_view_active(view: StandardView):
        StandardSteps.log.info("Checking if view %s is active" % view.__class__.__name__)
        assert view.is_active() is True, "View %s is not active" % view.__class__.__name__

    @staticmethod
    def get_driver():
        return Driver.AppiumDriver().get_driver()


class SettingsViewSteps(StandardSteps):
    __settings_view = Views.SettingsView()

    def scroll_and_click_general_title(self):
        self.__settings_view.scroll_and_click_title('General')

    def check_is_view_active(self):
        self._is_view_active(self.__settings_view)


class GeneralViewSteps(StandardSteps):
    __general_view = Views.GeneralView()

    def scroll_and_click_device_management_title(self):
        self.__general_view.scroll_and_click_title('Device Management')

    def check_is_view_active(self):
        self._is_view_active(self.__general_view)


class DeviceManagementViewSteps(StandardSteps):
    __device_management_view = Views.DeviceManagementView()

    def click_bot_home(self):
        self.__device_management_view.click_bot_home()

    def check_is_view_active(self):
        self._is_view_active(self.__device_management_view)


class BotHomeViewSteps(StandardSteps):
    __bot_home_view = Views.BotHomeView()

    def verify_app_status(self):
        self.__bot_home_view.verify_app_status('dummy-aqa-app')

    def check_is_view_active(self):
        self._is_view_active(self.__bot_home_view)

