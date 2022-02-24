from bases.rest_request_base import RestRequestBase
from enums.methods.methods_enum import MethodsEnum


class GetCookiesRemovingRequest(RestRequestBase):
    def __init__(self):
        super().__init__()
        #remove se estiver pre definido na request base
        #self.remove_cookies('location')
        self.url = "https://httpbin.org"
        self.method = MethodsEnum.GET.value
        self.request_server = "/cookies"

