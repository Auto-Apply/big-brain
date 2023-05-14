import time
from selenium.webdriver import Chrome


def click_something(driver: Chrome, by: str, element_identifier: str) -> None:
    time.sleep(1)
    driver.find_element(by, element_identifier).click()


def write_something(
    driver: Chrome, by: str, element_identifier: str, text: str
) -> None:
    time.sleep(1)
    driver.find_element(by, element_identifier).send_keys(text)
