from bases.soap_request_base import SoapRequestBase
from enums.methods.methods_enum import MethodsEnum


class SoapSumRequest(SoapRequestBase):
    def __init__(self):
        super().__init__()
        self.url = "http://www.dneonline.com/calculator.asmx"
        self.method = MethodsEnum.POST.value

    def set_xml_body(self, payload):
        self.xml_body = payload
