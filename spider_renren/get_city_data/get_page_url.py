import pandas as pd
import pymongo
from spider_renren.get_city_data.config import *
from spider_renren.get_city_data.save_to_db import *


# 连接数据库
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
table = db['city_url']


def get_page_url():
    data = pd.DataFrame(list(table.find()))
    data = data[["city_url", "city_name", "page_count"]]
    data = data[data["page_count"] > 0]
    page_dict = []
    for i in data.index:
        for p in range(1, data.loc[i][2] + 1):
            page_dict.append({"page_url": data.loc[i][0] + 'p' + str(p), "city_name": data.loc[i][1]})
    return page_dict


if __name__ == '__main__':
    # print(get_page_url())
    save_page_url = SaveData()
    save_page_url.save_page_url("page_url", get_page_url())

