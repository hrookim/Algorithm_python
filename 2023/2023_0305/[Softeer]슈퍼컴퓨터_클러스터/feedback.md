### 문제풀이 결과

1. 실패 (while - for: 시간초과, 최대 5090ms)
2. 실패 (while - for: 시간초과)
3. 실패 (while - for: 시간초과)
4. 성공 (이진탐색, 최대 300ms)



### 실패 원인

* 처음 작성한 code로는 최저 성능 컴퓨터의 최댓값을 `현재 갖고 있는 최저 성능 + 1`부터 시작해서 `price <= B`인 최대치까지 찾는 것이었음. 

* 그러나, 이렇게 진행하게 되면 `O(n**2)`이 실행되게 되고, 시간초과가 나게 된다.

* 이를 해결하기 위해 이진탐색을 사용했다.

  > 오랜만에 이진탐색을 시도하느라.. 등호의 여부와 중단 여부 판별이 힘들었다ㅠㅜㅠㅜ

* 생각보다 코드는 간단했다.

```python
# 이진탐색 코드
result = 0  # 최저 성능 컴퓨터의 최댓값이 될 결과
left, right = sorted(performances)[0]+1,  10**10
while left <= right:
    price = 0
    mid = (left + right) // 2
    
    for k in perfo_dict.keys():
        if k < mid:
            price += perfo_dict[k] * (mid - k)**2
    
    # 이진탐색의 종료조건, 이 안에서 걸러지지 않는다면 left > right가 됨으로써 종료된다.
    if price == B:
        result = mid
        break
    if price < B:
        result = mid
        left = mid + 1
    else:
        right = mid - 1
```





### 오늘의 교훈

**특정 값을 찾을 때 `O(n**2)`일 것 같은 느낌이 온다면, 빠르게 이진탐색을 사용해보자**