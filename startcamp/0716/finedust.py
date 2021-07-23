import requests
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=%EC%84%9C%EC%9A%B8&pageNo=1&numOfRows=100&pm10Value=1&returnType=json&serviceKey=stjlQoKqTsm4IBAGvPGwIa3rfwiC7FFtM9CkqUx7xxZInmSVJV09I8Fc9yPgArEEgkfnT%2BeSDxUg6uE6hp%2F7aA%3D%3D&ver=1.0'
response = requests.get(url).json()
city = (response['response']['body']['items'][0]['sidoName'])
city_1 = (response['response']['body']['items'][27]['stationName'])
density = (response['response']['body']['items'][0]['pm10Value'])



response1 = "{}의 {}의 미세먼지 농도는 {}입니다".format(city, city_1,density)


urll = 'https://api.telegram.org/bot1806170351:AAGayUFdPdQJtzzWOv9OR1Z6JbehEvgfJjc/sendMessage?chat_id=1819081060&text={}'.format(response1)
response12 = requests.get(urll).json()
print(response12)