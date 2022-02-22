import allure
from assertpy import assert_that, soft_assertions
from bases.test_base import TestBase
from requests_api.get_mantis_request import GetMantisRequest


@allure.suite("Mantis Feature")
class TestGetMantis(TestBase):

    @allure.tag("API Test")
    @allure.title("Mantis get users")
    @allure.description("Teste to verify auth in headers using API Mantis")
    def test_mantis(self):
        # arranges
        request = GetMantisRequest()

        # actions
        response = request.execute_request()

        # asserts
        assert_that(response.status_code).is_equal_to(200)

    @allure.tag("API Test")
    @allure.title("Mantis get users without Authorization")
    @allure.description("Teste to verify empty response body")
    def test_mantis_without_auth(self):
        # arranges
        request = GetMantisRequest()
        request.remove_headers("Authorization")

        # actions
        response = request.execute_request()

        # asserts
        assert_that(response.status_code).is_equal_to(200)
