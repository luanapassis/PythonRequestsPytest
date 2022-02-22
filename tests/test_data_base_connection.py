import allure

from bases.test_base import TestBase
from data_base_steps.query_db_steps import QueryDBSteps


@allure.suite("Data Base Connection Feature")
class TestDataBaseConnection(TestBase):


    @allure.tag("Data Base Connection")
    @allure.title("Connect with database and return the query result")
    def test_data_base_connection(self):
        # arranges
        query_db_stesps = QueryDBSteps()
        product = "produto2"

        # actions
        result = query_db_stesps.get_specific_product(product)

        # asserts
        assert product == result[0][0]

    @allure.tag("Data Base Connection")
    @allure.title("Connect with database and return results")
    def test_data_base_connection_exemple(self):
        # arranges
        query_db_stesps = QueryDBSteps()

        #actions
        result = query_db_stesps.get_products()

        #asserts



