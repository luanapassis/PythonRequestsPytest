from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum


class GetOauth1Request(RequestBase):
    def __init__(self):
        super().__init__()
        self.url = "https://postman-echo.com"
        self.method = "GET"
        self.request_server = "/oauth1"
        self.authentication_type = AuthenticationEnum.OAUTH1.value
        self.app_key = "RKCGzna7bv9YD57c"
        self.app_secret = "D+EdQ-gs$-%@2Nu7"
