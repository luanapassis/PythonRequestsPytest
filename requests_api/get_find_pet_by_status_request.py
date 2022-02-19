import json

from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from utils.utils import Utils


class GetFindPetByStatusRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.add_query_parameters({'status': 'sold'})
        self.method = "GET"
        self.request_server = "/v2/pet/findByStatus"


