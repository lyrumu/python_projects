import requests
from lxml import html
#定义URl
target_url = ""
#发送请求 获取数据
#在浏览器地址栏发起的请求 全部用get方式
response = requests.get(target_url)
#输出数据 (解析数据放到后面)
print(response.text)#response是一个对象
#大概率会返回前端页面原代码 需要解析的
#HTML控制内容
#CSS控制样式
#JS控制行为
#因此一般来说 需要解析得到的是HTML的内容
#安装 lxml库 pip install lxml  可以基于Xpath来解析网页
