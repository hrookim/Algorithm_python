"""
코딩테스트 참여 개발언어 항목에 cpp, java, python 중 하나를 선택해야 합니다.
지원 직군 항목에 backend와 frontend 중 하나를 선택해야 합니다.
지원 경력구분 항목에 junior와 senior 중 하나를 선택해야 합니다.
선호하는 소울푸드로 chicken과 pizza 중 하나를 선택해야 합니다.

# 궁금해하는 내용?
 [조건]을 만족하는 사람 중 코딩테스트 점수를 X점 이상 받은 사람은 모두 몇 명인가?
 '-' 표시는 해당 조건을 고려하지 않겠다는 의미입니다.
 "[조건] X"
"""


def solution(info, query):
    length = len(query)
    answer = [0] * length
    
    # 1. 쿼리 정리하기
    for n in range(length):
        qualifications = query[n].split()
    
        for _info in info:
            person_info = _info.split()
            
            tmp = fail = 0
            for i in range(5):
                if fail:
                    break
                if i < 4:
                    if qualifications[2*i] == '-':
                        tmp += 1
                    elif person_info[i] == qualifications[2*i]:
                        tmp += 1
                    else:
                        fail += 1
                elif i == 4 and int(person_info[i]) >= int(qualifications[7]):
                    tmp += 1
        
            if tmp == 5:
                answer[n] += 1
    
    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info, query))

"""

"""