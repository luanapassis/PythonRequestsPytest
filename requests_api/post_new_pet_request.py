import json

from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from utils.utils import Utils


class PostNewPetRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.method = "POST"
        self.request_server = "/v2/pet"

    def set_json_body(self, payload):
        self.json_body = json.dumps(payload, default=lambda x: x.__dict__)

