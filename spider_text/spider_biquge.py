import sys
import requests
from bs4 import BeautifulSoup


class downloader(object):


    # 笔趣阁 目标url
    def __init__(self):
        self.target = 'https://www.biqukan.com/15_15998/'
        self.server = 'https://www.biqukan.com'
        self.name = []
        self.urls = []
        self.nums = 0

    '''
        获取目标网页
    '''
    # def get_page(url):
    #     response = requests.get(url)
    #     response.encoding = 'gbk'
    #     if response.status_code == 200:
    #         return response.text
    #     return None
    #     # print(response.text)


    '''
        获取单个章节
    '''
    def get_text(self, target):
        #print(target)
        target_text = requests.get(url = target)
        target_text.encoding = 'gbk'
        html = target_text.text
        soup = BeautifulSoup(html, 'lxml')
        show_txt = soup.find_all('div', class_='showtxt')
        #print(show_txt)
        show_txt = show_txt[0].text.replace('\xa0' * 8, '')
        return str(show_txt)


    '''
        解析目标网页
    '''
    def parse_page(self):
        response = requests.get(self.target)
        response.encoding = 'gbk'
        html = response.text
        soup = BeautifulSoup(html, 'lxml')
        listmain = soup.find_all('div', class_='listmain')
        a_ = BeautifulSoup(str(listmain[0]))
        a = a_.find_all('a')
        #self.nums = len(a[12:])
        self.nums = len(a[900:])
        print(self.nums)
        for eacha in a[900:]:
            self.name.append(eacha.string)
            self.urls.append(self.server+eacha.get('href'))
            # print(eacha.string, server+eacha.get('href'))
        # print(listmain[0])


    '''
        写入txt
    '''
    def write_to_file(self, name, path, show_txt):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(show_txt)
            f.write('\n\n')


if __name__ == '__main__':
        dl = downloader()
        dl.parse_page()
        print('《女总裁的全能兵王》开始下载：')
        # print(nums)
        #print(str(dl.nums)+"#####")
        for i in range(dl.nums):
            #print(1)
            dl.write_to_file(dl.name[i], '女总裁的全能兵王.txt', dl.get_text(dl.urls[i]))
            sys.stdout.write("已下载:%.3f%%" % float(i/dl.nums*100) + '\r')
            sys.stdout.flush()
        print('《女总裁的全能兵王》下载完成')