import allure
from assertpy import assert_that, soft_assertions
from bases.test_base import TestBase
from requests_api.get_oauth1_request import GetOauth1Request


@allure.suite("Basic Digest Feature")
class TestGetOauth1(TestBase):

    @allure.tag("API Test")
    @allure.title("Oauth1 auth")
    @allure.description("Test to test Oauth1 Authentication")
    def test_basic_auth(self):
        request = GetOauth1Request()

        response = request.execute_request()

        assert_that(response.status_code).is_equal_to(200)