## `UnboundLocalError` 에러 해결

* 프로그래머스에서 문제를 풀게 되면, `def solution()` 안에 추가적으로 필요한 함수들을 만들어 푸는 경우가 많은데, 오늘은 처음으로 `UnboundLocalError`를 겪었다.
* 코드의 형태는 아래와 같았다.

```python
def solution(picks, minerals):

    def perm(curr=0):
        if r == curr:
            tmp = 0
            for i, mineral in enumerate(minerals):
                if i // 5 + 1 > len(test) or tmp >= answer:
                    break
                tmp += tiredness[mineral][test[i // 5]]
            if tmp < answer:
                answer = tmp
            return
        
    answer = float("inf")
    r, test, cnt = 무언가
    perm()

    return answer
```

> 중첩 함수 형태였으며, `solution()`에서 할당된 `r` `test` `cnt` `answer` 변수를 `perm()`에서 사용하고 있었다. 그리고 `answer`에서 할당되기 전 선언이 되었다는 `UnboundLocalError`를 내뱉었다.



* 여기서 의아했던 것은, `r` `test` `cnt` `answer` 모두 다 `perm()`밖에서 선언/할당된 변수들임에도 `answer`만 에러를 낸다는 점이었다.
  (pycharm 상에서도 `answer`에만 빨간 줄이 가득했다ㅠ)
* 보통 함수에서 그 밖의 scope에 있는 변수를 참조하려면 `global` 키워드를 사용했기에 도입하려 했으나 이미 함수 내에서 선언된 `answer`였기에 이 키워드를 사용하는 것도 불가능했다.
* 그래서 `global`키워드 사용이 가능한 형태로 코드를 변경했다.



## 해결방안 1: `global`

### 수정된 코드

```python
answer = float("inf")
def solution(picks, minerals):
	global answer
    
    def perm(curr=0):
        global answer
        if r == curr:
            tmp = 0
            for i, mineral in enumerate(minerals):
                if i // 5 + 1 > len(test) or tmp >= answer:
                    break
                tmp += tiredness[mineral][test[i // 5]]
            if tmp < answer:
                answer = tmp
            return
        
    r, test, cnt = 무언가
    perm()

    return answer
```

* 이렇게 하니 해결이 되었으나, 이 형태가 그다지 맘에 드는 형태는 아니었다. 그리고 분명 LEGB rule에 의해서 Local 범위를 넘으면 Encapsulated 범위에서 찾을 것일텐데도 에러가 난다는 것이 이해가 되지 않았다.
* 그래서 LEGB rule을 학습했던 자료를 다시 찾아보았고, 문제의 원인과 다양한 해결방안을 찾게 되었다.



## 해결방안 2: `nonlocal`

### 문제 원인

* **파이썬에서 변수를 할당할 때에는 로컬 스코프에서만 적용이 된다!**
* 즉, `answer = tmp`라고 변수에 새 값을 할당해버리면, `solution()`에서 정의된 `answer`를 사용하는 것이 아닌, `perm()`함수 스코프 내에서 새로운 `answer`로 만들어지는 것이다.
  * 코드를 다시 파악해보면, pycharm에서 `answer`에 빨간줄을 띄워주는 것은 `tmp >= answer`부터 존재하지만, 사실 이 부분이 문제여서 띄우는 에러는 아니다.
  * 문제의 부분은 `answer = tmp`로, 이 부분만 주석처리하면 에러가 말끔히 사라지는 것을 볼 수 있었다. 반대로 다른 `r` `test` `cnt`같은 변수들도 재할당을 하려고 하니 빨간줄과 함께 에러가 발생했다. 
* 이 에러를 해결하기 위해서는 해당 변수가 상위 함수에서 선언된 변수였음을 알려주는 키워드가 필요한데, 그것이 바로 `nonlocal`이다.



### `nonlocal`

* **상위 함수에 있는 변수를 참조한다고 미리 선언하기 위한 키워드**

* `global`은 그냥 함수 내에서 전역 변수를 사용할 때!
* `nonlocal`은 중첩 함수 내에서 상위 함수의 변수를 사용할때!



### 수정된 코드

```python
def solution(picks, minerals):
    answer = float("inf")
    
    def perm(curr=0):
        nonlocal answer
        if r == curr:
            tmp = 0
            for i, mineral in enumerate(minerals):
                if i // 5 + 1 > len(test) or tmp >= answer:
                    break
                tmp += tiredness[mineral][test[i // 5]]
            if tmp < answer:
                answer = tmp
            return
        
    r, test, cnt = 무언가
    perm()

    return answer
```



> 정리된 형태로는 굉장히 빠르게 착착 해결된 것처럼 보이지만, 사실 문제의 해결 방법만 먼저 알게되고 그 원인을 파악하는 데까지는 굉장히 오랜 시간이 소요되었다. 옆에서 ChatGPT에게 열심히 질문해가며 해결방안을 구해보았는데, GPT는 `nonlocal`을 쓰는 방법을 끝까지 알려주지 못했다..(못 미더운 자식)
>
> 그러나 완전히 새로운 형태의 해결방안을 알려주었다.



## 해결방안 3: 배열 이용하기

### 코드

```python
def solution(picks, minerals):
    answer = [float("inf")]
    
    def perm(curr=0):
        
        if r == curr:
            tmp = 0
            for i, mineral in enumerate(minerals):
                if i // 5 + 1 > len(test) or tmp >= answer[0]:
                    break
                tmp += tiredness[mineral][test[i // 5]]
            if tmp < answer[0]:
                answer[0] = tmp
            return
        
    r, test, cnt = 무언가
    perm()

    return answer
```

* 이 형태처럼 `answer`를 배열로 변경해 접근하게 되면, 에러가 나지 않을 것이라고 추천해주었다. 실제로 돌려보니 진짜 에러가 안났다. 너무 신기해서 그 이유를 물어보니 아래와 같은 답변을 들려주었다.



```markdown
파이썬에서 전역 변수와 배열 안의 값을 수정하는 것 사이의 차이점은 가변성(mutability) 때문입니다.

전역 변수를 직접 수정하려고 할 때, 함수 내에서 해당 변수를 참조하면 로컬 스코프에서 변수를 찾게 되고, 해당 변수가 로컬 스코프에 없으면 전역 스코프를 참조합니다. 그런데 함수 내에서 전역 변수에 값을 재할당하려고 하면, 로컬 스코프에 동일한 이름의 새로운 변수가 생성되어 전역 변수와 충돌이 발생합니다. 이러한 문제를 해결하기 위해 global 키워드를 사용하여 전역 변수임을 명시해야 합니다.

반면에 배열과 같은 가변 객체(mutable object)의 경우, 함수 내에서 배열의 값을 수정할 때 원본 객체를 직접 변경합니다. 따라서 함수 내에서 배열 원소를 변경할 때 전역 변수와 충돌이 발생하지 않으며, global 키워드를 사용할 필요가 없습니다. 이를 통해 함수 내에서 전역 변수를 안전하게 사용하고 수정할 수 있습니다.

요약하자면, 전역 변수를 직접 수정할 때는 스코프 충돌 문제로 인해 global 키워드를 사용해야 하지만, 배열과 같은 가변 객체의 값을 수정할 때는 원본 객체를 변경하므로 스코프 충돌 문제가 발생하지 않습니다.
```

* 정리해보면, 배열 안의 값을 변경할 때에는 새로운 로컬 스코프에 새 변수를 생성하는 것이 아닌 원본 객체를 직접 변경하기 때문이라는 것이다.
  * 심지어는 `answer = [9888]` 이런식의 재할당도 에러를 내지 않는다! 