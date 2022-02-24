from bases.rest_request_base import RestRequestBase
from enums.methods.methods_enum import MethodsEnum


class GetCookiesRequest(RestRequestBase):
    def __init__(self):
        super().__init__()
        self.add_cookies({'location': 'New York'})
        self.url = "https://httpbin.org"
        self.method = MethodsEnum.GET.value
        self.request_server = "/cookies"



