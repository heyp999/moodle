#!/usr/bin/env bash
import time
from selenium import webdriver
import os  
from selenium.webdriver.common.keys import Keys  

# "$ xvfb-run python test.py", this is how you run this script
chrome_options = webdriver.ChromeOptions()
# below trick saved my life
chrome_options.add_argument('--no-sandbox')

# set the folder where you want to save your file
prefs = {'download.default_directory' : os.getcwd()}
chrome_options.add_experimental_option('prefs', prefs)

# Optional argument, if not specified will search path.
driver = webdriver.Chrome('/usr/local/bin/chromedriver',chrome_options=chrome_options)  
chrome_options=chrome_options

# Scraping steps
driver.get("http://pypi.python.org/pypi/selenium")
time.sleep(3)
driver.find_element_by_css_selector("#content > div.section > table > tbody > tr.odd > td:nth-child(1) > span > a:nth-child(1)").click()
time.sleep(3)
print('Finished!')
driver.quit()
