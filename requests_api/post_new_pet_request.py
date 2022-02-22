import json

from bases.request_base import RequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from enums.methods.methods_enum import MethodsEnum
from utils.utils import Utils
import jsons


class PostNewPetRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.method = MethodsEnum.POST.value
        self.request_server = "/v2/pet"

    def set_json_body(self, payload):
        # self.json_body = json.dumps(payload, default=lambda x: x.__dict__)
        self.json_body = Utils.convert_object_into_json(payload)
        print("aqui--------------- com objeto")
        print(self.json_body)

    def set_json_body_from_file(self):
        with open("jsons/pet.json", "r") as file:
            payload = file.read()

        payload = payload\
             .replace("$id", "999") \
            .replace("$catetoryId", "88") \
            .replace("$categoryName", "cat name") \
            .replace("$name", "name doguinho") \
            .replace("$photoUrls", "fotinha") \
            .replace("$tagId", "1") \
            .replace("$tagName", "tag1") \
            .replace("$status", "diponivel")

        print("-------aqui---------")
        print(payload)

        self.json_body = payload
        print(self.json_body)
