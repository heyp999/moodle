from selenium import webdriver
option = webdriver.ChromeOptions()
# 无头模式
option.add_argument('headless')
# 沙盒模式运行
option.add_argument('no-sandbox')
# 大量渲染时候写入/tmp而非/dev/shm
option.add_argument('disable-dev-shm-usage')
# 指定驱动路径
browser = webdriver.Chrome( options=option)
# 访问百度
browser.get('http://www.baidu.com/')
# 打印标题
print(browser.title)
# 访问google
browser.get('https://github.com/heyp999/moodle')
print(browser.title)
# 关闭浏览器
browser.quit()
