# Database	

```
데이터베이스는 체계화된 데이터의 모임.
여러 사람이 공유하고 사용할 목적으로 통합 관리되는 정보의 집합. 논리적으로 연관된 자료의 모음.
몇 개의 자료 파일을 조직적으로 통합하여 자료 항목의 중복을 없애고 자료를 구조화하여 기억 시켜놓은 자료의 집합체
```



### DB로 얻는 장점들

* 데이터 중복 최소화
* 데이터 무결성 (정확한 정보 보장)
* 데이터 일관성
* 데이터 독립성
* 데이터 표준화
* 데이터 보안 유지



## 관계형 데이터베이스 (RDB)

* key와 value들의 간단한 관계를 table 형태로 정리한 데이터베이스
* 관계형 모델에 기반



### 주요 용어 정리

* Schema : 데이터베이스에서 자료의 구조, 표현방법, 관계등 전반적인 명세를 기술한 것
* Table : 열(column/field)과 행(record/value)의 모델을 사용해 조직된 데이터 요소들의 집합

* Column : 각 열에는 고유한 데이터 형식이 저장됨
* Row : 실제 데이터가 저장되는 형태
* Primary Key : 각 행의 고유 값



## 관계형 데이터베이스 관리 시스템 (RDBMS)

관계형 모델을 기반으로하는 데이터베이스 관리시스템 (가장 많이 활용)



## SQL (Structured Query Language)

* 관계형 데이터베이스 관리시스템의 데이터 관리를 위해 설계된 특수 목적의 프로그래밍 언어

* RDBMS에서 자료의 검색과 관리, 데이터베이스 스키마 생성과 수정, 데이터베이스 접근 관리 등을 위해 고안됨

* 예시 

  ```
  $ sqlite3 db.sqlite3
  sqlite> .tables
  sqlite> .schema articles_article
  sqlite> SELECT * FROM articles_article;
  ```

  - `.` 은 sqlite 프로그램의 기능을 실행하는 것 (SQL lite)
  - `;` 까지 하나의 명령 (SQL Query)로 간주 됨



|                        분류                         |                             개념                             |             예시             |
| :-------------------------------------------------: | :----------------------------------------------------------: | :--------------------------: |
|  DDL - 데이터 정의 언어 (Data Definition Language)  | 데이터 정의 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 |      CREATE DROP ALTER       |
| DML - 데이터 조작 언어 (Data Manlpulation Language) |               데이터 저장, 수정, 삭제, 조회 등               | INSERT UPDATE DELETE SELECT  |
|   DCL - 데이터 제어 언어 (Data Control Language)    |              데이터베이스 사용자의 권한 제어 등              | GRANT REVOKE COMMIT ROLLBACK |



#### 기본 데이터 베이스 활용법

- SQLite 3 생성 접근 : `sqlite3 <filename>`
- 테이블 목록 조회 : `.tables`
- 특정 테이블 스키마 조회 : `.schema <table>`





### 테이블



##### 생성

```sql
CREATE TABLE (table_name) (
	(column) datatype [constraints],
  (column) datatype [constraints],
  ...
);
```

* constraints

  PRIMARY KEY, NOT NULL, UNIQUE, DEFAULT 등

* `users_user.sql` 파일을 생성하여 불러와도 된다.

  ```sqlite
  sqlite> .read users_user.sql
  ```

##### 

예시

```sql
CREATE TABLE classmate (
first_name TEXT NOT NULL,
las_name TEXT NOT NULL,
city TEXT NOT NULL
)
```



##### 이름 변경

` ALTER TABLE`, `RENAME TO` 사용

```sql
ALTER TABLE classmates RENAME TO users;
```



##### 삭제

```sql
DROP TABLE table_name;
```



#### SELECT

SELECT 문은 데이터를 읽어올 수 있으며 특정한 테이블을 반환한다.

```sqlite
SELECT * FROM examples;
```



### CRUD



#### CREATE

* 특정 테이블에 새로운 행을 추가하여 데이터를 추가

  `INSERT INTO`, `VALUES`

  ```sql
  INSERT INTO table_name (colum_name1, column_name2) VALUES (values1, values2);
  ```

  ```sql
  INSERT INTO classmates VALUES ('길동','홍','서울');
  ```

  * 모든 열에 데이터가 있는경우 column을 명시하지 않아도 됨!



#### READ

* 특정 테이블에서 데이터를 조회
* ORDER BY, DISTINCT, WHERE, LIMIT, GROUP BY 등과 함께 사용



* <strong>LIMIT</strong>

  * 쿼리에서 반환되는 행 수를 제한
  * 특정 행부터 시작해서 조회하기 위해 `OFFSET`키워드와 함께 사용하기도 함

  ```sql
  SELECT rowid, name FROM classmates LIMIT 2;
  SELECT rowid, name FROM classmates LIMIT 2 OFFSET 2;
  ```

  

* <strong>WHERE</strong>

  * 쿼리에서 반환된 행에 대한 특정 검색 조건을 지정

  ```sql
  SELECT name FROM classmates WHERE address='seoul';
  ```

  

* <strong>SELECT DISTINCT</strong>

  * 조회 결과에서 중복 행을 제거
  * DISTINCT 절은 SELECT 키워드 바로 뒤에 작성해야 함

  ```sql
  SELECT DISTINCT age FROM classmates;
  ```



#### DELETE

* 테이블에서 행을 제거

``` sql
DELETE FROM classmates WHERE rowid=5;
```



* `AUTOINCREMENT`

  * SQLite가 사용되지 않은 값이나 이전에 삭제된 행의 값을 재사용하는 것을 방지
  * 테이블을 생성하는 단계에서 `AUTOINCREMENT`를 통해 설정 가능

  ```sql
  CREATE TABLE table_name (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ...
  );
  ```

  

#### UPDATE

* 기본 행의 데이터를 수정
* `SET` 에서 테이블의 각 열에 대해 새로운 값을 설정

```sql
UPDATE table_name SET column1=value1, colum2=value2, ... WHERE condition;
```

중복 불가능한(UNIQUE) 값인 rowid를 기준으로 수정

```sqlite
UPDATE classmates SET name='홍길동', address='제주도' WHERE rowid=5;
```





### SQLITE functions

* `COUNT`

  * 그룹의 항목 수를 가져 옴

  ```sql
  SELECT COUNT(column_name) FROM table_name;
  SELECT COUNT(*) FROM users;
  ```

  

* `AVG`

  * 각 집합의 평균 값을 계산

  ```sql
  SELECT AVG(column_name) FROM table_name;
  SELECT AVG(age) FROM users WHERE age>=30;
  ```

  

* `MAX`

  * 그룹에 있는 모든 값 중 최대값을 가져옴
  
  ```sql
  SELECT MAX(column_name) FROM table_name;
  SELECT first_name, MAX(blance) FROM users;
  ```
  
  
  
* `MIN`
  * 그룹에 있는 모든 값 중 최소값을 가져옴

  ```sql
  SELECT MIN(column_name) FROM table_name;
  SELECT age, MIN(balance) FROM users;
  ```

  

* SUM
  * 모든 값의 합을 계산

  ```sql
  SELECT SUM(column_name) FROM table_name;
  SELECT SUM(age) FROM users;
  ```

  

#### LIKE

* 패턴 일치를 기반으로 데이터를 조회하는 방법

* sqlite는 패턴 구성을 위한 2개의 wildcards를 제공

  * `%` : 문자열이 있을 수도 있고 없을 수도 있다

  * `_` : 반드시 이자리에 '한 개'의 문자가 존재해야 한다

    |     예     |                     의미                     |
    | :--------: | :------------------------------------------: |
    |     2%     |               2로 시작하는 값                |
    |     %2     |                2로 끝나는 값                 |
    |    %2%     |               2가 들어가는 값                |
    |    _2%     | 아무값이나 들어가고 두번째가 2로 시작하는 값 |
    |    1___    |           1로 시작하고 4자리인 값            |
    | 2_%_%/2__% |        2로 시작하고 적어도 3자리인 값        |



### ORDER BY

* 조회 결과 집합을 정렬
* SELECT 문에 추가하여 사용
* 정렬 순서를 위한 2개의 keyword 제공
  * ASC - 오름차순 (default)
  * DESC - 내림차순

```sql
SELECT * FROM table_name ORDER BY column ASC;
SELECT * FROM table_name ORDER BY column1, colum2 DESC;
```

나이순으로 오름차순 정렬 하여 상위 10개만 조회

```sql
SELECT * FROM users ORDER BY ages ASC LIMIT 10;
```



#### GROUP BY

* 행 집합에서 요약 행 집합을 만듦
* SELECT문의 optional 절
* 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듦
* 문장에 WHERE 절이 포함된 경우 반드시 WHERE 절 뒤에 작성해야 함

```sql
SELECT last_name COUNT(*) FROM users GROUP BY last_name;
```

users에서 각 성씨가 몇 명씩 있는지 조회



#### ALTER TABLE

* table 이름 변경

* 테이블에 새로운 column 추가

  ```sql
  ALTER TABLE table_name ADD COLUMN column_name datatype;
  ```

  NOT NULL을 설정해서 추가하면 Error가 발생하는데 해결방법 2가지가 있다.

  1. NOT NULL 설정 없이 추가
  2. 기본 값 설정하기

  ```sql
  ALTER TABLE classmates ADD COLUMN subtitle TEXT NOT NULL DEFAULT '소제목';

* column 이름 수정

  
