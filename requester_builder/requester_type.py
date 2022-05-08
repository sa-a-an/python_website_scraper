from enum import Enum

class RequesterType(Enum):
    """
        Types of requests
    """
    REQUEST_BUILD_WITH_PARAMS = 1
    REQUESTS = 2
    SELENIUM = 3
    
