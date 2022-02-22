from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from enums.methods.methods_enum import MethodsEnum


class GetBasicAuthRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.url = "https://postman-echo.com"
        self.method = MethodsEnum.GET.value
        self.request_server = "/basic-auth"
        self.authentication_type = AuthenticationEnum.BASIC.value

