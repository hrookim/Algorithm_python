import sys
sys.stdin = open('input.txt')

def get_students(idx, num):
    global students
    if num == 0:
        students = students
    else:
        tmp = students.pop(idx)
        students.insert(idx-num, tmp)


N = int(input())
students = [i for i in range(1, N+1)]
numbers = list(map(int, input().split()))
for idx, num in enumerate(numbers):
    get_students(idx, num)
print(' '.join(map(str, students)))
