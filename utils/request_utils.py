import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth
from requests_oauthlib import OAuth1
from requests_ntlm import HttpNtlmAuth

from utils.utils import Utils


class RequestUtils:


    @classmethod
    def execute_request(cls, method, url, request_server, headers, query_parameters, cookies, json_body,
                        authentication_type):

        authentication_used = cls.select_authentication_type(authentication_type)

        response = requests.request(method, url + request_server, headers=headers,
                                    params=query_parameters, cookies=cookies,
                                    data=json_body, auth=authentication_used)

        return response

    @classmethod
    def select_authentication_type(cls, authentication_type):

        authenticator_user = Utils.read_enviroment_key_json("authenticator_user")
        authenticator_password = Utils.read_enviroment_key_json("authenticator_password")
        app_key = Utils.read_enviroment_key_json("app_key")
        app_secret = Utils.read_enviroment_key_json("app_secret")

        if authentication_type == "BASIC":
            return HTTPBasicAuth(authenticator_user, authenticator_password)
        elif authentication_type == "NTLM":
            return HttpNtlmAuth(authenticator_user,authenticator_password)
        elif authentication_type == "DIGEST":
            return HTTPDigestAuth(authenticator_user, authenticator_password)
        elif authentication_type == "OAUTH1":
            auth = OAuth1(app_key, app_secret)
            return auth
        elif authentication_type == "NONE":
            return None
        else:
            raise Exception(f'Authentication type "{authentication_type}" is not supported')
