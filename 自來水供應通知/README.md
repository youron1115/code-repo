# WaterOff Query web crawler and notification

WaterOff Query is a web crawler and notification system that checks the status of water supply in the city of location . It is a simple Python script that uses the `selenium` and `requests` libraries to scrape the [TAIWAN WATER COPORATION](https://wateroffmap.water.gov.tw/wateroffmap/map/search) website and send a notification to the user's line when wateroff_Query.py is being executed.

# Token of Line Notify
token='op5pgVh67ROewXEYzgB7vyaz39k4cchVeR3G1WjD1z5'

# Query Location: National Yunlin University of Science and Technology
Change the location of the query by modifying the `address` variable in the `wateroff_Query.py` file.
```
address="雲林縣斗六市大學路三段123號"
```