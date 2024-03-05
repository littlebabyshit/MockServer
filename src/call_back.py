import time

import requests


class CallBack:
    def mock(self, req):
        rules = self.get_rules()
        # 返回请求的过程
        for rule in rules:
            if req == rule:
                req.res = rule.get("res")
        # 异步处理，等待50分钟
        time.sleep(50)
        # 对回调发起请求
        self.call_back()

    def call_back(self):
        # 对回调服务发起请求
        requests.post("/回调服务")

    def get_rules(self) -> dict:
        pass
