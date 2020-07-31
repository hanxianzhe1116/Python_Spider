import pandas as pd
import pymongo
import requests
import json
from bs4 import BeautifulSoup
from spider_renren.get_city_data.config import *
from spider_renren.get_city_data.save_to_db import *


# 连接数据库
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
table = db['page_url']


def get_page_url():
    data = pd.DataFrame(list(table.find()))
    data = data[["page_url", "city_name"]]
    page_list = []
    for i in data.index:
        page_list.append([data.loc[i][1], data.loc[i][0]])
    return page_list


def get_page(url):
    try:
        res = requests.get(url)
        if res.status_code == 200:
            # print(res.text)
            return res.text
    except:
        print("url解析错误，url："+url)


def get_url(url):
    try:
        url_list = []
        page_text = get_page(url)
        soup = BeautifulSoup(page_text, 'lxml')
        ul = soup.find_all(name="ul", attrs={"class": "row-fluid list-row js-car-list"})
        soup2 = BeautifulSoup(str(ul), 'lxml')
        urls = soup2.find_all(name="a")
        # 抓取单个车的url list
        for u in urls:
            url_list.append("https://www.renrenche.com"+u.get('href'))
        url_list.sort()
        url_len = len(url_list[len(url_list)//2])
        new_url_list = []
        # for u in url_list:
        #     print(u)
        # 删除无效链接
        for i in range(len(url_list)):
            if len(url_list[i]) == url_len:
                new_url_list.append(url_list[i])
        url_dict = []
        # print(len(url_list))
        for u in new_url_list:
            url_dict.append({"every_car_url": u})
        save_every_car_url = SaveData()
        save_every_car_url.save_every_car_url("every_car_url", url_dict)
    except:
        print("error")


if __name__ == '__main__':
    page_list = get_page_url()
    # 开始爬每个页面的每个车
    # get_url(page_list[155][1])
    # get_url(page_list[2][1])
    for i in range(1232, len(page_list)):
        print("index:", i)
        print("开始"+page_list[i][0]+"爬取，链接："+page_list[i][1])
        get_url(page_list[i][1])
