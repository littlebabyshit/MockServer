"""
模拟后端代码发送请求
"""
import requests
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    url_param = request.args
    name = url_param.get("name")
    proxy = {"http": "http://127.0.0.1:8080"
             ,"https": "http://127.0.0.1:8080"
             }
    # 模拟调后端第三方接口
    r = requests.get("https://httpbin.ceshiren.com/get",
    # 在调用第三方接口的时候需要配置代理
    #                  proxies=proxy,
                     params={"name": name}, verify=False)
    args = r.json().get("args")
    return {"host": str(args), "name": "123"}


if __name__ == '__main__':
    app.run()
