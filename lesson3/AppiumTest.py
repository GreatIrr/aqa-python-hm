from appium import webdriver

from View import SettingsView

print("before desired caps")

desired_capabilities = {
    "platformName": "iOS",
    "platformVersion": "12.5.5",
    "deviceName": "iPhone 6",
    "app": "",
    "udid": "98c0e343a64b454500e81ee035740c8d212e6bfb",
    "noReset": "true",
    "derivedDataPath": "/Users/bartnytskairyna/Git/aqa-mobile-ring/build/wda/98c0e343a64b454500e81ee035740c8d212e6bfb/WebDriverAgent",
    "automationName": "XCuiTest"
}

print("initing driver")

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities)

print("finished driver")

driver.activate_app("com.apple.Preferences")
# driver.find_element_by_ios_predicate("type=='XCUIElementTypeCell' and name=='Wi-Fi'").click()

settings_view = SettingsView(driver)

wifi_element_text = settings_view.get_current_wifi_text()

print("i got next text " + wifi_element_text)

assert "ZTE" == wifi_element_text, f"{wifi_element_text} is unexpected"

driver.quit()
