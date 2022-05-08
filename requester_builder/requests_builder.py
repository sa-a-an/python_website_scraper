
from requester_builder.requester_builder_interface import IRequesterBuilder

import requests as r


class RequestsBuilder(IRequesterBuilder):
    
    def __init__(self) -> None:
        self._response_object = None
    
    def request_get(self, url: str) -> None:
        self._response_object = r.get(url)
    
    def get_html_page(self) -> str:
        html = self._response_object.text
        return html
    
    def request_and_get_html_page(self, url: str) -> str:
        self._response_object = r.get(url)
        html = self._response_object.text
        return html
        