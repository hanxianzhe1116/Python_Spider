url = 'http://jiaotong.baidu.com/top/report/?citycode=53'
import time
from selenium import webdriver
from bs4 import BeautifulSoup
def get_html(url):
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(30)
    html = driver.page_source

    soup = BeautifulSoup(html, 'lxml')
    content = soup.find(name='div', class_='city-info')
    content = str(content)
    soup1 = BeautifulSoup(content, 'lxml')
    province_name = soup1.find(name='span', class_='province-name')
    city_name = soup1.find(name='span', class_='city-name')
    container3 = soup.find(name='div', class_='container3')
    container3 = str(container3)
    soup2 = BeautifulSoup(container3, 'lxml')
    table = soup2.find(name='table', class_='table clearfix open')
    soup3 = BeautifulSoup(str(table), 'lxml')
    thead = soup3.find(name='thead')
    soup4 = BeautifulSoup(str(thead), 'lxml')
    th = soup4.find_all(name='th')
    table_list = [[]]
    # print(table_list)
    for t in th:
        table_list[0].append(t.text.replace(u'\xa0', u' '))
    tbody = soup3.find(name='tbody')
    soup5 = BeautifulSoup(str(tbody), 'lxml')
    tr = soup5.find_all(name='tr')
    for tr in tr:
        soup6 = BeautifulSoup(str(tr), 'lxml')
        td = soup6.find_all(name='td')
        list = []
        for td in td:
            list.append(td.text)
        table_list.append(list)
    # 输出实时道路拥堵指数
    for i in range(4):
        print(table_list[i])

    # 获取昨日早晚高峰
    container5 = soup.find(name='div', class_='container5')
    morning = BeautifulSoup(str(container5), 'lxml').find(name='div', class_='morning clearfix open')
    morning_hour = BeautifulSoup(str(morning), 'lxml').find(name='div', class_='hour').text
    morning_index = BeautifulSoup(str(morning), 'lxml').find(name='div', class_='index').text

    night = BeautifulSoup(str(container5), 'lxml').find(name='div', class_='night clearfix open')
    night_hour = BeautifulSoup(str(night), 'lxml').find(name='div', class_='hour').text
    night_index = BeautifulSoup(str(night), 'lxml').find(name='div', class_='index').text
    print('昨日早晚高峰')
    print(morning_hour+'  '+morning_index)
    print(night_hour+'  '+night_index)

####################################################################################################
    driver.find_element_by_xpath('//*[@id="content"]/div/div/div[7]/div[1]/div/ul[1]/li[1]/a').click()
    # 获取道路拥堵情况
    ul = soup.find(name='ul', class_='cc-datalist-list')
    button = BeautifulSoup(str(ul), 'lxml').find_all(name='button')

    road_list1 = []
    for b in button:
        td = BeautifulSoup(str(b), 'lxml').find_all(name='td')
        list = []
        for td in td:
            list.append(td.text)
            # print(td.text, end=' ')
        # print(end='\n')
        road_list1.append(list)
    # 输出道路拥堵情况
    for i in road_list1:
        print(i)
##########################################################################################
    driver.find_element_by_xpath('//*[@id="content"]/div/div/div[7]/div[1]/div/ul[1]/li[2]/a').click()
    # 获取道路拥堵情况
    ul = soup.find(name='ul', class_='cc-datalist-list')
    button = BeautifulSoup(str(ul), 'lxml').find_all(name='button')

    road_list2 = []
    for b in button:
        td = BeautifulSoup(str(b), 'lxml').find_all(name='td')
        list = []
        for td in td:
            list.append(td.text)
            # print(td.text, end=' ')
        # print(end='\n')
        road_list2.append(list)
    # 输出道路拥堵情况
    for i in road_list2:
        print(i)
##########################################################################################
    driver.find_element_by_xpath('//*[@id="content"]/div/div/div[7]/div[1]/div/ul[1]/li[3]/a').click()
    # 获取道路拥堵情况
    ul = soup.find(name='ul', class_='cc-datalist-list')
    button = BeautifulSoup(str(ul), 'lxml').find_all(name='button')

    road_list3 = []
    for b in button:
        td = BeautifulSoup(str(b), 'lxml').find_all(name='td')
        list = []
        for td in td:
            list.append(td.text)
            # print(td.text, end=' ')
        # print(end='\n')
        road_list3.append(list)
    # 输出道路拥堵情况
    for i in road_list3:
        print(i)
##########################################################################################
    x_path1 = '//*[@id="content"]/div/div/div[7]/div[1]/div/ul[1]/li[1]/a'
    x_path2 = '//*[@id="content"]/div/div/div[7]/div[1]/div/ul[1]/li[2]/a'
    x_path3 = '//*[@id="content"]/div/div/div[7]/div[1]/div/ul[1]/li[3]/a'
    # print(road_list1)
    # print('--------------------------------------------------')
    # print(road_list2)
    # print('--------------------------------------------------')
    # print(road_list3)
    # print('--------------------------------------------------')
    # print(province_name.text)
    # print(city_name.text)
    # print(table.text)
    # print(container5)
get_html(url)
