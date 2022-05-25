import logging

from appium.webdriver import WebElement

log = logging.getLogger("helpers")


def swipe_until_element_is_displayed(driver, element):
    log.debug("Going to start scrolling to element")
    for i in range(5):
        if element.is_displayed():
            log.info("Element is visible")
            break
        else:
            driver.swipe(1, 200, 1, 1) # very reliable solution, I know


def swipe_and_click_element(driver, element: WebElement):
    swipe_until_element_is_displayed(driver, element)
    log.info(f"Element {element.text} is found, going to click")
    element.click()
