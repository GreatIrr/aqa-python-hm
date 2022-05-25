from steps.standardsteps import StandardSteps
from views import bothomeview


class BotHomeViewSteps(StandardSteps):
    __bot_home_view = bothomeview.BotHomeView()

    def verify_app_status(self):
        self.__bot_home_view.verify_app_status('dummy-aqa-app')

    def check_is_view_active(self):
        self._is_view_active(self.__bot_home_view)
