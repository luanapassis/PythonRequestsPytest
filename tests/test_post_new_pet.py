import json

import allure
from assertpy import assert_that, soft_assertions

from bases.test_base import TestBase
from models.pet import Pet
from models.category import Category
from models.tag import Tag
from requests_api.post_new_pet_request import PostNewPetRequest
from utils.utils import Utils

@allure.suite("New Pet Feature")
class TestPostNewPet(TestBase):

    @allure.tag("API Test")
    @allure.title("Add new pet sucess")
    @allure.description("test adding new pet successfully")
    def test_add_new_pet_success(self):
        payload = Pet()
        payload.id = "99"
        category = Category()
        category.id = "11"
        category.name = "cat name"
        payload.category = category
        payload.name = "Teste"
        payload.photoUrls = ["Fotinha pet1", "Fotinha pet2"]
        payload.tags = []
        tag1 = Tag()
        tag1.id = 1
        tag1.name = "tag1"
        payload.tags.append(tag1)
        tag2 = Tag()
        tag2.id = 2
        tag2.name = "tag2"
        payload.tags.append(tag2)
        payload.status = "avaliable"

        request = PostNewPetRequest()
        request.set_json_body(payload)
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        assert_that(response.status_code).is_equal_to(200)
        with soft_assertions():
            assert_that(response_body["name"]).contains("Tes")
            assert_that(response_body["tags"][0]["name"]).is_equal_to("tag1")
            assert_that(response_body["tags"]).extracting("name").contains("tag2")
            assert_that(response_body["tags"]).extracting("name").is_equal_to(['tag1', 'tag2'])

