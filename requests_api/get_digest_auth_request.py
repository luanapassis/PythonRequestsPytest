from bases.rest_request_base import RestRequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from enums.methods.methods_enum import MethodsEnum


class GetDigestAuthRequest(RestRequestBase):
    def __init__(self):
        super().__init__()
        self.url = "https://postman-echo.com"
        self.method = MethodsEnum.GET.value
        self.request_server = "/digest-auth"
        self.authentication_type = AuthenticationEnum.DIGEST.value
