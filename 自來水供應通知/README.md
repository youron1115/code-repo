# WaterOff Query web crawler and notification

WaterOff Query is a web crawler and notification system that checks the status of water supply of location . It is a simple Python script that uses the `selenium` and `requests` libraries to scrape the [TAIWAN WATER COPORATION](https://wateroffmap.water.gov.tw/wateroffmap/map/search) website and send a notification to the user's LINE when wateroff_Query.py is being executed.

### Token of Line Notify
Change to the user's token by modifying the `token` variable.
```python
token='op5pgVh67ROewXEYzgB7vyaz39k4cchVeR3G1WjD1z5'#Variable token should be changed to the user's token.
```

### Query Location
Change the location of the query by modifying the `address` variable in the `wateroff_Query.py` file. The address initially set is the address of National Yunlin University of Science and Technology.
```python
address="雲林縣斗六市大學路三段123號"#Variable address should be changed to the user's address by modifying the `token` variable.
```

### Result of the query
1. **查無案件**:回傳**正常供水**  
  
2. 查詢結果為**降壓**，回傳
    1. 查詢時間
    2. 查詢結果為降壓
    3. 降壓地區
    4. 開始與結束時間

3. 查詢結果為**停水**，回傳
    1. 查詢時間
    2. 查詢結果為停水
    3. 停水地區
    4. 開始與結束時間

### Msg of Query result
![Error occur about the picture.](https://github.com/youron1115/Code-repo/blob/main/%E8%87%AA%E4%BE%86%E6%B0%B4%E4%BE%9B%E6%87%89%E9%80%9A%E7%9F%A5/Line%20notification.png?raw=true "Picture about the notification of LINE")