import allure

from enums.authentication.authentication_enum import AuthenticationEnum
from utils.allure_utils import AllureUtils
from utils.request_utils import RequestUtils
from utils.utils import Utils


class RequestBase:

    def __init__(self):
        self.url = Utils.read_enviroment_key_json("base_url")
        self.request_server = ""
        self.method = ""
        self.json_body = None
        self.headers = {'Content-Type': 'application/json'}
        self.cookies = {}
        self.query_parameters = {}
        self.authentication_type = AuthenticationEnum.NONE.value
        self.authenticator_user = ""
        self.authenticator_password = ""
        self.app_key = ""
        self.app_secret = ""
        self.user_oauth_token = ""
        self.user_oauth_token_secret = ""

    @allure.step("Request")
    def execute_request(self):
        response = RequestUtils.execute_request(self.method, self.url, self.request_server, self.headers,
                                                self.query_parameters, self.cookies, self.json_body,
                                                self.authentication_type)

        AllureUtils.allure_log_requests(self.url, self.request_server, self.query_parameters, self.json_body,
                                        self.method, self.headers, self.cookies)
        AllureUtils.allure_log_responses(response.status_code, response.headers, response.text, response)

        return response

    def add_headers(self, l_headers):
        # for key in l_headers:
        #     self.headers[key] = self.headers.get(key, l_headers[key])
        self.headers.update(l_headers)

    def add_cookies(self, l_cookies):
        # for key in l_cookies:
        #     self.cookies[key] = self.cookies.get(key, l_cookies[key])
        self.cookies.update(l_cookies)

    def add_query_parameters(self, l_query_parameters):
        # for key in l_query_parameters:
        #     self.query_parameters[key] = self.query_parameters.get(key, l_query_parameters[key])
        self.query_parameters.update(l_query_parameters)

    def remove_headers(self, hearder):
        # recebe apenas a key
        self.headers.pop(hearder)

    def remove_cookies(self, cookie):
        # recebe apenas a key
        self.cookies.pop(cookie)

    def remove_parameters(self, parameter):
        # recebe apenas a key
        self.query_parameters.pop(parameter)
