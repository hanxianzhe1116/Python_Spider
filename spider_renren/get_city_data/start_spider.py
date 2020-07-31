from spider_renren.get_city_data.save_to_db import *
from spider_renren.get_city_data.spider_city_url import Get_City_Url

if __name__ == '__main__':

    gcu = Get_City_Url("https://www.renrenche.com/bj/ershouche/?&plog_id=bb97445b3ce898dec2c3c0f4f4f85ea3")
    city_url_list, city_url_dict = gcu.get_city_url()

    print(city_url_list, city_url_dict)
    print(len(city_url_list), len(city_url_dict))

    save_city_url = SaveData()
    save_city_url.save_city_url("city_url", city_url_dict)
