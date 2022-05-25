from steps.standardsteps import StandardSteps
from views import generalview


class GeneralViewSteps(StandardSteps):
    __general_view = generalview.GeneralView()

    def scroll_and_click_device_management_title(self):
        self.__general_view.scroll_and_click_title('Device Management')

    def check_is_view_active(self):
        self._is_view_active(self.__general_view)