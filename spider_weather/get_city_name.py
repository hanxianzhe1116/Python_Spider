import pandas as pd
import pymongo
import time
import requests
import json
from bs4 import BeautifulSoup
from spider_weather.save_to_db import *


def get_page(url):
    try:
        # time.sleep(1.5)
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"}
        res = requests.get(url, headers=header)
        if res.status_code == 200:
            # print(res.text)
            return res.text
    except Exception as e:
        print("ERROR:", e)
        time.sleep(10)


def get_city_name(url):
    try:
        page_text = get_page(url)
        soup = BeautifulSoup(page_text, 'lxml')
        city_list = []
        city = soup.find_all(name="ul", attrs={"class": "l2 f14 tqlist"})
        soup2 = BeautifulSoup(str(city), 'lxml')
        city_name = soup2.find_all(name="a")
        # print(1111)
        for u in city_name:
            u_n = u.get('href')
            if len(u_n) < 15:
                city_list.append(u_n[2:-1])
        return city_list
    except Exception as e:
        print("ERROR:", e)


def get_city_every_area(city_list):
    try:
        city_area_list = []
        for c in city_list:
            url = "https://tianqi.911cha.com/" + c
            page_text = get_page(url)
            soup = BeautifulSoup(page_text, 'lxml')
            city = soup.find_all(name="ul", attrs={"class": "l2 f14 tqlist"})
            soup2 = BeautifulSoup(str(city[0]), 'lxml')
            city_name = soup2.find_all(name="a")
            for u in city_name:
                u_n = u.get('href')
                city_area_list.append(u_n[3:-1])
        return city_area_list
    except Exception as e:
        print("ERROR:", e)


def start_get():
    # url = "https://tianqi.911cha.com/gansu.html"
    # city_list = get_city_name(url)
    # print(city_list)
    city_list = ['lanzhou', 'jinchang', 'baiyin', 'tianshui', 'wuwei', 'zhangye', 'pingliang', 'jiuquan', 'qingyang', 'dingxi', 'longnan', 'linxia', 'gannanzhou']
    city_area_list = get_city_every_area(city_list)
    # 嘉峪关特殊情况，无单独区域
    city_area_list.append('jiayuguan')
    return city_area_list