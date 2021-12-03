# 서울의 모레 날씨는 Showers로 예상됩니다.

import requests
url = 'https://www.metaweather.com/api/location/1132599/'
date = 'https://www.metaweather.com/api/location/1132599/2021/7/18/'
city = requests.get(url).json()
datee = requests.get(date).json()


print("{0}의 {1} 날씨는 {2}로 예상됩니다.".format(city['title'],datee[0]['applicable_date'],datee[0]['weather_state_name']))



