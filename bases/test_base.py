import pytest


class TestBase:

    @pytest.fixture(scope='session')
    def config(self):
        print("Function executed just once before all the tests")



    @pytest.fixture(autouse=True)
    def base_test(self, config, request):
        # setUp
        print("antes do teste")

        yield

        # tearDown
        print("depois do teste")

