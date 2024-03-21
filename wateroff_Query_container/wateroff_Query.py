from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import requests

import time
import os

url="https://wateroffmap.water.gov.tw/wateroffmap/map/search"
service = Service(executable_path=ChromeDriverManager().install())

# 這些建議都加上，不開頁面、禁用GPU加速等等
options = webdriver.ChromeOptions()
options.add_argument("--headless")  
options.add_argument("--disable-gpu") 
options.add_argument("--disable-extensions")
options.add_argument("--disable-infobars")
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=service, options=options)

"""
print("Chrome version:", driver.capabilities['browserVersion'])
print("ChromeDriver version:", driver.capabilities['chrome']['chromedriverVersion'])
"""

driver.get(url)

address=os.environ.get('ADDRESS',"雲林縣斗六市大學路三段123號")

query_output=""

def query_time():
    #print("執行query_time")
    begin_date=driver.find_element("xpath","/html/body/div/div/div[1]/div[1]/div[3]/div/div[2]/div[2]")
    begin_time=driver.find_element("xpath","/html/body/div/div/div[1]/div[1]/div[3]/div/div[2]/div[3]")
    print("供水時間:",begin_date.text,begin_time.text)
    
    end_date=driver.find_element("xpath","/html/body/div/div/div[1]/div[1]/div[3]/div/div[3]/div[2]")
    end_time=driver.find_element("xpath","/html/body/div/div/div[1]/div[1]/div[3]/div/div[3]/div[3]")
    print("結束時間:",end_date.text,end_time.text)
    
    return "供水時間:{} {}\n結束時間:{} {}\n".format(begin_date.text,begin_time.text,end_date.text,end_time.text)

def water_shutdown():
    texts = driver.find_element("xpath", "/html/body/div/div/div[1]/div[1]/div[3]/div/div[4]/div[2]")
    
    if texts.text!="":
        print("查詢結果為:停水")
        times=query_time()
        print("停水地區:",texts.text)
        output_water_shutdown="查詢結果為:停水\n{}停水地區:{}\n".format(times,texts.text)
        return output_water_shutdown
    return ""

def water_pressurize():
    texts = driver.find_element("xpath", "/html/body/div/div/div[1]/div[1]/div[3]/div/div[6]/div[2]")
    
    if texts.text!="":
        print("查詢結果為:降壓")
        times=query_time()
        print("降壓地區:",texts.text)
        output_water_shutdown="查詢結果為:降壓\n{}降壓地區:{}\n".format(times,texts.text)
        return output_water_shutdown
    return ""

run_date=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print("查詢時間:",run_date)

#輸入地址
search=driver.find_element('xpath','/html/body/div/div/div[1]/div[1]/div/div[2]/div[2]/input')
search.send_keys(address)

#查詢確認
query_button=driver.find_element('xpath','/html/body/div/div/div[1]/div[1]/div/div[4]/div[1]/a')
query_button.click()

#確認是否正常供水
output_of_normal = driver.find_element('xpath',"/html/body/div[1]/div/div[1]/div[2]/div/div[1]/span")

#time.sleep(5)等待網頁載入完成才能找到目標元素
time.sleep(5)
if output_of_normal.text=="查無案件":
    query_output="查詢結果為:正常供水"
    print("查詢結果為:正常供水")
else:
    query_output+=water_shutdown()
    query_output+=water_pressurize()

driver.quit()
print("查詢結束")