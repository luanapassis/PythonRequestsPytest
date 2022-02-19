import allure
from assertpy import assert_that, soft_assertions
from bases.test_base import TestBase
from requests_api.get_basic_auth_request import GetBasicAuthRequest


@allure.suite("Basic Auth Feature")
class TestGetBasicAuth(TestBase):

    @allure.tag("API Test")
    @allure.title("Basic auth")
    @allure.description("Test to test Basic Authentication")
    def test_basic_auth(self):
        request = GetBasicAuthRequest()

        response = request.execute_request()

        assert_that(response.status_code).is_equal_to(200)