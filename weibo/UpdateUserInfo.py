import pymongo
import requests
from bs4 import BeautifulSoup
from lxml import etree
import re

def get_proxies():
    # 代理服务器
    # 阿布云动态版
    proxyHost = "http-dyn.abuyun.com"
    proxyPort = "9020"
    # 代理隧道验证信息
    proxyUser = "H40C3249595Y905D"
    proxyPass = "43CDFD383F5A23D3"
    proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
        "host": proxyHost,
        "port": proxyPort,
        "user": proxyUser,
        "pass": proxyPass,
    }
    proxies = {
        "http": proxyMeta,
        "https": proxyMeta,
    }
    return proxies

myclient = pymongo.MongoClient("mongodb://172.17.13.223:27017/",
                               username='root',
                               password='example',
                               authSource='admin',
                               authMechanism='SCRAM-SHA-1')
mydb = myclient["weibo_db"]
mycol = mydb["users"]
cursor = mycol.find({})
userids = []
for document in cursor:
    # print(document['id'])
    userids.append(document['id'])
import pandas as pd

pd.DataFrame(userids).to_csv('user_ids.csv')
# print(userids)
# userids.to_csv('user_ids.csv')
# cookies_str = 'Cookie: SINAGLOBAL=2396446694865.8545.1609895077206; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5.ZPavGw5iRLyICST4rfu85JpX5KMhUgL.Fo-cehB0Sh5N1K.2dJLoI7feIg4rIGHoIsvV905R; ALF=1641452001; SSOLoginState=1609915987; SCF=Au-OYR11J_LzHRUat3D5-pYmWau668YHYNPz1E5nIq_vFmJo5ba5XJvrfGz-dvu36xAkWLvfIQd4BcnGmjFChks.; SUB=_2A25y8S4yDeRhGeNI61YS9C7LwjWIHXVRhxj6rDV8PUNbmtAfLWrNkW9NSKc9QqDb7YBm0Npf6CJ76X4TSN1D-5tA; wvr=6; _s_tentry=login.sina.com.cn; UOR=,,www.google.com; Apache=9735507163292.777.1609916005694; ULV=1609916005738:2:2:2:9735507163292.777.1609916005694:1609895077225; webim_unReadCount=%7B%22time%22%3A1609998260278%2C%22dm_pub_total%22%3A4%2C%22chat_group_client%22%3A0%2C%22chat_group_notice%22%3A0%2C%22allcountNum%22%3A52%2C%22msgbox%22%3A0%7D'
# cookies={}#初始化cookies字典变量
#
# for line in cookies_str.split(';'):   #按照字符：进行划分读取
#     #其设置为1就会把字符串拆分成2份
#     name,value=line.strip().split('=',1)
#     cookies[name]=value  #为字典cookies添加内容
#
#
# agent = 'Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1'
#
# for uid in userids:
#     url = f'https://weibo.com/u/{uid}?is_hot=1'
#
#     home_page = requests.get(url, cookies=cookies, proxies=get_proxies())
#     #     粉丝xpath
#     follows_path = '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[1]/div/div/div/table/tbody/tr/td[2]/a/strong'
# #     资料xpath
#     infos_path = '/html/body/div[1]/div/div[2]/div/div[2]/div[1]/div[4]/div/div/a'
#     ret = pattern.match(r'location.replace("(?.")')
#
#     pattern = re.compile(r"^\$CONFIG['page_id']='\d+';$")
#     ret = pattern.match(home_page.content)
#
#     selector = etree.HTML(home_page.content)
#     # soup = BeautifulSoup(home_page.text)
#     # 粉丝
#     divs = selector.xpath(follows_path)
#     # soup.select(".tb_counter")
