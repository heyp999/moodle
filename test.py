from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

DRIVER_PATH ="/usr/local/bin/chromedriver"


if __name__ == "__main__":
    # 设置浏览器
    options &#61; Options()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")  # 无头参数
    options.add_argument("--disable-gpu")
    # 启动浏览器
    driver &#61; Chrome(executable_path&#61;DRIVER_PATH, options&#61;options)
    # 访问目标URL
    driver.get("https://www.baidu.com/")
    print(driver.page_source)
    driver.close()
    driver.quit()
