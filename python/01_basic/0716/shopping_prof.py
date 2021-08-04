import requests
from pprint import pprint


query ='키크론 k2'
url ="https://openapi.naver.com/v1/search/shop.json?query={}&sort=asc".format(query)

head = {
    "X-Naver-Client-Id": "TSRtYho34lHEiVMb5IVG",
    "X-Naver-Client-Secret": "Cx5XAs8mOl"
}

response = requests.get(url, headers=head).json()
# pprint(response)

items = response['items']
min_value = 99999999999
title= ""
min_url = ""
for item in items:
    print(item['lprice'])

for item in items:
    if min_value > int(item['lprice']):
        min_value = int(item['lprice'])
        title = item['title']
        min_url = item['link']
shop =("{} \n 최저가 : {} \n 링크:{}".format(title,min_value,min_url))


urll = 'https://api.telegram.org/bot1806170351:AAGayUFdPdQJtzzWOv9OR1Z6JbehEvgfJjc/sendMessage?chat_id=1819081060&text={}'.format(shop)
response = requests.get(urll).json()
print(response[''])
