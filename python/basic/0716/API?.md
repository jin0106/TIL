

### 1. JSON(JavaScript Object Notation)

* `데이터만을` 주고 받기 위한 표기법
* 파이썬의 `Dictionary`와 `list `구조로 쉽게 변환하여 활용 가능



<img src="0716 startcamp.assets/image-20210716100146494.png" alt="image-20210716100146494" style="zoom:50%;" />



![image-20210716100443092](0716 startcamp.assets/image-20210716100443092.png)

dictionary 처럼 보이지만 사실 JSON이다.



![image-20210716100929874](0716 startcamp.assets/image-20210716100929874.png)

문자열인 JSON을 dictionary와 list 형태로 바꿔줌.



# API란?



![image-20210716102728265](0716 startcamp.assets/image-20210716102728265.png)

* 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스. 
* 어떠한 운영체제를 사용하도 동일한 결과값을 받아 볼수 있음.

### API 활용

1. 정보가 있는 API url 확인

   ```
   url = 'https://asdf'
   ```

2. url로 요청

   ```
   response = requests.get(url).json()
   ```

3. 응답 결과를 확인 정보 출력

   ```
   print(response)
   ```

   

#### API 사용의 핵심

* 서버에서 확인 할 수 있게끔 요청을 보내야함.

##  Web Crawling

* `Web Crawling` 이란?

  * 웹을 조직적, 자동화 된 방법으로 탐색하는것
  * 검색 엔진과 같은 여러 사이트에서는 데이터 최신 상태 유지를 위해 웹 크롤링 실시

* 정보 스크랩

  * 정보가 있는 사이트 url 확인

    ```python
    # 원하는 주소로 요청, 응답 저장
    import requests
    response = requests.get(url).text
    # 정보 출력 및 확인
    print(response)
    ```

  * `url`로 요청

    ```python
    import reuests
    from bs4 import BeautifulSoup
    response = requests.get("https://finance.naver.com/marketindex/").text
    html= BeautifulSoup(response,'html.parser')
    # 출력
    print(html.select_one("#exchangeList > li:nth-child(3) > a.head.eur > div > span.value").text
    ```

* requests 모듈

  * 파이썬에서 서버에 요청할 때 사용하는 모듈 (기본제공 모듈)

  * 설치 방법

    ```
    $ pip install requests
    ```

  * 사용방법

    ```python
    # requests.get('URL')
    # 'URL'에 requests 해서, 정보를 get
    
    import requests
    
    requests.get('URL')
    requests.get('URL').text				# text 문서 형식으로 수신
    requests.get('URL').status_code # 상태 코드만 추출
    requests.get('URL').json()			# json 형식으로 수신
    ```

* beautifulsoup4

  * 문서를 검색하기 쉽게 만드는 모듈

  * 설치방법

    ```
    $ pip3 install beautifulsoup4
    from bs4 import BeautifulSoup # 모듈 호출
    ```

  * 사용 방법

    ```python
    BeautifulSoup(문서)
    BeautifulSoup.select(경로)			# 문서 안에 있는 특정 내용 추출
    BeautifulSoup.select_one(경로)	# 문서 안에 있는 특정 하나만 추출
    
    # ex)
    data = BeautifulSoup(response)
    ```

    

