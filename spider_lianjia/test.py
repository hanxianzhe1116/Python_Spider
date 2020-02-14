import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import re
import xlwt
from multiprocessing import Pool

target = 'https://lz.lianjia.com/ershoufang/106103461406.html'


def get_house_id(url):
    # print("111")

    # url = 'https://bj.lianjia.com/ershoufang/'
    header = {'Accept': 'application/json, text/javascript, */*; q=0.01',
              'Accept-Encoding': 'gzip, deflate, br',
              'Accept-Language': 'zh-CN,zh;q=0.9',
              'Connection': 'keep-alive',
              'Cookie': 'lianjia_uuid=81095082-83c4-4d24-b69c-e8d2df958489; _smt_uid=5d916e6b.4cc2c9ff; UM_distinctid=16d801753c83ba-030b367822c8b5-67e1b3f-144000-16d801753c98f8; _ga=GA1.2.360699290.1569812078; digv_extends=%7B%22utmTrackId%22%3A%2221583074%22%7D; _jzqa=1.607157400828764900.1569812076.1569812076.1570192425.2; _jzqc=1; _jzqckmp=1; _gid=GA1.2.1375638494.1570192427; all-lj=3d8def84426f51ac8062bdea518a8717; CNZZDATA1255633284=1807001504-1570191787-https%253A%252F%252Fwww.lianjia.com%252F%7C1570191787; _qzjc=1; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1570192464; select_city=620100; CNZZDATA1255604082=801302758-1570188405-https%253A%252F%252Fwww.lianjia.com%252F%7C1570190403; lianjia_ssid=20131468-c944-4927-bb40-d7849061b217; _jzqy=1.1569812076.1570194487.2.jzqsr=baidu|jzqct=%E9%93%BE%E5%AE%B6.jzqsr=baidu; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216d8017555f275-03db659049335c-67e1b3f-1327104-16d80175560562%22%2C%22%24device_id%22%3A%2216d8017555f275-03db659049335c-67e1b3f-1327104-16d80175560562%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%2C%22%24latest_referrer_host%22%3A%22www.baidu.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_utm_source%22%3A%22baidu%22%2C%22%24latest_utm_medium%22%3A%22pinzhuan%22%2C%22%24latest_utm_campaign%22%3A%22sousuo%22%2C%22%24latest_utm_content%22%3A%22biaotimiaoshu%22%2C%22%24latest_utm_term%22%3A%22biaoti%22%7D%7D; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNThhMjdhMzczYWViZTY5MWY4Njg3N2U2MzFjYjM3NGM4YTBjMjVkMjc1M2Q1ODE3Njk1YTFmYTRjZWViMWRhOTA1Y2Y0ZDc2MzI0NTQ5ODM1ZjlmZWFlODFiYTQ4MzRiY2Q5NGNmYjQ4ODdiYmJiODA2OWE1M2Y4YTRmODFmMDQ0YjJkNmRmMzg1N2ZiNTQ1Y2I3ZmI0MzMzMTllZGI1ZTIyMWU2MjljODIyMjQyNTJiMmE5MTVkNTIyNmNlN2Q1Njk3YWI0MTBjYzdmOTdhYTVkYzA0Njc1NTdmN2FlZTU1MTEzMzdkZDU4OWQ2NDZiMmE4NjE1ZDkxZjMyYWI2ZmUzOGNkMGQ0M2YyYTZlODA4ZTU4MzViYjBjNGRlNjYzYmYwZmU5OGQ4NGNmNWYzNWZlN2IwYzY2YzA1ZDY5NGZjMzExMjIyZmFjZjE1NmVjODhlOGYzNzkyNGExMTUxZlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJmZDUyMjlhNFwifSIsInIiOiJodHRwczovL2x6LmxpYW5qaWEuY29tL2Vyc2hvdWZhbmcvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1570194653; CNZZDATA1254525948=1965425289-1570188605-https%253A%252F%252Fwww.lianjia.com%252F%7C1570189464; _qzja=1.395786867.1570192438534.1570192438534.1570192438534.1570194491366.1570194653228.0.0.0.25.1; _qzjb=1.1570192438534.25.0.0.0; _qzjto=25.1.0; _jzqb=1.27.10.1570192425.1',
              'Host': 'lz.lianjia.com',
              'Referer': 'https://lz.lianjia.com/ershoufang/',
              'Sec-Fetch-Mode': 'cors',
              'Sec-Fetch-Site': 'same-origin',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36',
              'X-Requested-With': 'XMLHttpRequest',
              'X-Tingyun-Id': 'gVpxXPG41PA;r=194653284'
              }
    res = requests.get(url=url, headers=header)
    # print(res.status_code)
    if res.status_code == 200:
        # print(res.text)
        return res.text


def parse_page(page_text, a_list):
    # page_text = get_house_id()
    soup = BeautifulSoup(page_text, 'lxml')
    # urls_data = soup.findAll(name="div", attrs={"class": "item"})
    urls_data = soup.find_all(name="a", attrs={"class": "noresultRecommend"})
    for i in urls_data:
        a_list.append(i.get('href'))
        # print(i.get('href'))
    return a_list

def get_url():
    # get_house_id()
    a_list = []
    url = 'https://lz.lianjia.com/ershoufang/pg'
    cou = 1
    for page in range(1, 101):
        print(cou)
        cou += 1
        parse_page(get_house_id(url+str(page)), a_list)
    # print(a_list)
    # print(len(a_list))
    return a_list


def get_details(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"}
    res = requests.get(url=url, headers=header)
    # print(res.status_code)
    # print(res.status_code)
    if res.status_code == 200:
        # print(res.text)
        return res.text


def parse_details(html):
    soup = BeautifulSoup(html, 'lxml')
    text = soup.find(name='div', class_='base')
    soup = BeautifulSoup(str(text), 'lxml')
    li = soup.findAll(name='li')
    details_list = []
    for i in li:
        matchObj = re.match(r'<li>(.*?)</span>(.*?)</li>', str(i), re.M | re.I)
        # 输出房屋属性
        # print(matchObj.group(2))
        details_list.append(matchObj.group(2))
    # 房屋总价及每平米价格
    soup = BeautifulSoup(html, 'lxml')
    price = soup.find(name='div', class_='price')
    total = BeautifulSoup(str(price), 'lxml')
    total_price = total.find(name='span', class_='total')
    unit = total.find(name='span', class_='unit')
    totalPrice = total_price.text+unit.text
    details_list.append(totalPrice)
    # print(totalPrice)
    unit_price = total.find(name='div', class_='unitPrice')
    # print(unit_price.text)
    details_list.append(unit_price.text)

    # 房屋所在区域
    soup1 = BeautifulSoup(html, 'lxml')
    area = soup1.find(name='div', class_='areaName')
    area_info = BeautifulSoup(str(area), 'lxml')
    areaInfo = area_info.find(name='span', class_='info')
    details_list.append(areaInfo.text)
    return details_list


def save_to_excel(details_list):
    # 创建工作workbook
    workbook = xlwt.Workbook()

    # 创建工作表worksheet,填入表名
    worksheet = workbook.add_sheet('兰州房价预测')
    # print(len(details_list)/15)
    # 在表中写入相应的数据
    k = 0
    for i in range(1, 3001):
        for j in range(0, 15):
            worksheet.write(i, j, details_list[k])
            k += 1
    # worksheet.write(1, 1, '你好')
    # 保存表
    workbook.save('lanzhou.xls')


def sprider():
    url_list = get_url()
    details_list = []
    # details_list += parse_details(get_details(url_list[0]))
    for url in url_list:
        # get_details(url)
        details_list += parse_details(get_details(url))
    print(len(details_list))
    save_to_excel(details_list)


sprider()