from .requester_builder_interface import IRequesterBuilder
import constants
from seleniumwire import webdriver

class SeleniumBuilder(IRequesterBuilder):
    def __init__(self, driver_path: str = None):
        self._driver_path = driver_path if driver_path is not None else constants.DRIVER_PATH
        self._driver = self.__create_driver_object()
        print(self._driver_path)
    
    def __create_driver_object(self):
        driver = webdriver.Chrome(
            executable_path=self._driver_path
        )
        return driver
    
    def request_get(self, url: str) -> None:
        self._driver.get(url)
    
    def get_html_page(self) -> str:
        html = self._driver.page_source
        return html
    
    def request_and_get_html_page(self, url: str) -> str:
        self._driver.get(url)
        html = self._driver.page_source
        return html