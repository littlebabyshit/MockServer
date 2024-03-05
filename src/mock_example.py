mock_rules1 = [{"req": "ad", "res": "xxx"}, {""}]

# 不同的case想返回不同的mock结果，这个怎么实现，有什么实现思路？
mock_rules2 = [
    {"req": "ad", "flag": 1, "res": "aaaa"},
    {"req": "ad", "flag": 2, "res": "bbb"},
]

# 3、基于现有的mock server, 如果新增一个接口并且需要mock,怎么做的？需要开发代码？
mock_rules3 = [
    {"req": "ad", "res": "xxx"},
    {"req": "ad2", "res": "yyy"}
]

# 4、mock server中调用第三方接口时鉴权、加解密是怎么做的？加签、验签

# 5、测试一个核保接口，要mock返回核保失败的结果，你们是怎么做的，要改代码吗？

# 6、如果接口自动化测试，涉及到请求外部公司的接口，这个自动化会用到mock server吗？怎么实现的？
mock_rules4 = [
    {"req": "ad", "flag": 1, "res": "aaaa"},
    {"req": "ad", "flag": 2, "res": "bbb"},
]
