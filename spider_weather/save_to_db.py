from spider_weather.config import *
import pymongo
client = pymongo.MongoClient(MONGO_URL, MONGO_PORT)
db = client[MONGO_DB]


def save_everyday_weather(table, everyday_weather_dict_list):
    print("save to db[everyday_weather]")
    data_len = len(everyday_weather_dict_list)
    for item in everyday_weather_dict_list:
        db[table].save(item)
    print("共存入" + str(data_len) + "条数据到" + table + "数据库！")


def save_everyday_detail_weather(table, everyday_detail_weather_dict_list):
    print("save to db[everyday_detail_weather_dict_list]")
    data_len = len(everyday_detail_weather_dict_list)
    for item in everyday_detail_weather_dict_list:
        db[table].save(item)
    print("共存入" + str(data_len) + "条数据到" + table + "数据库！")


def save_all_year_weather(table, all_year_weather_dict_list):
    print("save to db[all_year_weather]")
    data_len = len(all_year_weather_dict_list)
    for item in all_year_weather_dict_list:
        db[table].save(item)
    print("共存入" + str(data_len) + "条数据到" + table + "数据库！")