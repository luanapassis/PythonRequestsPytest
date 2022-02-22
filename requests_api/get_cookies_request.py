from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from enums.methods.methods_enum import MethodsEnum
from utils.utils import Utils


class GetCookiesRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.add_cookies({'location': 'New York'})
        self.url = "https://httpbin.org"
        self.method = MethodsEnum.GET.value
        self.request_server = "/cookies"



