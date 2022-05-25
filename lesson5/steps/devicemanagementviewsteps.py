from steps.standardsteps import StandardSteps
from views import devicemanagementview


class DeviceManagementViewSteps(StandardSteps):
    __device_management_view = devicemanagementview.DeviceManagementView()

    def click_bot_home(self):
        self.__device_management_view.click_bot_home()

    def check_is_view_active(self):
        self._is_view_active(self.__device_management_view)
