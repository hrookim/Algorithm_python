def solution(s):
    answer = []
    stack = []
    for i in range(len(s)):
        if s[i] == "{" or s[i] == "}":
            stack.append(s[i])
        elif s[i] == ",":
            pass
        else:
            if s[i-1] not in ("{", "}", ","):
                stack[-1] += s[i]
            else:
                stack.append(s[i])
    stack = stack[1:-1]
    
    tuples = []
    op = cls = 0
    for j in range(len(stack)):
        if stack[j] == "{":
            op = j
        elif stack[j] == "}":
            cls = j
            tuples.append(stack[op+1:cls])
    
    for k in range(1, len(tuples)+1):
        for tup in tuples:
            if k == len(tup):
                for t in tup:
                    if int(t) not in answer:
                        answer.append(int(t))
    print(answer)
    return answer



s = "{{20,111},{111}}"
solution(s)