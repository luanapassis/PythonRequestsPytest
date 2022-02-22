import allure
from bases.test_base import TestBase
from requests_api.get_find_pet_by_status_request import GetFindPetByStatusRequest
from utils.utils import Utils

@allure.suite("Find Pet by Status Feature")
class TestGetFindPetByStatus(TestBase):

    @allure.tag("API Test")
    @allure.title("Find pet by status")
    @allure.description("Find Pet By Status to verify query parameters")
    def test_find_pet_by_status(self):
        # arrange
        request = GetFindPetByStatusRequest()

        # actions
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        #asserts

