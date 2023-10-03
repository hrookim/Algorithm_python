# SELECT 연습

## 1. 조건에 맞는 회원수 구하기

* `USER_INFO` 테이블

| Column name | Type       | Nullable |
| ----------- | ---------- | -------- |
| USER_ID     | INTEGER    | FALSE    |
| GENDER      | TINYINT(1) | TRUE     |
| AGE         | INTEGER    | TRUE     |
| JOINED      | DATE       | FALSE    |



### 문제

2021년에 가입한 회원 중 나이가 20세 이상 29세 이하인 회원이 몇명인지 출력하기



### 답안

```sql
SELECT count(*) AS USERS FROM USER_INFO
WHERE YEAR(JOINED) = 2021 
AND AGE BETWEEN 20 AND 29;
```

```sql
SELECT count(*) AS USERS FROM USER_INFO
WHERE YEAR(JOINED) = 2021 
AND 20 <= AGE
AND AGE <= 29;
```

---



## 2. 상위 n개 레코드

* `ANIMAL_INS` 테이블

| NAME             | TYPE       | NULLABLE |
| ---------------- | ---------- | -------- |
| ANIMAL_ID        | VARCHAR(N) | FALSE    |
| ANIMAL_TYPE      | VARCHAR(N) | FALSE    |
| DATETIME         | DATETIME   | FALSE    |
| INTAKE_CONDITION | VARCHAR(N) | FALSE    |
| NAME             | VARCHAR(N) | TRUE     |
| SEX_UPON_INTAKE  | VARCHAR(N) | FALSE    |



### 문제

동물 보호소에 가장 먼저 들어온 동물의 이름을 조회하는 SQL 문을 작성해주세요.



### 답안

```sql
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME LIMIT 1;
```

**`LIMIT`는 `ORDER BY` 뒤에 적혀야 한다!**



## 3. 오프라인/온라인 판매 데이터 통합하기 - `UNION`

### `UNION`: 중복되는 행은 하나로 표시

### `UNION ALL`: 중복제거를 하지 않고 모두 표시

* 두개의 SELECT 결과를 합칠 수 있음
* 컬럼의 개수가 같아야 하고, 각 컬럼의 데이터 타입이 같아야 한다

```sql
-- 사용법
SELECT * FROM TABLE_A
UNION (ALL)
SELECT * FROM TABLE_B
```



### 문제

`ONLINE_SALE` 테이블과 `OFFLINE_SALE` 테이블에서 2022년 3월의 오프라인/온라인 상품 판매 데이터의 판매 날짜, 상품ID, 유저ID, 판매량을 출력

`OFFLINE_SALE` 테이블의 판매 데이터의 `USER_ID` 값은 NULL 로 표시

결과는 판매일 -> 상품 ID -> 유저 ID를 기준으로 오름차순 정렬



### 답안

```sql
(SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT FROM ONLINE_SALE
WHERE MONTH(SALES_DATE) = 3 AND YEAR(SALES_DATE) = 2022)
UNION
(SELECT DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE, PRODUCT_ID, NULL AS USER_ID, SALES_AMOUNT FROM OFFLINE_SALE
WHERE MONTH(SALES_DATE) = 3 AND YEAR(SALES_DATE) = 2022)
ORDER BY SALES_DATE, PRODUCT_ID, USER_ID;
```



## 4. 재구매가 일어난 상품과 회원 리스트 구하기

### 문제

`ONLINE_SALE` 테이블에서 동일한 회원이 동일한 상품을 재구매한 데이터를 구하여, 재구매한 회원 ID와 재구매한 상품 ID를 출력

결과는 회원 ID를 기준으로 오름차순 정렬, 회원 ID가 같다면 상품 ID를 기준으로 내림차순 정렬



### 답안

* 내가 작성한 답안

```sql
SELECT USER_ID, PRODUCT_ID 
FROM
(
SELECT USER_ID, PRODUCT_ID, COUNT(PRODUCT_ID) AS PROD_CNT
    FROM ONLINE_SALE
    GROUP BY USER_ID, PRODUCT_ID
) A
WHERE PROD_CNT >= 2
ORDER BY USER_ID, PRODUCT_ID DESC;
```



* 블로그에 있는 답안 (`GROUP BY`와 `HAVING` 사용)

```sql
SELECT
    USER_ID,
    PRODUCT_ID
FROM    
    ONLINE_SALE
GROUP BY
    USER_ID,
    PRODUCT_ID
HAVING
    COUNT(*) >= 2
ORDER BY
    USER_ID ASC,
    PRODUCT_ID DESC
```



### 만났던 오류

**Every derived table must have its own alias**

> 서브 쿼리 사용시 alias를 주지 않아서 생기는 에러, MySQL은 필수적으로 서브쿼리 뒤에 alias를 붙여줘야 한다. 위의 경우 `A`가 alias이다!



## 5. 서울에 위치한 식당 목록 구하기

### 문제

`REST_INFO`와 `REST_REVIEW` 테이블이 따로 존재. 

서울에 위치한 식당들의 식당 ID, 식당 이름, 음식 종류, 즐겨찾기수, 주소, 리뷰 평균 점수를 조회하는 SQL문을 작성

이때 리뷰 평균점수는 소수점 세 번째 자리에서 반올림

결과는 평균점수를 기준으로 내림차순, 평균점수가 같다면 즐겨찾기수를 기준으로 내림차순



### 답안

```sql
SELECT I.REST_ID, I.REST_NAME, I.FOOD_TYPE, I.FAVORITES, I.ADDRESS,
ROUND(AVG(REVIEW_SCORE), 2) AS SCORE
FROM REST_INFO I, REST_REVIEW R
WHERE I.REST_ID = R.REST_ID AND ADDRESS LIKE "서울%"
GROUP BY REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;
```

> 이 코드는 JOIN문 없이 JOIN한 결과를 내고 있다. JOIN을 사용한 결과는 아래와 같다 (블로그)

```sql
SELECT B.REST_ID,	REST_NAME,	FOOD_TYPE,	FAVORITES,	ADDRESS,
ROUND(AVG(REVIEW_SCORE),2) AS SCORE
FROM REST_INFO A
JOIN REST_REVIEW B ON A.REST_ID=B.REST_ID
WHERE ADDRESS LIKE '서울%'
GROUP BY REST_ID
ORDER BY SCORE DESC,FAVORITES DESC
```

