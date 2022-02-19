import json

import allure
from assertpy import assert_that, soft_assertions
from bases.test_base import TestBase
from requests_api.get_mantis_request import GetMantisRequest


@allure.suite("Mantis Feature")
class TestGetMantis(TestBase):

    @allure.tag("API Test")
    @allure.title("Mantis get users")
    @allure.description("Teste to verify empty response body and headers using API Mantis")
    def test_mantis(self):
        request = GetMantisRequest()

        response = request.execute_request()

        assert_that(response.status_code).is_equal_to(200)
