import allure

from enums.authentication.authentication_enum import AuthenticationEnum
from utils.allure_utils import AllureUtils
from utils.request_utils import RequestUtils
from utils.utils import Utils


class SoapRequestBase:

    def __init__(self):
        # Inicialização dos valores comuns a todas as requisições
        self.url = Utils.read_enviroment_key_json("base_url")
        self.method = ""
        self.xml_body = None
        self.headers = {'Content-Type': 'text/xml'}
        self.authentication_type = AuthenticationEnum.NONE.value

    @allure.step("RequestSoap")
    def execute_soap_request(self):
        response = RequestUtils.execute_soap_request(self.method, self.url, self.headers, self.xml_body,
                                                     self.authentication_type)

        AllureUtils.allure_log_soap_requests(self.url, self.xml_body, self.method, self.headers)
        AllureUtils.allure_log_soap_responses(response.status_code, response.headers, response.text, response)

        return response

    def add_headers(self, l_headers):
        self.headers.update(l_headers)

    def remove_headers(self, header):
        # recebe apenas a key
        self.headers.pop(header)
