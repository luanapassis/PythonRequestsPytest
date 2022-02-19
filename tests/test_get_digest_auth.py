import allure
from assertpy import assert_that, soft_assertions
from bases.test_base import TestBase
from requests_api.get_digest_auth_request import GetDigestAuthRequest


@allure.suite("Basic Digest Feature")
class TestGetBasicAuth(TestBase):

    @allure.tag("API Test")
    @allure.title("Digest auth")
    @allure.description("Test to test Digest Authentication")
    def test_basic_auth(self):
        request = GetDigestAuthRequest()

        response = request.execute_request()

        assert_that(response.status_code).is_equal_to(200)