from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum


class GetDigestAuthRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.url = "https://postman-echo.com"
        self.method = "GET"
        self.request_server = "/digest-auth"
        self.authentication_type = AuthenticationEnum.DIGEST.value
        self.authenticator_user = "postman"
        self.authenticator_password = "password"