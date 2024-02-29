from selenium import webdriver
import requests
from selenium.webdriver.support.ui import Select
import gspread

import time

# 全家

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 

# 程式開始

# 登入

driver = webdriver.Chrome() # 登入網頁
driver.get("https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip123/query")

# 登入身分證字號

identity_button = driver.find_element(By.CLASS_NAME, "custIdType")
time.sleep(1)  
identity_button.click()

identity = "N222837452" # 將身分證字號
identity_input = driver.find_element(By.ID, "pid")
identity_input.send_keys(identity)
time.sleep(1)  

#輸入起程站
start = "1000-臺北" # 起程站
start_input = driver.find_element(By.ID, "startStation1")
start_input.send_keys(start)
time.sleep(1)  

#輸入抵達站
end = "4220-臺南" # 抵達站
end_input = driver.find_element(By.ID, "endStation1")
end_input.send_keys(end)
time.sleep(1) 

#輸入日期
date = "2024/02/29" # 日期
date_input = driver.find_element(By.ID, "rideDate1")
date_input.send_keys(date)
time.sleep(1)  

#輸入票數
nub = "1" # 票數
nub_input = driver.find_element(By.ID, "normalQty1")
nub_input.clear()
nub_input.send_keys(nub)
time.sleep(1)  

#輸入車次
tr_num = "123" # 車次
tr_num_input = driver.find_element(By.ID, "trainNoList1")
tr_num_input.clear()
tr_num_input.send_keys(tr_num)
time.sleep(1)  

#輸入座位偏好
seat_pre = "不指定" # 座位偏好
if seat_pre == "不指定":
    # seat_pre_button = driver.find_element(By.ID, "seatPref1")
    seat_pre_button = driver.find_elements(By.CLASS_NAME, "btn btn-lg btn-linear active")[0]
    time.sleep(1)  
    seat_pre_button.click()
elif seat_pre == "靠窗":
    seat_pre_button = driver.find_element(By.ID, "seatPref2")
    seat_pre_button.click()
    time.sleep(1)  
elif seat_pre == "靠走道":
    seat_pre_button = driver.find_element(By.ID, "seatPref3")
    seat_pre_button.click()
    time.sleep(1) 
elif seat_pre == "桌型座優先":
    seat_pre_button = driver.find_element(By.ID, "seatPref4")
    seat_pre_button.click()
    time.sleep(1) 

#查詢建
login_button = driver.find_element(By.CLASS_NAME, "btn btn-3d")
time.sleep(1) 
login_button.click()
time.sleep(2) 

input()

 