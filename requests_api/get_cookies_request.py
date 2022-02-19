from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from utils.utils import Utils


class GetCookiesRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.add_cookies({'location': 'New York'})
        self.url = "https://httpbin.org"
        self.method = "GET"
        self.request_server = "/cookies"



