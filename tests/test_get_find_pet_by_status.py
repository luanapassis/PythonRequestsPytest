import json

import allure
from assertpy import assert_that, soft_assertions

from bases.request_base import RequestBase
from bases.test_base import TestBase
from enums.authentication.authentication_enum import AuthenticationEnum
from models.pet import Pet
from models.category import Category
from models.tag import Tag
from requests_api.get_find_pet_by_status_request import GetFindPetByStatusRequest
from requests_api.post_new_pet_request import PostNewPetRequest
from utils.utils import Utils

@allure.suite("Find Pet by Status Feature")
class TestGetFindPetByStatus(TestBase):

    @allure.tag("API Test")
    @allure.title("Find pet by status")
    @allure.description("Find Pet By Status to verify query parameters")
    def test_find_pet_by_status(self):

        request = GetFindPetByStatusRequest()
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        print(response_body)
        print(response.status_code)
        print(response.request)
        print(response.headers)
        print(response.url)

