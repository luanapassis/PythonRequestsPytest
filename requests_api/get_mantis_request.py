from bases.rest_request_base import RestRequestBase
from enums.methods.methods_enum import MethodsEnum


class GetMantisRequest(RestRequestBase):
    def __init__(self):
        super().__init__()
        self.add_headers({'Authorization': '1uWBtLR_YsRgZiaYS-dGKVkj1Vfck32L'})
        self.url = "http://localhost:8989"
        self.method = MethodsEnum.GET.value
        self.request_server = "/api/rest/users/me"


