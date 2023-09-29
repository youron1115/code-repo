from selenium import webdriver
import time
import requests
import datetime
tonow = datetime.datetime.now()
report = []

driverPath='C:/Users/USER/Downloads/chromedriver.exe'
browser=webdriver.Chrome(driverPath)

url='https://www.cwb.gov.tw/V8/C/K/astronomy_month.html'
token='odMPVZ1ltX9x7bn1QwioDXp9B3X8bXmA5ohNGvKa9Sj'

def star():
    reformat = ''  
    year=tonow.year
    month=str(tonow.month)
    report.append(year) 
    report.append(month)
    
    browser.get(url)
    browser.maximize_window()
    time.sleep(3)
    button=browser.find_element('xpath','//*[@id="calendar"]/div[1]/ul/li[2]/a')
    button.click()
    time.sleep(3)
    
    #本月天文現象
    tits=browser.find_elements('xpath','//*[@class="as-title"]//*[@class="date"]')
    times=0
    for i in tits:
        times+=1
    tits=browser.find_elements('xpath','//*[@class="as-title"]')
    
    num=1
    
    for i in tits:
        if times<=0:
            break
        #把標題加進暫存字串中
        reformat += "\n\n"
        reformat += i.text
        print(num)
        print(i.text)
        print("\n")
        times-=1
        num+=1
    report.append(reformat)
    
    #下個月天文現象
    button=browser.find_element('xpath','/html/body/div[3]/main/div/div/div/div[1]/div[1]/div[2]/div/button[2]')
    button.click()
    time.sleep(3)
    
    tits=browser.find_elements('xpath','//*[@class="as-title"]//*[@class="date"]')
    times=0
    for i in tits:
        times+=1
    tits=browser.find_elements('xpath','//*[@class="as-title"]')
    
    #計算月份與進位
    month = (tonow.month+1)%12  
    if(((tonow.month+1)/12)==1):
        year += 1
    report.append(year) 
    report.append(month)
    
    #清空暫存字串
    reformat = ''
    num=1
    if times>0:
        for i in tits:
            if times<=0:
                break
            reformat +="\n\n"
            reformat += i.text
            print(num)
            print(i.text)
            print("\n")
            times-=1
            num+=1
        report.append(reformat)
    else:
        print("查無資料") 
        report.append("查無資料")
        
    #展開report，照索引值依序放入{}
    reformat = "\n{}年{}月天文現象:{}\n===============\n{}年{}月天文現象:\n{}".format(*report)
    lineNotifyMessage_msg(token,reformat) 
    browser.close()

def lineNotifyMessage_msg(token,msg):
    headers={
        "Authorization":"Bearer "+ token,
        #"Content-Type":"application/x-www-form-urlencoded"
    }
    payload={'message':msg}
    r=requests.post("https://notify-api.line.me/api/notify",headers=headers,params=payload)
    #print(r.status_code)
    return r.status_code
  
star()