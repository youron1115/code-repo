import random
import numpy as np

import matplotlib.pyplot as plt

def set_prize():
    
    prize = np.random.randint(0,3,1) # 生成1-3的隨機數，1個
    """
    prize_list=[0,0,0]
    for i in range(3):
        if i==prize:
            prize_list[i]=1
    print("獎品列:",prize_list)#1為獎品
    """
    return prize

       
def set_first_choice():
    choice =np.random.randint(0,3,1) # 生成1-3的隨機數，1個
    #print("第一次選擇: 第",choice," 扇門")
    return choice

def open_goat_door(prize_location,first_choice):
    for i in range(3):
        if i!=prize_location and i!=first_choice:
            #print("打開第",i,"扇:山羊門")
            return i

def change_choice(): 
    choice =np.random.randint(0,2,1) # 生成0/1(不換/換)
    """
    if choice:
        #print("換門")
    else:
        #print("不換門")
    """
    return choice

def set_final_choice(goat_door,first_choice,change):
    if change:
        for i in range(3):
            if i!=goat_door and i!=first_choice:
                #print("第二次選擇: 第",i," 扇門")
                return i
    else:
        #print("第二次選擇: 第",first_choice," 扇門")
        return first_choice

def monty_hall(times):
    print("\nMonty Hall 問題 with ",times," times")
    prize_time_with_change=0
    prize_time_with_not_change=0
    goat_time=0
    goat_time_with_change=0
    
    for _ in range(times):
        s_p=set_prize()#設定獎品位置
        FirstChoice=set_first_choice()#選擇其一(第一次選擇)
        
        goat_1=open_goat_door(s_p,FirstChoice)#打開一扇山羊門
        change_or_not=change_choice()#是否換門
        FinalChoice=set_final_choice(goat_1,FirstChoice,change_or_not)#最終選擇
        if FinalChoice==s_p:
            #print("恭喜你獲得獎品")
            if change_or_not:
                prize_time_with_change+=1
            else:
                prize_time_with_not_change+=1
        else:
            if change_or_not:
                goat_time_with_change+=1
            else:
                goat_time+=1
            #print("恭喜你獲得山羊")
            
    print("\n換門獲得獎品次數:",prize_time_with_change,"機率為:",prize_time_with_change/times)
    print("不換門獲得獎品次數:",prize_time_with_not_change,"機率為:",prize_time_with_not_change/times)
    print("換門獲得山羊次數:",goat_time_with_change,"機率為:",goat_time_with_change/times)
    print("不換門獲得山羊次數:",goat_time,"機率為:",goat_time/times)
    
    plt.title('Monty Hall problem with '+str(times)+' times')
    plt.xlabel('change or not')
    plt.ylabel('probability')
    plt.bar(['change','not change'],[prize_time_with_change/times,prize_time_with_not_change/times])
    plt.show()
times_set=1000
monty_hall(times_set)
        
times_set=10000
monty_hall(times_set)

times_set=100000
monty_hall(times_set)