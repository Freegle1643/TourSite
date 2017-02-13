#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.QcloudApi.qcloudapi import QcloudApi
import re
import copy
import ConfigParser
import string, os, sys

cf = ConfigParser.ConfigParser()
cf.read("qcloudapi_sdk_python/appconfig.conf")#已用相对路径改好了

module = 'yunsou'
action1 = 'DataManipulation'
action2 = 'DataSearch'

secretId = cf.get("app", "secretId")
secretKey = cf.get("app", "secretKey")
appId1 = cf.get("app", "appId1")
appId2 = cf.get("app", "appId2")
appId3 = cf.get("app", "appId3")

config = {
    'Region': 'gz',
    'secretId': secretId,
    'secretKey': secretKey,
    'method': 'get'
}

paramsupload1 = {
    'op_type': 'add',
    'appId': appId1,
}

paramsupload2 = {
    'op_type': 'add',
    'appId': appId2,
}

paramsupload3 = {
    'op_type': 'add',
    'appId': appId3,
}

'''
数据上传
paramsupload = {
    'op_type': 'add',
    'appId': 54550002,
    'contents.0.dname': 'sdshd',
    'contents.0.dinfo': 'dcdyg',
    'contents.0.id': 1003,
}
'''

paramsdelete = {
    'op_type': 'del',
    'appId': appId1,
    'contents.0.doc_id': -1,
}

'''
数据删除，doc_id为主键
params = {
    'op_type': 'del',
    'appId': 54550002,
    'contents.0.doc_id': 1000,
}
'''

paramssearch = {
    "appId" : appId1,
    "search_query" : '',
    "page_id" : 0,
    "num_per_page" : 10,
}

'''
params = {
    "appId" : 54550002,
    "search_query" : "test",
    "page_id" : 0,
    "num_per_page" : 10,
    "num_filter" : "[N:NA:1300:1400]",
}
'''

def upload1(did, dname, dinfo):
    paramsupload1['appId'] = appId1
    paramsupload1['contents.0.dname'] = dname
    paramsupload1['contents.0.dinfo'] = dinfo
    paramsupload1['contents.0.id'] = did
    service = QcloudApi(module, config)
    url = service.generateUrl(action1, paramsupload1)
    info = service.call(action1, paramsupload1)
    print url
    print info
    re1 = re.compile('"code":(\w+),')
    re2 = re.compile('"errmsg":"(\w+)",')
    if re1.findall(info) != ['0'] or re2.findall(info) != ['succ']:
        output = open('errorlog', 'a+')
        output.write("upload error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return False
    return True
    #检查是否成功，错误返回信息写入日志

def upload2(tid, tdays, tname, tdescrip, tpeople, tdest):
    paramsupload2['appId'] = appId2
    paramsupload2['contents.0.tname'] = tname
    paramsupload2['contents.0.tdescrip'] = tdescrip
    paramsupload2['contents.0.tpeople'] = tpeople
    paramsupload2['contents.0.tdest'] = tdest
    paramsupload2['contents.0.id'] = tid
    paramsupload2['contents.0.tdays'] = tdays
    service = QcloudApi(module, config)
    url = service.generateUrl(action1, paramsupload2)
    info = service.call(action1, paramsupload2)
    print url
    print info
    re1 = re.compile('"code":(\w+),')
    re2 = re.compile('"errmsg":"(\w+)",')
    if re1.findall(info) != ['0'] or re2.findall(info) != ['succ']:
        output = open('errorlog', 'a+')
        output.write("upload error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return False
    return True
    #检查是否成功，错误返回信息写入日志

def upload3(jid, jname, jtag):
    paramsupload3['appId'] = appId3
    paramsupload3['contents.0.jname'] = jname
    paramsupload3['contents.0.jtag'] = jtag
    paramsupload3['contents.0.id'] = jid
    service = QcloudApi(module, config)
    url = service.generateUrl(action1, paramsupload3)
    info = service.call(action1, paramsupload3)
    print url
    print info
    re1 = re.compile('"code":(\w+),')
    re2 = re.compile('"errmsg":"(\w+)",')
    if re1.findall(info) != ['0'] or re2.findall(info) != ['succ']:
        output = open('errorlog', 'a+')
        output.write("upload error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return False
    return True
    #检查是否成功，错误返回信息写入日志

def delete(doc_id, appId):
    if appId == 1:
        paramsdelete['appId'] = appId1
    elif appId == 2:
        paramsdelete['appId'] = appId2
    elif appId == 3:
        paramsdelete['appId'] = appId3
    else:
        return False
    paramsdelete['contents.0.doc_id'] = doc_id
    service = QcloudApi(module, config)
    url = service.generateUrl(action1, paramsdelete)
    info = service.call(action1, paramsdelete)
    print url
    print info
    re1 = re.compile('"code":(\w+),')
    re2 = re.compile('"errmsg":"(\w+)",')
    if re1.findall(info) != ['0'] or re2.findall(info) != ['succ']:
        output = open('errorlog', 'a+')
        output.write("delete error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return False
    return True
    #检查是否成功，错误返回信息写入日志

def search1(query):
    paramssearch['appId'] = appId1
    paramssearch['search_query'] = query
    service = QcloudApi(module, config)
    url = service.generateUrl(action2, paramssearch)
    info = (service.call(action2, paramssearch)).encode('utf-8')
    print url
    print info
    re1 = re.compile('"code":(\w+),')
    re2 = re.compile('"result_num":(\w+),')
    re3 = re.compile('"doc_meta":"\{\\\\"dinfo\\\\":\\\\"(.+)\\\\",\\\\"dname\\\\":\\\\"(.+)\\\\",\\\\"id\\\\":\\\\"(.+)\\\\"\}')
    if re1.findall(info) != ['0']:
        output = open('errorlog', 'a+')
        output.write("search error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return [{'id':-1,'dname':'False','dinfo':'False'}]
        #检查是否成功，错误返回信息写入日志
    counter = (int)(re2.findall(info)[0][0])
    port = re3.findall(info)
    pport = {}
    ppport = []
    for i in range(0, counter):
        pport['id'] = (port[i][2].decode('raw_unicode_escape')).encode("utf-8")
        pport['dname'] = (port[i][1].decode('raw_unicode_escape')).encode("utf-8")
        pport['dinfo'] = (port[i][0].decode('raw_unicode_escape')).encode("utf-8")
        ppport.append(pport)
    return ppport

def search2(query):
    paramssearch['appId'] = appId2
    paramssearch['search_query'] = query
    service = QcloudApi(module, config)
    url = service.generateUrl(action2, paramssearch)
    info = service.call(action2, paramssearch)
    print url
    print info
    re1 = re.compile('"code":(\w+),')
    re2 = re.compile('"result_num":(\w+),')
    re3 = re.compile('"doc_meta":"\{\\\\"id\\\\":\\\\"(.+)\\\\",\\\\"tdays\\\\":\\\\"(.+)\\\\",\\\\"tdescrip\\\\":\\\\"(.+)\\\\",\\\\"tdest\\\\":\\\\"(.+)\\\\",\\\\"tname\\\\":\\\\"(.+)\\\\",\\\\"tpeople\\\\":\\\\"(.+)\\\\"\}')
    if re1.findall(info) != ['0']:
        output = open('errorlog', 'a+')
        output.write("search error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return [{'id':-1,'tdays':'False','tname':'False','tdescrip':'False','tpeople':'False','tdest':'False'}]
        #检查是否成功，错误返回信息写入日志
    counter = (int)(re2.findall(info)[0][0])
    port = re3.findall(info)
    pport = {}
    ppport = []
    for i in range(0, counter):
        pport['id'] = (port[i][0].decode('raw_unicode_escape')).encode("utf-8")
        pport['tdays'] = (port[i][1].decode('raw_unicode_escape')).encode("utf-8")
        pport['tname'] = (port[i][4].decode('raw_unicode_escape')).encode("utf-8")
        pport['tdescrip'] = (port[i][2].decode('raw_unicode_escape')).encode("utf-8")
        pport['tpeople'] = (port[i][5].decode('raw_unicode_escape')).encode("utf-8")
        pport['tdest'] = (port[i][3].decode('raw_unicode_escape')).encode("utf-8")
        ppport.append(pport)
    return ppport

def search3(query):
    paramssearch['appId'] = appId3
    paramssearch['search_query'] = query
    service = QcloudApi(module, config)
    url = service.generateUrl(action2, paramssearch)
    info = service.call(action2, paramssearch)
    print url
    print info
    re1 = re.compile('"code":(\w+),')
    re2 = re.compile('"result_num":(\w+),')
    re3 = re.compile('"doc_meta":"\{\\\\"id\\\\":\\\\"(.+)\\\\",\\\\"jname\\\\":\\\\"(.+)\\\\",\\\\"jtag\\\\":\\\\"(.+)\\\\"\}')
    if re1.findall(info) != ['0']:
        output = open('errorlog', 'a+')
        output.write("search error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return [{'id':-1,'jname':'False','jtag':'False'}]
        #检查是否成功，错误返回信息写入日志
    counter = (int)(re2.findall(info)[0][0])
    port = re3.findall(info)
    pport = {}
    ppport = []
    for i in range(0, counter):
        pport['id'] = (port[i][0].decode('raw_unicode_escape')).encode("utf-8")
        pport['jname'] = (port[i][1].decode('raw_unicode_escape')).encode("utf-8")
        pport['jtag'] = (port[i][2].decode('raw_unicode_escape')).encode("utf-8")
        ppport.append(pport)
    return ppport

def searchall(query):
    searchallresult = {}
    destin = search1(query)
    trip = search2(query)
    jouurnal = search3(query)
    searchallresult['destin'] = destin
    searchallresult['trip'] = trip
    searchallresult['jouurnal'] = jouurnal
    return searchallresult

'''
def main():
    service = QcloudApi(module, config)
    print service.generateUrl(action1, paramsupload)
    print service.call(action1, paramsupload)
    #service.setRequestMethod('get')
    #print service.call('DescribeCdnEntities', {})

if (__name__ == '__main__'):
    main()
'''
'''
upload1(5,'天津','ushd')
m = search1('天津')
print m
delete(5,1)
search1('天津')



upload2(1,12,'南京dsd','dwhde','sdd','dsds')
m = search2('南京')
print m
delete(1, 2)
search2('南京')



upload3(1,'无锡','swh')
m = search3('sw')
print m
delete(1, 3)
search3('sw')
'''
