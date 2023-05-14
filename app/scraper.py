import time


def click_something(driver, by, element_identifier):
    time.sleep(1)
    driver.find_element(by, element_identifier).click()


def write_something(driver, by, element_identifier, text):
    time.sleep(1)
    driver.find_element(by, element_identifier).send_keys(text)
