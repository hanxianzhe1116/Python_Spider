import requests
import re
import json
import csv
from urllib.parse import urlencode
import datetime
import time

'''
函数说明：输入url及其参数
params:
    baseUrl:最开始的url
    cityCode:城市编码，这里我选择的是重庆，重庆编码：132
    roadType:道路类型
    callBack:返回类型
'''
def getPage(baseUrl,cityCode,roadType,callBack):
    #headers信息

    params = {
        'cityCode' : cityCode,
        'roadtype' : roadType,
        'callback' : callBack
    }
    url = baseUrl + urlencode(params)   #获取到url参数
    # print(requests.get(url).text)
    try:
        response = requests.get(url)
        if response.status_code == 200: #返回成功
            return response
    except requests.ConnectionError as e:
        print('url出错',e.args)

if __name__ == '__main__':
    url = 'https://jiaotong.baidu.com/trafficindex/city/roadrank?'
    #
    with open('transformData.csv','w') as f:
        f_csv = csv.writer(f)
        #保存五十分钟的数据
        for i in range(10):
            response = getPage(url,132,0,'jsonp_1553486162746_179718')
            # print(type(response.text))
            transformData = json.loads(re.findall(r'^\w+\((.*)\)$',response.text)[0])
            transformData = transformData.get('data').get('list')
            dateTime = datetime.datetime.now().strftime('%Y-%m-%d')
            f_csv.writerow(str(dateTime))
            dataList = []
            for item in transformData:
                # print(item)
                list = []
                list.append(item.get('roadname'))
                list.append(item.get('index'))
                list.append(item.get('speed'))
                dataList.append(list)

                # print(datetime.datetime.now().strftime('%Y-%m-%d'))
            f_csv.writerows(dataList)
            print(dataList)
            time.sleep(5)
    # f_csv.close()
