使用前修改：
1.appconfig.conf中存放云API密钥以及各个appid，必须对应正确
2.demo.py中的cf.read()参数需要填写appconfig.conf的绝对路径，中间用/而不是\

demo.py中主要API
下述函数中名中若带有1，2，3指分别对应用TourDestination，TourTrip，TourJournal进行操作

upload1(did, dname, dinfo)
upload2(tid, tdays, tname, tdescrip, tpeople, tdest)
upload3(jid, jname, jtag)
//注意这里的tdest为具体的地名而非数据库中的数字指代，需要对数据库中相应数字进行转换变为具体地名方可使用
//返回true，false来判定是否上传正确，若错误可到errorlog中查看upload error:对应的具体错误

delete(doc_id, appId)//这里的doc_id即是上面的did，tid，jid，appId为选择操作的应用，值可为1，2，3
//返回true，false来判定是否上传正确，若错误可到errorlog中查看delete error:对应的具体错误

search1(query)
search2(query)
search3(query)
searchall(query)
//仅需将需要搜索的字符串传入即可，前三个分别对对应的应用进行操作，返回结果为包含多个字典(每个字典对应一条查询结果)的列表，
//字典键除了将did，tid，jid统一为id，其他与uploadx()函数中参数名相同
//最后一个将对三个应用针对三个列表整合成一个字典，键分别为destin，trip，jouurnal
//如果错误，将返回仅有一个字典的列表，且字典中所有id均为-1，其余文本都为False，可到errorlog中查看search error:对应的具体错误

例子：
对三个应用分别进行插入查询删除查询四次操作检查的demo

'''
upload1(5,'天津','ushd')
m = search1('天津')
print m
delete(5,1)
search1('天津')
'''

'''
upload2(1,12,'南京dsd','dwhde','sdd','dsds')
m = search2('南京')
print m
delete(1, 2)
search2('南京')
'''

'''
upload3(1,'无锡','swh')
m = search3('sw')
print m
delete(1, 3)
search3('sw')
'''

一个完整的对第三个应用操作的例子：
'''
#!/usr/bin/python
# -*- coding: utf-8 -*-
from qcloudapi_sdk_python.demo import*    #from demo import*

upload3(1,'无锡','swh','wsu')
search3('sw')
delete(1, 3)
search3('sw')
'''
