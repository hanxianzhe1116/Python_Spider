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
table = db['cars_info']

# def get_table():
data = pd.DataFrame(list(table.find()))
# print(data.columns)
df = data[["售价", "新车售价"]]
# print(df.head())
data.to_excel("cars_info.xlsx", index=False)