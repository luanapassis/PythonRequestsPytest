from bases.request_base import RequestBase


class GetCookiesRemovingRequest(RequestBase):
    def __init__(self):
        super().__init__()
        self.remove_cookies('location')
        self.url = "https://httpbin.org"
        self.method = "GET"
        self.request_server = "/cookies"

