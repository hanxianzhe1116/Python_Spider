import pandas as pd
import pymongo
import time
from multiprocessing import Pool
import requests
from bs4 import BeautifulSoup
from spider_renren.get_city_data.config import *
from spider_renren.get_city_data.save_to_db import *

# 连接数据库
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
table = db['every_car_url']


def get_every_car_url():
    data = pd.DataFrame(list(table.find()))
    data = data["every_car_url"]
    every_car_url_list = []
    for i in data.index:
        every_car_url_list.append(data.loc[i])
    return every_car_url_list


def get_page(url):
    try:
        # time.sleep(1.5)
        res = requests.get(url)
        if res.status_code == 200:
            # print(res.text)
            return res.text
    except:
        time.sleep(10)


def get_cars_detail_info(url):
    table_dict = {}
    table_dict["url"] = url
    try:
        page_text = get_page(url)
        soup = BeautifulSoup(page_text, 'lxml')
        right_container = soup.find_all(name="div", attrs={"class": "right-container"})
        middle_content = BeautifulSoup(str(right_container), 'lxml').find_all(name="div", attrs={"class": "middle-content"})
        price = BeautifulSoup(str(middle_content), 'lxml').find(name="p", attrs={"class": "price detail-title-right-tagP"})
        if price is not None:
            price = str(price.contents[0]).replace('\n', '').replace(' ', '')
            # print(price)
            table_dict["售价"] = price
        new_car_price_span = BeautifulSoup(str(middle_content), 'lxml').find(name="div", attrs={
            "class": "new-car-price detail-title-right-tagP"})
        new_car_price = BeautifulSoup(str(new_car_price_span), 'lxml').find(name="span")
        if new_car_price is not None:
            new_car_price = str(new_car_price.get_text()).replace('\n', '').replace(' ', '')
            # print(new_car_price[:-1])
            table_dict["新车售价"] = new_car_price[:-1]

        mileage_li = soup.find_all(name="li", attrs={"class": "kilometre"})
        mileage = BeautifulSoup(str(mileage_li), 'lxml').find(name="strong")
        if mileage is not None:
            mileage = str(mileage.get_text()).replace('\n', '').replace(' ', '')
            # print(mileage[:-3])
            table_dict["行驶里程"] = mileage[:-3]

        city_div = soup.find_all(name="div", attrs={"class": "licensed-city"})
        city = BeautifulSoup(str(city_div), 'lxml').find(name="strong")
        if city is not None:
            city = str(city.get_text()).replace('\n', '').replace(' ', '')
            # print(city)
            table_dict["车牌所在地"] = city

        info_ul = soup.find_all(name="ul", attrs={"class": "module-base-content clearfixnew"})
        ul_soup = BeautifulSoup(str(info_ul), 'lxml')
        for index, li in enumerate(ul_soup.find_all('li')):
            li_soup = BeautifulSoup(str(li), 'lxml')
            base_key = li_soup.find(name="span", attrs={"class": "module-base-content-key"})
            base_value = li_soup.find(name="span", attrs={"class": "module-base-content-value"})
            if base_key is not None and base_value is not None:
                base_key = str(base_key.contents[0]).replace('\n', '').replace(' ', '')
                base_value = str(base_value.contents[0]).replace('\n', '').replace(' ', '')
                # print(base_key, base_value)
                table_dict[base_key] = base_value

        js_parms_table = soup.find_all(name="div", attrs={"id": "js-parms-table"})
        soup2 = BeautifulSoup(str(js_parms_table), 'lxml')

        for index, table in enumerate(soup2.find_all('table')):
            soup3 = BeautifulSoup(str(table), 'lxml')
            for index2, tr in enumerate(soup3.find_all("tr")):
                if index2 != 0:
                    tds = tr.find_all('td')
                    for index3, td in enumerate(tds):
                        # print(index, index2, index3)
                        # print(type(BeautifulSoup(str(td), 'lxml').find(name="div", attrs={"class": "item-name"})))
                        soup_key = BeautifulSoup(str(td), 'lxml').find(name="div", attrs={"class": "item-name"})
                        soup_value = BeautifulSoup(str(td), 'lxml').find(name="div", attrs={"class": "item-value"})
                        if soup_key is not None and soup_value is not None:
                            dict_key = str(soup_key.contents[0]).replace('\n', '').replace(' ', '')
                            dict_value = str(soup_value.contents[0]).replace('\n', '').replace(' ', '')
                            # if dict_key != "" and dict_value != "":
                            table_dict[dict_key] = dict_value
                    # print(table_dict)
                    # print(tds[0].contents[0])
                    # print(tds[0].contents[1])
                    # print(tds[1])
                    # print(tds[2])
            # print(index, table)
        # print(table_dict)
        # table_text = soup2.find_all("table")
        # print(table_text)
        # for index, table in enumerate(soup.find_all('tr')):
        #
        #
        #
        # for table in table_text:
        #     table.to_csv("2.csv", encoding='utf-8', header=0, index=False)
        # print(len(table_dict))

        # if len(table_dict) != 202:
        #     print(len(table_dict))
        #     for d in table_dict.values():
        #         print(d)
        #     save_failed_url = SaveData()
        #     save_failed_url.save_failed_url("failed_url", {"failed_url": table_dict["url"]})
        # else:
        #     save_car_detail = SaveData()
        #     save_car_detail.save_car_detail("cars_info", table_dict)
        save_car_detail = SaveData()
        save_car_detail.save_car_detail("cars_info_4", table_dict)
        # return table_dict
        # return failed_url
    except:
        print("咱也不知道啥问题！我擦！")


def main(i):
    try:
        get_cars_detail_info(every_car_url_list[i])
    except:
        print("问题url:"+str(every_car_url_list[i]))
        print("main里出问题了！我擦！")


every_car_url_list = get_every_car_url()
failed_url = []
if __name__ == '__main__':
    pool = Pool(4)
    try:
        pool.map(main, [i for i in range(0, len(every_car_url_list))])
    except:
        print("多线程出问题了！我擦！")
    pool.close()
    pool.join()
    # every_car_url_list = get_every_car_url()
    # for i in range(len(every_car_url_list)):
    #     get_cars_detail_info(every_car_url_list[i])
    # print(every_car_url_list[i])
    # print(len(every_car_url_list))
    # print(every_car_url_list[4])
    # get_cars_detail_info("https://www.renrenche.com/anshun/car/205e191aa21afba5")
    # print(every_car_url_list[5])
    # get_cars_detail_info(every_car_url_list[5])
