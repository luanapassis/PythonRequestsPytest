import allure
import pytest
from assertpy import assert_that, soft_assertions
from bases.test_base import TestBase
from requests_api.get_cookies_removing_request import GetCookiesRemovingRequest
from requests_api.get_cookies_request import GetCookiesRequest
from utils.utils import Utils

@allure.suite("Cookies Feature")
class TestGetCookies(TestBase):

    @pytest.mark.smoke
    @allure.tag("API Test")
    @allure.title("Insert Cookies")
    @allure.description("Test to insert cookies")
    def test_cookies_insert(self):

        request = GetCookiesRequest()
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)

    @pytest.mark.smoke
    @allure.tag("API Test")
    @allure.title("Remove cookies")
    @allure.description("Test to insert and remove cookies")
    def cookies_remove(self):
        request = GetCookiesRequest()
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)

        request2 = GetCookiesRemovingRequest()
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
