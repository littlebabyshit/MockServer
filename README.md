
## Mock规则

### req ( if 真实请求 == req)

哪些请求需要mock，哪些不需要mock：

### res



1、能说下你们的mock server是怎么实现的吗？

- 没改进的mock

```plantuml
title 未mock
接口用例 -> 服务端: 发起请求
服务端 -> 第三方: 发起请求
第三方 -> 服务端: 响应信息
服务端 -> 测试用例: 响应信息
```


```plantuml
title 简单mock
接口用例 -> 服务端: 发起请求
服务端 -> MockServer: 发起请求
MockServer  -> MockServer: 匹配是否要mock
MockServer -> 服务端: 如果要mock 返回响应
服务端 -> 接口用例: 响应信息
```

```plantuml
title 复杂mock
接口用例 -> MockRules文件: 添加mock规则
接口用例 -> 服务端: 发起请求
服务端 -> MockServer: 发起请求
MockServer  -> MockRules文件: 获取所有的规则信息
MockRules文件 -> MockServer: 是否可以mock
MockServer -> 服务端: 如果要mock 返回响应
服务端 -> 接口用例: 响应信息
```





2、不同的case想返回不同的mock结果，这个怎么实现，有什么实现思路？
3、基于现有的mock server,如果新增一个接口并且需要mock,怎么做的？需要开发代码？
4、mock server中调用第三方接口时鉴权、加解密是怎么做的？加签、验签
5、测试一个核保接口，要mock返回核保失败的结果，你们是怎么做的，要改代码吗？
6、如果接口自动化测试，涉及到请求外部公司的接口，这个自动化会用到mock server吗？怎么实现的？