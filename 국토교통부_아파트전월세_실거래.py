"""국토교통부 아파트전월세 실거래 데이터 추출 예시
- 링크: https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15058017
"""
from dotenv import load_dotenv
import os
import requests
import pandas as pd
import io
import xmltodict
import json

# import xml.etree.ElementTree as et


# load .env
load_dotenv()
getRTMSDataSvcAptRent_en = os.environ.get("getRTMSDataSvcAptRent_en")
getRTMSDataSvcAptRent_de = os.environ.get("getRTMSDataSvcAptRent_de")

url = "http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptRent"
params = {
    "serviceKey": getRTMSDataSvcAptRent_de,
    "LAWD_CD": "11680",  # Input 1: 시군구코드 5자리, ex) 11680 = 서울특별시 강남구
    "DEAL_YMD": "202207",  # Input 2: 년월(YYYYMM), ex) 202208 = 2022년 8월
}

response = requests.get(url, params=params)
dict_content = xmltodict.parse(response.content)["response"]["body"]["items"]["item"]
df = pd.DataFrame(dict_content)


df.to_csv("data/서울특별시_강남구_아파트전월세_202207.csv", encoding="utf8", index=False)
