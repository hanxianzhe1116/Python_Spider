import requests
from bs4 import BeautifulSoup


class Get_City_Url:
    def __init__(self, url):
        self.url = url
    """
        :param url:str, 用来抓取页面文本的url
        :return res.text:str, 返回页面文本
    """
    def get_page(self, url):
        try:
            res = requests.get(url)
            if res.status_code == 200:
                # print(res.text)
                return res.text
        except:
            print("url出错了！")

    def get_city_url(self):
        url_list = []
        url_dict = []
        page_text = self.get_page(self.url)
        soup = BeautifulSoup(page_text, 'lxml')
        div = soup.find_all(name="div", attrs={"class": "area-city-letter"})
        soup2 = BeautifulSoup(str(div), 'lxml')
        urls = soup2.find_all(name="a")
        for u in urls:
            url_list.append((u.get('href'), u["rrc-event-expand-tag_value"]))
        print("共抓取到"+str(len(url_list))+"条url链接！")
        city_url_list = []
        for u in url_list:
            city_url_list.append(["https://www.renrenche.com" + u[0] + "ershouche/", u[1]])
        for u in city_url_list:
            pagecount = self.get_pagecount(u[0])
            url_dict.append({"city_url": u[0], "city_name": u[1], "page_count": pagecount})
            u.append(pagecount)
        return city_url_list, url_dict

    def get_pagecount(self, url: str):
        try:
            page_text = self.get_page(url)
            soup = BeautifulSoup(page_text, 'lxml')
            ul = soup.find_all(name="ul", attrs={"class": "pagination js-pagination"})
            soup2 = BeautifulSoup(str(ul), 'lxml')
            pagecount = soup2.find_all(name="li")
            page = BeautifulSoup(str(pagecount[-2]), 'lxml')
            a_content = page.find_all(name='a')[0].string
            # print(a_content)
            # for item in page.find_all("a"):
            #     print(item.string)
            return int(a_content)
        except Exception as res:
            return 0
