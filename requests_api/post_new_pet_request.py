import json

from bases.rest_request_base import RestRequestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from enums.methods.methods_enum import MethodsEnum
from utils.utils import Utils
import jsons


class PostNewPetRequest(RestRequestBase):
    def __init__(self):
        super().__init__()
        self.method = MethodsEnum.POST.value
        self.request_server = "/v2/pet"

    # exemplo de método para setar json body por objeto
    def set_json_body(self, payload):
        self.json_body = Utils.convert_object_into_json(payload)

    # exemplo de método para setar json body por arquivo .json
    def set_json_body_from_file(self, id, category_id, category_name, name, photo_urls, tag_id, tag_name, status):
        with open("jsons/pet.json", "r") as file:
            payload = file.read()

        payload = payload \
            .replace("$id", id) \
            .replace("$categoryId", category_id) \
            .replace("$categoryName", category_name) \
            .replace("$name", name) \
            .replace("$photoUrls", photo_urls) \
            .replace("$tagId", tag_id) \
            .replace("$tagName", tag_name) \
            .replace("$status", status)

        self.json_body = payload

    # exemplo de método para setar json body por variável string
    def set_json_body_from_text(self, id, category_id, category_name, name, photo_urls, tag_id, tag_name, status):
        payload = """{
                  "id": $id,
                  "category": {
                    "id": $categoryId,
                    "name": "$categoryName"
                  },
                  "name": "$name",
                  "photoUrls": [
                    "$photoUrls"
                  ],
                  "tags": [
                    {
                      "id": $tagId,
                      "name": "$tagName"
                    }
                  ],
                  "status": "$status"
                }"""

        payload = payload \
            .replace("$id", id) \
            .replace("$categoryId", category_id) \
            .replace("$categoryName", category_name) \
            .replace("$name", name) \
            .replace("$photoUrls", photo_urls) \
            .replace("$tagId", tag_id) \
            .replace("$tagName", tag_name) \
            .replace("$status", status)

        self.json_body = payload


