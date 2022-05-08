from urllib.request import Request

from requester_builder.requests_builder import RequestsBuilder
from .requester_builder_interface import IRequesterBuilder
from .requester_type import RequesterType
from .selenium_builder import SeleniumBuilder
from .requests_builder import RequestsBuilder
import constants

class RequesterFactory():

    @staticmethod
    def build_requester_generator(requester_type: RequesterType) -> IRequesterBuilder:
        if requester_type is None:
            raise AttributeError('Cannot create object from None')
        elif requester_type == RequesterType.REQUEST_BUILD_WITH_PARAMS:
            pass
        elif requester_type == RequesterType.SELENIUM:
            return SeleniumBuilder()
        elif requester_type == RequesterType.REQUESTS:
            return RequestsBuilder()
        