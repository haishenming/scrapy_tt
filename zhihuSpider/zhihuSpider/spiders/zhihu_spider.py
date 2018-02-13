import scrapy
from zhihuSpider.settings import COOKIES_PATH
from zhihuSpider.selenium_spider.selenium_tools import get_cookies

class ZhihuSpider(scrapy.Spider):
    name = "zhihu"

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://www.zhihu.com/"
    }

    def start_requests(self):
        Cookies = get_cookies()
        cookies_path = COOKIES_PATH

        cookie_dict = {}
        for cookie in Cookies:
            # 写入文件
            cookie_dict[cookie['name']] = cookie['value']

        urls = ["https://www.zhihu.com", ]

        for url in urls:
            yield scrapy.Request(url, headers=self.headers, cookies=cookie_dict)

    def parse(self, response):
        text = response.body

        with open("zhihu.html", "wb") as f:
            f.write(text)

        print(text)