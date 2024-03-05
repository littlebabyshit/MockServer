import requests


def test_httpbin():
    pass


def test_get():
    r = requests.get("https://httpbin.ceshiren.com/get", params={"name": "ad"})
    print(r.json())