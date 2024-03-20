from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import requests

import time

url="https://wateroffmap.water.gov.tw/wateroffmap/map/search"
driver=webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)

token='op5pgVh67ROewXEYzgB7vyaz39k4cchVeR3G1WjD1z5'
address="雲林縣斗六市大學路三段123號"

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
        time=query_time()
        print("停水地區:",texts.text)
        output_water_shutdown="查詢結果為:停水\n{}停水地區:{}\n".format(time,texts.text)
        return output_water_shutdown
    return ""

def water_pressurize():
    texts = driver.find_element("xpath", "/html/body/div/div/div[1]/div[1]/div[3]/div/div[6]/div[2]")
    
    if texts.text!="":
        print("查詢結果為:降壓")
        time=query_time()
        print("降壓地區:",texts.text)
        output_water_shutdown="查詢結果為:降壓\n{}降壓地區:{}\n".format(time,texts.text)
        return output_water_shutdown
    return ""

def lineNotifyMessage_msg(para_token,para_msg):
    headers={
        "Authorization":"Bearer "+ para_token,
        #"Content-Type":"application/x-www-form-urlencoded"
    }
    payload={'message':para_msg}
    r=requests.post("https://notify-api.line.me/api/notify",headers=headers,params=payload)
    #print(r.status_code)
    return r.status_code

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

#time.sleep(5)目的是等待網頁載入完成
time.sleep(5)
if output_of_normal.text=="查無案件":
    query_output="查詢結果為:正常供水"
    print("查詢結果為:正常供水")
else:
    query_output+=water_shutdown()
    query_output+=water_pressurize()

driver.quit()
print("查詢結束")
msg="\n查詢時間為:{}\n查詢地址為:\n{}\n{}".format(run_date,address,query_output)

lineNotifyMessage_msg(token,msg)