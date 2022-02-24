import pytest
from data_base_steps.query_db_steps import QueryDBSteps
from steps.authentication_steps import AuthenticationSteps


class TestBase:


    @pytest.fixture(autouse=True)
    def base_test(self, before_suite):
        # setUp
        # caso a geração de token deva ser feita quando inicar cada teste
        # AuthenticationSteps.get_token()
        print("Inicio do teste")

        yield

        # tearDown
        print("Final do teste")
