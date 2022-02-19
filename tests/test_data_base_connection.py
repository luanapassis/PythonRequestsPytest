import allure

from bases.test_base import TestBase
from data_base_steps.query_db_steps import QueryDBSteps


@allure.suite("Data Base Connection Feature")
class TestDataBaseConnection(TestBase):


    @allure.tag("Data Base Connection")
    @allure.title("Connect with database and return the query result")
    def test_data_base_connection(self):
        query_db_stesps = QueryDBSteps()
        product = "produto2"

        result = query_db_stesps.get_specific_product(product)

        assert product == result[0][0]

    @allure.tag("Data Base Connection")
    @allure.title("Connect with database and return results")
    def test_data_base_connection_exemple(self):
        query_db_stesps = QueryDBSteps()
        result = query_db_stesps.get_products()



