import pytest

from data_base_steps.query_db_steps import QueryDBSteps


@pytest.fixture(scope='session')
def before_suite():
    print("Método executado no inicio da suíte")
    # caso a geração de token deva ser feita quando inicar a bateria de testes
    # AuthenticationSteps.get_token()

