#!/usr/bin/env python3

import requests
from requests.exceptions import RequestException
from multiprocessing import Pool
from bs4 import BeautifulSoup
import pymongo
from config import *

#goodsmile厂商的地址
url = "https://www.goodsmile.info/zh/products/announced/"
#获取到年份的list


#配置数据库信息
client = pymongo.MongoClient(MONGO_URL)
db_prototype_data_info = client[PROTOTYPE_DATA_INFO]


'''
    对goodsmile请求返回页面
'''
def search(year):
    try:
        res = requests.get(url + str(year))
        if res.status_code == 200:
            # print("11111")
            return res.text
        # print("2222222")
        return search(year)
    except RequestException:
        # print("3333333")
        return search(year)

'''
    解析页面得到所有商品的url
'''
def parse_page(year):
    page_text = search(year)
    soup = BeautifulSoup(page_text, 'lxml')
    urls_data = soup.findAll(name = "div", attrs = {"class" : "hitBox"})
    # print(urls_data)
    i = 0
    for data_item in urls_data:
        # print(data_item.a.get('href'))
        i += 1
        db_prototype_data_info['good_smile_company_url_list'].save({'url':data_item.a.get('href')})

    print("第" + str(year) + "年共有" + str(i) + "个手办")


def main():

    # pool = Pool(processes = 10)
    # pool.map(parse_page,year_list)
    YEAR_LIST = [2019, 2018, 2017, 2016, 2015, 2014, 2013, 2012, 2011, 2010, 2009, 2008, 2007, 2006]
    for year in YEAR_LIST:
        parse_page(year)


if __name__ == '__main__':
    main()
