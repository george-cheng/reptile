# -*- coding: UTF-8 -*-

import json
import re
import requests
from requests import RequestException


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def parse_page(html):
    pattern = re.compile(
        '<img.*?src="(.*?)".*?/>.*?<a.*?href="(.*?)".*?/>', re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'image': item[0],
            'href': item[1],
        }


def write_to_file(content):
    with open('bian.txt', 'a', encoding='utf-8')as f:
        # print(type(json.dumps(content)))
        f.write(json.dumps(content, ensure_ascii=False))


def main():
    url = "http://pic.netbian.com/4kmeinv/"
    html = get_page(url)
    for item in parse_page(html):
        print(item)
        write_to_file(item)


if __name__ == '__main__':
    main()
