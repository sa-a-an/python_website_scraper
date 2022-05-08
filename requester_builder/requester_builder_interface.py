from abc import ABCMeta, abstractmethod

class IRequesterBuilder(metaclass = ABCMeta):
    """Interface for RequestBuilder class"""   
    
    @abstractmethod
    def request_get(self, url):
        """ Do get request to the page """

    @abstractmethod
    def get_html_page(self):
        """ Do get request to the page """
        
    @abstractmethod
    def request_and_get_html_page(self,url):
        """Make get request and return html page"""