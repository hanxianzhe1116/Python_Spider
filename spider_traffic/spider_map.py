import requests
import re
import json


def get_page(url):
    try:
        response = requests.get(url)
        if response.content:  # 返回成功
            return response
    except requests.ConnectionError as e:
        print('url出错', e.args)


def write_to_file(content):
    with open('长春市交通情况爬取.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False)+'\n')
        # f.close()


# 获取实时拥堵指数内容
def get_detail(page):
    # print(page.text)
    # page = {"detail":{"index":"1.61","last_index":"1.52","week_rate":0.059,"max_congest_day":"20191008","max_week_day":"2","max_index":"1.97"},"updatetime":"201910131755"}
    transformData = json.loads(re.findall(r'[(](.*?)[)]', page.text)[0])
    # transformData = transformData.get('data')
    # transformData = transformData.replace('\\', '')
    # return transformData
    detail = transformData['data']['detail']
    # print('实时拥堵指数数据：')
    for i in detail:
        write_to_file(str(i)+'：'+str(detail[i]))
        print(str(i)+'：'+str(detail[i]))
    # print(transformData['data']['detail'])


# 获取实时拥堵指数变化内容
def get_curve(page):
    # print(type(page))
    # print(page.text)
    # page = {"detail":{"index":"1.61","last_index":"1.52","week_rate":0.059,"max_congest_day":"20191008","max_week_day":"2","max_index":"1.97"},"updatetime":"201910131755"}
    transformData = json.loads(re.findall(r'[(](.*?)[)]', page.text)[0])
    # transformData = transformData.get('data')
    # transformData = transformData.replace('\\', '')
    # return transformData
    curve_detail = transformData['data']['list']
    k = 0
    for roadrank_list in curve_detail:
        print('---------------分割线---------------')
        print(k)
        write_to_file(str(k)+str(roadrank_list))
        k += 1
        print(roadrank_list)
    # print(curve_detail)


# 获取实时道路拥堵指数内容
def get_road(page):
    # print(type(page))
    # print(page.text)
    # page = {"detail":{"index":"1.61","last_index":"1.52","week_rate":0.059,"max_congest_day":"20191008","max_week_day":"2","max_index":"1.97"},"updatetime":"201910131755"}
    transformData = json.loads(re.findall(r'[(](.*?)[)]', page.text)[0])
    # transformData = transformData.get('data')
    # transformData = transformData.replace('\\', '')
    # return transformData
    detail = transformData['data']['detail']
    for i in detail:
        write_to_file(str(i)+'：'+str(detail[i]))
        print(str(i)+'：'+str(detail[i]))
    # print(transformData['data']['detail'])


# 获取实时拥堵里程内容
def get_congestmile(page):
    # print(type(page))
    # print(page.text)
    # page = {"detail":{"index":"1.61","last_index":"1.52","week_rate":0.059,"max_congest_day":"20191008","max_week_day":"2","max_index":"1.97"},"updatetime":"201910131755"}
    transformData = json.loads(re.findall(r'[(](.*?)[)]', page.text)[0])
    # transformData = transformData.get('data')
    # transformData = transformData.replace('\\', '')
    # return transformData
    congest = transformData['data']['congest']
    # print('获取实时拥堵里程内容：')
    for i in congest:
        write_to_file(str(i)+'：'+str(congest[i]))
        print(str(i)+'：'+str(congest[i]))
    # print(transformData['data']['detail'])


# 获取昨日早晚高峰内容
def get_peakCongest(page):
    # print(type(page))
    # print(page.text)
    # page = {"detail":{"index":"1.61","last_index":"1.52","week_rate":0.059,"max_congest_day":"20191008","max_week_day":"2","max_index":"1.97"},"updatetime":"201910131755"}
    transformData = json.loads(re.findall(r'[(](.*?)[)]', page.text)[0])
    # transformData = transformData.get('data')
    # transformData = transformData.replace('\\', '')
    # return transformData
    peak_detail = transformData['data']['peak_detail']
    # print('获取昨日早晚高峰内容：')
    for i in peak_detail:
        write_to_file(str(i)+'：'+str(peak_detail[i]))
        print(str(i)+'：'+str(peak_detail[i]))


# 获取全部道路拥堵情况
def get_roadrank(page):
    # print(type(page))
    # print(page.text)
    # page = {"detail":{"index":"1.61","last_index":"1.52","week_rate":0.059,"max_congest_day":"20191008","max_week_day":"2","max_index":"1.97"},"updatetime":"201910131755"}
    transformData = json.loads(re.findall(r'[(](.*?)[)]', page.text)[0])
    # transformData = transformData.get('data')
    # transformData = transformData.replace('\\', '')
    # return transformData
    roadrank_detail = transformData['data']['list']
    for roadrank_list in roadrank_detail:
        write_to_file('---------------分割线---------------')
        print('---------------分割线---------------')
        for element in roadrank_list:
            if str(element) != 'links' and str(element) != 'nameadd':
                write_to_file(str(element)+':'+str(roadrank_list[element]))
                print(str(element)+':'+str(roadrank_list[element]))
        # print(roadrank_list)
    # print(roadrank_detail)
    # print('获取昨日早晚高峰内容：')
    # for i in peak_detail:
    #     print(str(i) + '：' + str(peak_detail[i]))
    # print(transformData['data']['detail'])


if __name__ == '__main__':

    url = 'https://jiaotong.baidu.com/trafficindex/city/details?cityCode=53&callback=jsonp_1570959868686_520859'

    url_curve = 'https://jiaotong.baidu.com/trafficindex/city/curve?cityCode=53&type=minute&callback=jsonp_1571018819971_8078256'

    url_road = 'https://jiaotong.baidu.com/trafficindex/city/road?cityCode=53&callback=jsonp_1571014746541_9598712'

    url_congestmile = 'https://jiaotong.baidu.com/trafficindex/city/congestmile?cityCode=53&callback=jsonp_1571014746542_5952586'

    url_peakCongest = 'https://jiaotong.baidu.com/trafficindex/city/peakCongest?cityCode=53&callback=jsonp_1571014746543_3489265'

    url_roadrank = 'https://jiaotong.baidu.com/trafficindex/city/roadrank?cityCode=53&roadtype=0&callback=jsonp_1571016737139_1914397'

    url_highroadrank = 'https://jiaotong.baidu.com/trafficindex/city/roadrank?cityCode=53&roadtype=1&callback=jsonp_1571018628002_9539211'

    # 获取实时拥堵指数内容
    print('获取实时拥堵指数内容')
    write_to_file('获取实时拥堵指数内容')
    get_detail(get_page(url))

    # 获取实时拥堵指数变化内容
    print('获取实时拥堵指数变化内容')
    write_to_file('获取实时拥堵指数变化内容')
    get_curve(get_page(url_curve))

    # 获取实时道路拥堵指数内容
    print('获取实时道路拥堵指数内容')
    write_to_file('获取实时道路拥堵指数内容')
    get_road(get_page(url_road))

    # 获取实时拥堵里程内容
    print('获取实时拥堵里程内容')
    write_to_file('获取实时拥堵里程内容')
    get_congestmile(get_page(url_congestmile))

    # 获取昨日早晚高峰内容
    print('获取昨日早晚高峰内容')
    write_to_file('获取昨日早晚高峰内容')
    get_peakCongest(get_page(url_peakCongest))

    # 获取全部道路拥堵情况
    print('获取全部道路拥堵情况')
    write_to_file('获取全部道路拥堵情况')
    get_roadrank(get_page(url_roadrank))

    # 获取高速/快速路拥堵情况
    print('获取高速/快速路拥堵情况')
    write_to_file('获取高速/快速路拥堵情况')
    get_roadrank(get_page(url_highroadrank))