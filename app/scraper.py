from typing import List
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager


class Scraper:
    driver: Chrome

    def find_something(self, by: str, element_identifier: str) -> bool:
        try:
            self.driver.find_element(by, element_identifier)
            return True
        except Exception:
            return False

    def click_something(self, by: str, element_identifier: str) -> None:
        self.driver.find_element(by, element_identifier).click()

    def write_something(
        self, by: str, element_identifier: str, text: str
    ) -> None:
        self.driver.find_element(by, element_identifier).send_keys(text)

    def scroll_down(
        self,
        num_scrolls: int,
    ) -> None:
        for _ in range(num_scrolls):
            self.driver.execute_script("window.scrollBy(0, {});".format(5))

    def load_url(self, url: str) -> None:
        self.driver.get(url)

    def get_shadow_root(self, container: WebElement) -> WebElement:
        span: WebElement = container.find_element(
            By.CSS_SELECTOR, ":first-child"
        )
        shadow_root: WebElement = self.driver.execute_script(
            "return arguments[0].shadowRoot", span
        )
        return shadow_root

    def __init__(self, arguments: List[str] = []) -> None:
        coptions = Options()

        # Setting scraper instance arguments
        coptions.add_argument("--lang=en_US")
        coptions.add_argument("--no-sandbox")
        coptions.add_argument("--disable-popup-blocking")
        coptions.add_argument("--disable-notifications")
        coptions.add_argument("--disable-infobars")
        coptions.add_argument("--disable-logging")
        coptions.add_argument("--disable-dev-shm-usage")
        coptions.add_argument("--disable-blink-features=AutomationControlled")
        coptions.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
        )
        for argument in arguments:
            coptions.add_argument(argument)

        # Setting experimental scraper instance arguments
        coptions.add_experimental_option("excludeSwitches", ["enable-logging"])

        self.driver = Chrome(
            service=Service(ChromeDriverManager().install()), options=coptions
        )
        self.driver.delete_all_cookies()
        self.load_url("https://tools.pingdom.com/")
