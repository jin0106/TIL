# rDatabase	

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

  ```sql
  $ sqlite3 db.sqlite3
  sqlite> .tables
  sqlite> .schema articles_article
  sqlite> SELECT * FROM articles_article;
  ```

  * `.` 은 sqlite 프로그램의 기능을 실행하는 것

  * `;` 까지 하나의 명령 (SQL Query)로 간주 됨

    

|                        분류                         |                             개념                             |             예시             |
| :-------------------------------------------------: | :----------------------------------------------------------: | :--------------------------: |
|  DDL - 데이터 정의 언어 (Data Definition Language)  | 데이터 정의 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 |      CREATE DROP ALTER       |
| DML - 데이터 조작 언어 (Data Manlpulation Language) |               데이터 저장, 수정, 삭제, 조회 등               | INSERT UPDATE DELETE SELECT  |
|   DCL - 데이터 제어 언어 (Data Control Language)    |              데이터베이스 사용자의 권한 제어 등              | GRANT REVOKE COMMIT ROLLBACK |



### 기본 구조

