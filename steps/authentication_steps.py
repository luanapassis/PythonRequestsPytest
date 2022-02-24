from requests_api.post_get_token_request import PostGetTokenRequest
from utils.utils import Utils


class AuthenticationSteps():

    @classmethod
    def get_token(self):
        # arranges
        authenticator_user = Utils.read_enviroment_key_json("authenticator_user")
        authenticator_password = Utils.read_enviroment_key_json("authenticator_password")
        request = PostGetTokenRequest()

        # actions
        request.set_json_body_from_text(authenticator_user, authenticator_password)
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        token = response_body["authorization"]

        Utils.write_token_in_config_file(token)
        print(token)


