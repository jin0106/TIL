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
lst =[]
for i in range(1,len(response)+1):  
    pprint(response['items'][i]['lprice'])
    lst.append(response['items'][i]['lprice'])
    if response['items'][i]['lprice'] == '19800':
        print(response['items'][i]['link']+response['items'][i]['mallName'])
        break


urll = 'https://api.telegram.org/bot1806170351:AAGayUFdPdQJtzzWOv9OR1Z6JbehEvgfJjc/sendMessage?chat_id=1819081060&text={}'.format(asdf)
response1 = requests.get(urll).json()
print(response1)
# print(min(lst))
    
# # pprint(response)

# 1. 반복문을 사용하여 각 제품마다 lprice를 출력해주세요
# # 2. 최저가를 찾아서 최저가를 출력해주세요.
# 3. 최저가명, 최저가, 최저가 쇼핑몰 링크
# 4. 텔레그램으로 출력