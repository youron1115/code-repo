# 使用官方 Python 執行環境作為基礎映像
FROM python:3.9.9-slim

RUN mkdir /app

# 設定工作目錄為 /app
WORKDIR /app

# 將當前目錄的內容複製到容器的 /app 內
ADD . /app

# 安裝 wget 和依賴套件
RUN apt-get update && apt-get install -y \
    wget \
    gnupg2 \
    unzip \
    curl

# 安裝 Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# install Chromium
RUN apt-get update

# install chromedriver
RUN apt-get install -yqq unzip
RUN wget -O /tmp/chromedriver.zip http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip
RUN unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/

# 安裝在 requirements.txt 中列出的必要套件
RUN pip install -r requirements.txt

# 當容器啟動時運行 flask_python.py
CMD ["python", "/app/wateroff_Query.py"]