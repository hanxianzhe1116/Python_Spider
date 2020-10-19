import requests
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def get_page(url):
    headers = {
        'Host': 'www.qichacha.com',
        'Connection': 'keep-alive',
        'Accept': r'text/html, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': r'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36',
        'Referer': url,
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': r'QCCSESSID=e5p9ilq02rumugqvs3u9nluhq0; UM_distinctid=17418f7ea42b19-0d1c421836594e-3323766-144000-17418f7ea43c3b; zg_did=%7B%22did%22%3A%20%2217418f7ea4aada-0fbb3a5a2802c4-3323766-144000-17418f7ea4b35c%22%7D; hasShow=1; _uab_collina=159814673495149456757532; Hm_lvt_78f134d5a9ac3f92524914d0247e70cb=1598146735; acw_tc=7ca3c39b15981625389884879eb489fa20e6a1fba05c5c17aa67dc1032; zg_faa71dba513e47e2b1742e346e8fdf66=%7B%22sid%22%3A%201598162588722%2C%22updated%22%3A%201598162588763%2C%22info%22%3A%201598162588723%2C%22superProperty%22%3A%20%22%7B%5C%22%E5%BA%94%E7%94%A8%E5%90%8D%E7%A7%B0%5C%22%3A%20%5C%22%E9%A3%8E%E6%8E%A7%E7%AE%A1%E5%AE%B6WEB%E7%AB%AF%5C%22%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22cuid%22%3A%20%22863ecd06fc2290ee4a77f91e24a64c0b%22%7D; CNZZDATA1254842228=1028978580-1598146299-https%253A%252F%252Fwww.baidu.com%252F%7C1598158227; zg_de1d1a35bfa24ce29bbf2c7eb17e6c4f=%7B%22sid%22%3A%201598160737316%2C%22updated%22%3A%201598163048654%2C%22info%22%3A%201598146734673%2C%22superProperty%22%3A%20%22%7B%7D%22%2C%22platform%22%3A%20%22%7B%7D%22%2C%22utm%22%3A%20%22%7B%7D%22%2C%22referrerDomain%22%3A%20%22www.qcc.com%22%2C%22zs%22%3A%200%2C%22sc%22%3A%200%2C%22cuid%22%3A%20%22863ecd06fc2290ee4a77f91e24a64c0b%22%7D; Hm_lpvt_78f134d5a9ac3f92524914d0247e70cb=1598163049',
    }
    try:
        # header = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
        # time.sleep(1.5)
        res = requests.get(url, headers)
        if res.status_code == 200:
            print(res.text)
            return res.text
    except:
        time.sleep(10)


def get_company(url):
    a_list = ''
    try:
        page_text = get_page(url)
        soup = BeautifulSoup(page_text, 'lxml')
        com = soup.find_all(name="div", attrs={"class": "proinv-wrap"})
        print(com)
        # a_list = com.find('a')
        # print(a_list.get('href'))
    except:
        print("咱也不知道啥问题！我擦！")


if __name__ == '__main__':
    url1 = 'https://www.qcc.com/search?key='
    key_list = ['导航犬']
    # driver = webdriver.Chrome()
    # driver.get('https://www.tianyancha.com/login')
    # driver.find_element_by_xpath('//div[@class="title"]').click()
    # time.sleep(2)
    #
    # driver.find_element_by_id('mobile').send_keys('15568877056')
    # driver.find_element_by_id('password').send_keys('jc11160610')
    # # driver.find_element_by_xpath('//div[@class="btn -xl btn-primary -block"]').click()
    # # time.sleep(10)
    for k in key_list:
        url = url1 + k
        get_company(url)
