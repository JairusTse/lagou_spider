import requests

# url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'
url = 'https://www.lagou.com/jobs/positionAjax.json?px=default&city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false'

payload = {
    'first': 'true',
    'pn': '66',
    'kd': 'Java',
}


headers = {
    'cookie': 'user_trace_token=20200502161006-5f64092b-68ad-49bb-85a1-952defce0136; LGUID=20200502161006-24b8a27b-853e-42e1-9809-59c326101987; _ga=GA1.2.1074256822.1588407007; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1587110728; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171d47186695ae-07036821372d5c-153f6554-1440000-171d471866ab1b%22%2C%22%24device_id%22%3A%22171d47186695ae-07036821372d5c-153f6554-1440000-171d471866ab1b%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; X_MIDDLE_TOKEN=02fc7f6174fa05f29534d0042e6e367e; _gid=GA1.2.1621370232.1589458129; privacyPolicyPopup=false; login=false; unick=""; _putrc=""; index_location_city=%E5%B9%BF%E5%B7%9E; LGSID=20200516230520-1f928ce2-1da8-415e-b38d-ae92738264c8; _gat=1; X_HTTP_TOKEN=1a6f741dbfa808232083469851197b66cad4d9d31a; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1589643804; LGRID=20200516234323-b6a20210-6565-41d6-98ad-406dcf9893f5',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'referer': 'https://www.lagou.com/jobs/list_java/p-city_213?px=default',
}
response = requests.post(url, data=payload, headers=headers)

print(response.text)