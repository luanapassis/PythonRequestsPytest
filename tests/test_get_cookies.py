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
        # arrange
        request = GetCookiesRequest()

        # actions
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        # asserts
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)

    @pytest.mark.smoke
    @allure.tag("API Test")
    @allure.title("Remove cookies")
    @allure.description("Test to insert and remove cookies")
    def test_cookies_remove(self):
        # arranges
        request = GetCookiesRequest()

        # actions
        # first request
        response = request.execute_request()
        Utils.get_json_in_response(response)
        # second request
        request2 = GetCookiesRemovingRequest()
        response2 = request2.execute_request()
        Utils.get_json_in_response(response2)

        # asserts
        with soft_assertions():
            assert_that(response.status_code).is_equal_to(200)
            assert_that(response2.status_code).is_equal_to(200)
