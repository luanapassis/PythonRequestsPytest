import json

from bases.rest_request_base import RestRequestBase
from enums.methods.methods_enum import MethodsEnum


class GetFindPetByStatusRequest(RestRequestBase):
    def __init__(self):
        super().__init__()
        self.add_query_parameters({'status': 'sold'})
        self.method = MethodsEnum.GET.value
        self.request_server = "/v2/pet/findByStatus"


