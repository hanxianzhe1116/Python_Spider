from spider_renren.get_city_data.config import *
import pymongo


client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]

class SaveData:
    def save_city_url(self, table, city_url_dict):
        print("save to db[city_url]")
        data_len = len(city_url_dict)
        for item in city_url_dict:
            db[table].save(item)
        print("共存入"+str(data_len)+"条数据到"+table+"数据库！")

    def save_page_url(self, table, page_url_dict):
        print("save to db[page_url]")
        data_len = len(page_url_dict)
        for item in page_url_dict:
            db[table].save(item)
        print("共存入"+str(data_len)+"条数据到"+table+"数据库！")

    def save_every_car_url(self, table, every_car_url):
        print("save to db[every_car_url]")
        data_len = len(every_car_url)
        for item in every_car_url:
            db[table].save(item)
        print("共存入" + str(data_len) + "条数据到" + table + "数据库！")

    def save_car_detail(self, table, table_dict):
        db[table].save(table_dict)
        print("存入1条数据到" + table + "数据库！")

    def save_failed_url(self, table, url_dict):
        db[table].save(url_dict)
        print("存入1条数据到" + table + "数据库！")