import sys
sys.stdin = open('input.txt')


def which_type():
    s_points1 = [(x1, y1), (x1, q1), (p1, y1), (p1, q1)]
    s_points2 = [(x2, y2), (x2, q2), (p2, y2), (p2, q2)]

    return [x1, y1, p1, q1] & [x2, y2, p2, q2]
    
    

T = 4

for tc in range(T):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    
    print(which_type())
   