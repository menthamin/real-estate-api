"""국토교통부_공동주택 단지 목록제공 서비스
- 링크: https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15057332
"""
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import io
import xmltodict
import json

# import xml.etree.ElementTree as et
# https://apis.data.go.kr/1613000/AptListService2/getTotalAptList?serviceKey=kZTVxFnH9M4WwBalaryfozQTc3bNUiVQHXpP0kUC1X0Ye1RV9%2FYo53xoR9z3efEQR7vD5shcSMYoXYei8UezhQ%3D%3D&pageNo=1&numOfRows=10

# load .env
load_dotenv()
pubkey_de = os.environ.get("pubkey_de")

url = "http://apis.data.go.kr/1613000/AptListService2/getTotalAptList"
params = {
    "serviceKey": pubkey_de,
    "pageNo": 1,  # 페이지 수
    "numOfRows": 100000,  # 목록 건수 (한국 APT 단지 수 약 1.9만개)
}

response = requests.get(url, params=params)

dict_content = xmltodict.parse(response.content)["response"]["body"]["items"]["item"]
df = pd.DataFrame(dict_content)


df.to_csv("data/국토교통부_아파트단지목록_20220913.csv", encoding="utf8", index=False)
