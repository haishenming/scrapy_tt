
# 通过selenium拿到cookie

from selenium import webdriver


brower = webdriver.Chrome()


brower.get("http://www.baidu.com")

Cookie = brower.get_cookies()


print(Cookie)

brower.close()