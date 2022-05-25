import logging

from util import driver
from views.standardview import StandardView


class StandardSteps:

    log = logging.getLogger(__name__)

    @staticmethod
    def _is_view_active(view: StandardView):
        StandardSteps.log.info("Checking if view %s is active" % view.__class__.__name__)
        assert view.is_active() is True, "View %s is not active" % view.__class__.__name__

    @staticmethod
    def get_driver():
        return driver.AppiumDriver().get_driver()

