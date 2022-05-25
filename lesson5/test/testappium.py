import steps.settingsteps
import steps.generalviewsteps
import steps.devicemanagementviewsteps
import steps.bothomeviewsteps


def test_dummy_app():
    settings_steps = steps.settingsteps.SettingsViewSteps()
    general_steps = steps.generalviewsteps.GeneralViewSteps()
    device_management_steps = steps.devicemanagementviewsteps.DeviceManagementViewSteps()
    bot_home_steps = steps.bothomeviewsteps.BotHomeViewSteps()

    settings_steps.get_driver().activate_app("com.apple.Preferences")
    settings_steps.check_is_view_active()
    settings_steps.scroll_and_click_general_title()

    general_steps.check_is_view_active()
    general_steps.scroll_and_click_device_management_title()

    device_management_steps.check_is_view_active()
    device_management_steps.click_bot_home()

    bot_home_steps.check_is_view_active()
    bot_home_steps.verify_app_status()

    bot_home_steps.get_driver().terminate_app('com.apple.Preferences')
    bot_home_steps.get_driver().quit()

