import pandas as pd
import pymongo
import time
import requests
import json
from bs4 import BeautifulSoup
from spider_weather.save_to_db import *
from spider_weather.get_city_name import *


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


def get_everyday_weather(url, area, year):
    everyday_weather_dict_list = []
    try:
        page_text = get_page(url)
        soup = BeautifulSoup(page_text, 'lxml')
        for index, tr in enumerate(soup.find_all("tr")):
            if index == 0:
                continue
            date = None
            if index % 2 != 0:
                date1 = tr.find("a").get_text()
                date = date1
            else:
                date = date1
            dict_list = {key:con.get_text() for key, con in zip(
                ['time', 'image', 'weather', 'temperature', 'humidity', 'wind_force', 'wind_scale', 'precipitation',
                 'sendible_temperature', 'cloud_amount'], tr.find_all("td"))}
            dict_list["area"] = area
            dict_list["year"] = year
            dict_list['date'] = date
            everyday_weather_dict_list.append(dict_list)
        print(len(everyday_weather_dict_list))
        # for d in everyday_weather_dict_list:
        #     print(d)
        # print(everyday_weather_dict_list)
        return everyday_weather_dict_list
    except Exception as e:
        print("ERROR:", e)


def get_everyday_detail_weather(url, area, year, mon, day):
    everyday_detail_weather_dict_list = []
    try:
        page_text = get_page(url)
        soup = BeautifulSoup(page_text, 'lxml')
        for index, tr in enumerate(soup.find_all("tr")):
            if index == 0:
                continue
            time = tr.find('th').get_text()
            dict_list = {key: con.get_text() for key, con in zip(
                ['time', 'image', 'weather', 'temperature', 'humidity', 'wind_force', 'wind_scale', 'precipitation',
                 'sendible_temperature', 'cloud_amount'], tr.find_all("td"))}
            dict_list["area"] = area
            dict_list["year"] = year
            dict_list['date'] = str(mon)+"月"+str(day)+"日"
            dict_list["times"] = time
            everyday_detail_weather_dict_list.append(dict_list)
        print(len(everyday_detail_weather_dict_list))
        # for d in everyday_weather_dict_list:
        #     print(d)
        # print(everyday_weather_dict_list)
        return everyday_detail_weather_dict_list
    except Exception as e:
        print("ERROR:", e)


def get_all_year_weather(url, area, year):
    all_year_weather_dict_list = []
    try:
        page_text = get_page(url)
        soup = BeautifulSoup(page_text, 'lxml')
        mcon_list = soup.find_all(name="div", attrs={"class": "mcon"})
        every_elements = []
        for m in mcon_list:
            mm = BeautifulSoup(str(m), 'lxml')
            for t in mm.find_all("table"):
                tt = BeautifulSoup(str(t), 'lxml')
                key = []
                for index, tr in enumerate(tt.find_all("tr")):
                    if index == 0:
                        key = [th.get_text() for th in tr.find_all("th")]
                        # print(key)
                    else:
                        th = key[0]+": "+tr.find("th").get_text()
                        td = [td.get_text() for td in tr.find_all("td")]
                        td.insert(0, th)
                        every_elements.append(td)
                        # print(td)
        # print(len(every_elements))
        # for el in every_elements:
        #     print(el)
        # 加入dict
        for col in range(1, 14):
            every_elements_dict = {}
            for row in range(len(every_elements)):
                every_elements_dict['area'] = area
                every_elements_dict['year'] = year
                if col == 1:
                    every_elements_dict['time'] = '全年'
                else:
                    every_elements_dict['time'] = str(col-1)+'月'
                every_elements_dict[every_elements[row][0]] = every_elements[row][col]
            all_year_weather_dict_list.append(every_elements_dict)
        # print(len(all_year_weather_dict_list))
        # for al in all_year_weather_dict_list:
        #     print(al)
        return all_year_weather_dict_list
    except Exception as e:
        print("ERROR:", e)


if __name__ == '__main__':
    # 获得区域列表
    area_list = start_get()

    # # ===================================================part1========================================================
    # # 开始爬取2017-2019各区域全年平均、最高低天气信息
    # failed_url_all_year_list = []
    # for area in area_list:
    #     for year in range(2017, 2020):
    #         url = "https://tianqi.911cha.com/" + area + "/" + str(year) + ".html"
    #         all_year_weather_dict_list = get_all_year_weather(url, area, year)
    #         try:
    #             save_all_year_weather("every_area_all_year_weather", all_year_weather_dict_list)
    #             print("---------------------------华丽分割线------------------------------")
    #         except Exception as e:
    #             print("ERROR:", e)
    #             failed_url_all_year_list.append(url)
    # print(len(failed_url_all_year_list))
    # print(failed_url_all_year_list)

    # # ===================================================part2========================================================
    # # 测试
    # area_list = ["chengguanqu", "qilihe", "xigu", "anningqu", "honggu", "yongdeng", "gaolan", "yuzhong"]
    # url = "https://tianqi.911cha.com/" + "chengguanqu" + "/" + str(2009) + "-" + str(1) + ".html"
    # dic_list = get_everyday_weather(url, "chengguanqu", "2009")
    # save_everyday_weather("everyday_weather", dic_list)

    # # ===================================================part3========================================================
    # # 开始爬取2017-2019个区域每天每时的天气信息
    # failed_url2_list = []
    # failed_url_list = []
    #
    # for area in area_list:
    #     for year in range(2017, 2020):
    #         for mon in range(1, 13):
    #             # 每月的
    #             url = "https://tianqi.911cha.com/"+area+"/"+str(year)+"-"+str(mon)+".html"
    #             dic_list = get_everyday_weather(url, area, str(year))
    #             # print(dic_list)
    #             try:
    #                 save_everyday_weather("every_area_everyday_weather", dic_list)
    #             except:
    #                 failed_url_list.append(url)
    #
    #             # 每天的
    #             days = 0
    #             if mon == 2:
    #                 if (year % 4) == 0:
    #                     if (year % 100) == 0:
    #                         if (year % 400) == 0:
    #                             days = 29
    #                         else:
    #                             days = 28
    #                     else:
    #                         days = 29
    #                 else:
    #                     days = 28
    #             elif mon == 1 or mon == 3 or mon == 5 or mon == 7 or mon == 8 or mon == 10 or mon == 12:
    #                 days = 31
    #             else:
    #                 days = 30
    #             for day in range(1, days+1):
    #                 url2 = "https://tianqi.911cha.com/"+area+"/"+str(year)+"-"+str(mon)+"-"+str(day)+".html"
    #                 everyday_list = get_everyday_detail_weather(url2, area, str(year), mon, day)
    #                 try:
    #                     save_everyday_detail_weather("everyday_detail_weather_dict_list", everyday_list)
    #                 except:
    #                     failed_url2_list.append(url2)
    #                     # print(url2)
    # print("failed_url:", failed_url_list)
    # print("failed_url2:", failed_url2_list)

    # # ===================================================part4========================================================
    # # 爬取失败列表中的信息
    # u = ['https://tianqi.911cha.com/chengguanqu/2017-4-30.html', 'https://tianqi.911cha.com/chengguanqu/2018-11-3.html',
    #  'https://tianqi.911cha.com/anningqu/2019-8-14.html', 'https://tianqi.911cha.com/anningqu/2019-8-15.html',
    #  'https://tianqi.911cha.com/huining/2017-12-5.html', 'https://tianqi.911cha.com/maiji/2017-10-2.html',
    #  'https://tianqi.911cha.com/suzhouqu/2017-1-23.html', 'https://tianqi.911cha.com/zhangxian/2017-9-12.html']
    # for u in failed_url2_list_input:
    # everyday_list = get_everyday_detail_weather(u[7], "zhangxian", str(2017), 9, 12)
    # save_everyday_detail_weather("everyday_detail_weather_dict_list", everyday_list)