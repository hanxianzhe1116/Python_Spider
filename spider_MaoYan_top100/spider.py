import json
from multiprocessing import Pool
import requests
from requests.exceptions import RequestException
import re


def get_one_page(url):
    try:
        param = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
        }
        response = requests.get(url, headers=param)
        if response.status_code == 200:
            return response.text
        # print(response.status_code)
        return None
    except RequestException:
        return None


def parse_one_page(html):
    # pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name">'
    #                    + '<a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>'
    #                    + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)

    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'image': item[1],
            'title': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }
    # print(items)


def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')
        f.close()


def main(offset):
    url = "https://maoyan.com/board/4?offset=" +str(offset)
    html = get_one_page(url)
    # parse_one_page(html)
    for item in parse_one_page(html):
        write_to_file(item)
        print(item)
    # print(html)


if __name__ == '__main__':
    # for i in range(10):
    #   main(i*10)
    pool = Pool()
    pool.map(main, [i*10 for i in range(10)])
