import logging
import sys

from mitmproxy import http
from mitmproxy.tools.main import mitmdump

from mock_rules import MockRules


class MitmJson:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow):

        # if flow.request.host == "httpbin.ceshiren.com":
        #     self.num = self.num + 1
        #     # 如果是前两次请求，则返回500，让其失败
        #     if self.num == 1 or self.num == 2:
        #         print(f"支付接口第{self.num}次发起请求")
        #         flow.response = http.Response.make(
        #             500,  # (optional) status code
        #             b"Hello World",  # (optional) content
        #             {"Content-Type": "text/html"}  # (optional) headers
        #         )

        for rule in MockRules.get_rules():
            if flow.request.query == rule.get("req"):
                pass


        # self.num = self.num + 1
        # logging.info("We've seen %d flows" % self.num)


    @classmethod
    def main(cls):
        mitmdump()

addons = [MitmJson()]

if __name__ == '__main__':
    MitmJson.main()
