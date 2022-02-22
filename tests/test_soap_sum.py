import allure
from assertpy import assert_that, soft_assertions
from lxml import etree
from bases.test_base import TestBase
from requests_api.soap_sum_request import SoapSumRequest


@allure.suite("Soap Feature")
class TestSaoapSum(TestBase):

    @allure.tag("API SOAP Test")
    @allure.title("Sum with SOAP")
    @allure.description("test sum with SOAP requests")
    def test_sum_two_numbers(self):
        # arranges
        payload = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
                       <soapenv:Header/>
                       <soapenv:Body>
                          <tem:Add>
                             <tem:intA>10</tem:intA>
                             <tem:intB>31</tem:intB>
                          </tem:Add>
                       </soapenv:Body>
                    </soapenv:Envelope>"""
        request = SoapSumRequest()

        # actions
        request.set_xml_body(payload)
        response = request.execute_soap_request()
        response_xml = response.text
        tree = etree.fromstring(bytes(response_xml, encoding='utf8'))
        result = tree.xpath("//text()")[0]

        # asserts
        assert_that(response.status_code).is_equal_to(200)
        with soft_assertions():
            assert_that(result).is_equal_to("41")
