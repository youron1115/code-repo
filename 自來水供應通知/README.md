# WaterOff Query web crawler and notification

WaterOff Query is a web crawler and notification system that checks the status of water supply in the city of location . It is a simple Python script that uses the `selenium` and `requests` libraries to scrape the [TAIWAN WATER COPORATION](https://wateroffmap.water.gov.tw/wateroffmap/map/search) website and send a notification to the user's line when wateroff_Query.py is being executed.

# Token of Line Notify
token='op5pgVh67ROewXEYzgB7vyaz39k4cchVeR3G1WjD1z5'

# Query Location: National Yunlin University of Science and Technology
Change the location of the query by modifying the `address` variable in the `wateroff_Query.py` file.
```
address="雲林縣斗六市大學路三段123號"
```

# Result of the query
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