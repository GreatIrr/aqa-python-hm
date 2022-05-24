import logging

log = logging.getLogger("Helpers")


def swipe_until_element_is_displayed(driver, element):
    log.debug("Going to start scrolling to element")
    for i in range(5):
        if element.is_displayed():
            log.info("Element is visible")
            break
        else:
            driver.swipe(1, 200, 1, 1)


def swipe_and_click_element(driver, element):
    swipe_until_element_is_displayed(driver, element)
    log.info("Element is found, going to click")
    element.click()
