from utils.data_base_utils import DataBaseUtils
from utils.utils import Utils


class QueryDBSteps:

    QUERIES_PATH = "./queries/"

    def get_specific_product(self, product):
        query = Utils.read_file(self.QUERIES_PATH+"get_a_product.sql")
        query = query.replace("$produto", product)
        return DataBaseUtils.return_query_result(query)

    def get_products(self):
        query = Utils.read_file(self.QUERIES_PATH+"get_products.sql")
        return DataBaseUtils.return_query_result(query)
