import json
import allure
from utils.utils import Utils


class AllureUtils:

    @classmethod
    def allure_log_query(cls, result, description):
        results = Utils.convert_into_list(result, description)
        allure.attach(f'{results}', "Query result:", allure.attachment_type.TEXT, results)

    # Methods to log Rest Requests
    @classmethod
    def allure_log_rest_requests(cls, url, request_server, query_parameters, json_body, method, headers, cookies):
        allure.attach(str(url), name="URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(request_server), name="Request", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(query_parameters), name="Parameters", attachment_type=allure.attachment_type.TEXT)
        if json_body != None:
            allure.attach((json.dumps(json.loads(json_body), indent=4)), name="Json Body",
                          attachment_type=allure.attachment_type.TEXT)
        else:
            allure.attach(str(json_body), name="Json Body", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(method), name="Method", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(headers), name="Headers", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(cookies), name="Cookies", attachment_type=allure.attachment_type.TEXT)

    @classmethod
    def allure_log_rest_responses(cls, response_status_code, response_headers, response_text, response):
        allure.attach(str(response_status_code), name="Response StatusCode",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(json.dumps(dict(response_headers), indent=4), name="Response Headers",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(json.dumps(Utils.get_json_in_response(response), indent=4), name="Response Body",
                      attachment_type=allure.attachment_type.JSON)

    # Methods to log Soap Requests
    @classmethod
    def allure_log_soap_requests(cls, url, xml_body, method, headers):
        allure.attach(str(url), name="URL", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(xml_body), name="XML Body", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(method), name="Method", attachment_type=allure.attachment_type.TEXT)
        allure.attach(str(headers), name="Headers", attachment_type=allure.attachment_type.TEXT)

    @classmethod
    def allure_log_soap_responses(cls, response_status_code, response_headers, response_text, response):
        allure.attach(str(response_status_code), name="Response StatusCode",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(json.dumps(dict(response_headers), indent=4), name="Response Headers",
                      attachment_type=allure.attachment_type.TEXT)
        allure.attach(response_text, name="Response Body", attachment_type=allure.attachment_type.JSON)

