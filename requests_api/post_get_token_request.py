from bases.rest_request_base import RestRequestBase
from enums.methods.methods_enum import MethodsEnum


class PostGetTokenRequest(RestRequestBase):
    def __init__(self):
        super().__init__()
        self.url = "https://serverest.dev"
        self.method = MethodsEnum.POST.value
        self.request_server = "/login"

    def set_json_body_from_text(self, email, password):
        payload = """{
                      "email": "$email",
                      "password": "$password"
                    }"""

        payload = payload \
            .replace("$email", email) \
            .replace("$password", password)

        self.json_body = payload

