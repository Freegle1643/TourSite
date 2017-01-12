#!/usr/bin/python
# -*- coding: utf-8 -*-
from src.QcloudApi.qcloudapi import QcloudApi
import re
import copy
import ConfigParser
import string, os, sys

cf = ConfigParser.ConfigParser()
cf.read("appconfig.conf")

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

def upload2(tid, tname, tpeople, tdest):
    paramsupload2['appId'] = appId2
    paramsupload2['contents.0.tname'] = tname
    paramsupload2['contents.0.tpeople'] = tpeople
    paramsupload2['contents.0.tdest'] = tdest
    paramsupload2['contents.0.id'] = tid
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

def upload3(jid, jname, jdest, jcontent):
    paramsupload3['appId'] = appId3
    paramsupload3['contents.0.jname'] = jname
    paramsupload3['contents.0.jdest'] = jdest
    paramsupload3['contents.0.jcontent'] = jcontent
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
        return [{'dinfo':'False','dname':'False','id':-1}]
        #检查是否成功，错误返回信息写入日志
    counter = (int)(re2.findall(info)[0][0])
    port = re3.findall(info)
    pport = {}
    ppport = []
    for i in range(0, counter):
        pport['dinfo'] = (port[i][0].decode('raw_unicode_escape')).encode("utf-8")
        pport['dname'] = (port[i][1].decode('raw_unicode_escape')).encode("utf-8")
        pport['id'] = port[i][2]
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
    re3 = re.compile('"doc_meta":"\{\\\\"tdest\\\\":\\\\"(.+)\\\\",\\\\"tpeople\\\\":\\\\"(.+)\\\\",\\\\"tname\\\\":\\\\"(.+)\\\\",\\\\"id\\\\":\\\\"(.+)\\\\"\}')
    if re1.findall(info) != ['0']:
        output = open('errorlog', 'a+')
        output.write("search error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return [{'tdest':'False','tpeople':'False','tname':'False','id':-1}]
        #检查是否成功，错误返回信息写入日志
    counter = (int)(re2.findall(info)[0][0])
    port = re3.findall(info)
    pport = {}
    ppport = []
    for i in range(0, counter):
        pport['tdest'] = (port[i][0].decode('raw_unicode_escape')).encode("utf-8")
        pport['tpeople'] = (port[i][1].decode('raw_unicode_escape')).encode("utf-8")
        pport['tname'] = (port[i][2].decode('raw_unicode_escape')).encode("utf-8")
        pport['id'] = port[i][3]
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
    re3 = re.compile('"doc_meta":"\{\\\\"jcontent\\\\":\\\\"(.+)\\\\",\\\\"jdest\\\\":\\\\"(.+)\\\\",\\\\"jname\\\\":\\\\"(.+)\\\\",\\\\"id\\\\":\\\\"(.+)\\\\"\}')
    if re1.findall(info) != ['0']:
        output = open('errorlog', 'a+')
        output.write("search error:\n")
        output.write(url)
        output.write(info)
        output.write("\n")
        output.close()
        return [{'jcontent':'False','jdest':'False','jname':'False','id':-1}]
        #检查是否成功，错误返回信息写入日志
    counter = (int)(re2.findall(info)[0][0])
    port = re3.findall(info)
    pport = {}
    ppport = []
    for i in range(0, counter):
        pport['jcontent'] = (port[i][0].decode('raw_unicode_escape')).encode("utf-8")
        pport['jdest'] = (port[i][1].decode('raw_unicode_escape')).encode("utf-8")
        pport['jname'] = (port[i][2].decode('raw_unicode_escape')).encode("utf-8")
        pport['id'] = port[i][3]
        ppport.append(pport)
    return ppport

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
upload1(1,'无锡','123')
upload1(2,'南京','1234')
'''

m = search1('南京')
print m[0]['dname']