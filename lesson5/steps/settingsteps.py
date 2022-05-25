from steps.standardsteps import StandardSteps
from views import settingsview


class SettingsViewSteps(StandardSteps):
    __settings_view = settingsview.SettingsView()

    def scroll_and_click_general_title(self):
        self.__settings_view.scroll_and_click_title('General')

    def check_is_view_active(self):
        self._is_view_active(self.__settings_view)
