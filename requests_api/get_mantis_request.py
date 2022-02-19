from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from utils.utils import Utils


class GetMantisRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.add_headers({'Authorization': '1uWBtLR_YsRgZiaYS-dGKVkj1Vfck32L'})
        self.url = "http://localhost:8989"
        self.method = "GET"
        self.request_server = "/api/rest/users/me"

