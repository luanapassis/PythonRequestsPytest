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
    @allure.title("Add new pet sucess with Pet object")
    @allure.description("test adding new pet successfully")
    def test_add_new_pet_success(self):
        # arranges
        payload = Pet()
        payload.id = "44"
        category = Category()
        category.id = "55"
        category.name = "Dogs"
        payload.category = category
        payload.name = "Ro"
        payload.photoUrls = ["fotinhafofinha.com.br/foto1", "fotinhafofinha.com.br/foto2"]
        payload.tags = []
        tag1 = Tag()
        tag1.id = 1
        tag1.name = "Pinscher"
        payload.tags.append(tag1)
        tag2 = Tag()
        tag2.id = 2
        tag2.name = "Bravo"
        payload.tags.append(tag2)
        payload.status = "sold"

        request = PostNewPetRequest()

        # actions
        request.set_json_body(payload)
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        # asserts
        assert_that(response.status_code).is_equal_to(200)
        with soft_assertions():
            assert_that(response_body["name"]).contains("Ro")
            assert_that(response_body["tags"][0]["name"]).is_equal_to("Pinscher")
            assert_that(response_body["tags"]).extracting("name").contains("Bravo")
            assert_that(response_body["tags"]).extracting("name").is_equal_to(['Pinscher', 'Bravo'])

    @allure.tag("API Test")
    @allure.title("Add new pet sucess with json file")
    @allure.description("test adding new pet successfully with json file")
    def test_add_new_pet_success_with_json_file(self):
        # arranges
        id = "55"
        category_id = "66"
        category_name = "Dogs"
        name = "Titi"
        photo_urls = "fotinhastiti.com.br"
        tag_id = "1"
        tag_name = "Basset"
        status = "sold"
        request = PostNewPetRequest()

        # actions
        request.set_json_body_from_file(id, category_id, category_name, name, photo_urls, tag_id, tag_name, status)
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        # asserts
        assert_that(response.status_code).is_equal_to(200)

    @allure.tag("API Test")
    @allure.title("Add new pet sucess with Pet text")
    @allure.description("test adding new pet successfully with Pet text")
    def test_add_new_pet_success_with_text(self):
        # arranges
        id = "77"
        category_id = "88"
        category_name = "Dogs"
        name = "Dogo"
        photo_urls = "fotinhasdogo.com.br"
        tag_id = "1"
        tag_name = "Srd"
        status = "sold"
        request = PostNewPetRequest()

        # actions
        request.set_json_body_from_text(id, category_id, category_name, name, photo_urls, tag_id, tag_name, status)
        response = request.execute_request()
        response_body = Utils.get_json_in_response(response)

        # asserts
        assert_that(response.status_code).is_equal_to(200)


