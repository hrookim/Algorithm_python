import sys
sys.stdin = open("input2.txt")


def binary_search(start, end):
    while start <= end:
        mid = (start + end) // 2
        
        tmp_list = [0]*N
        tmp_list[0] = C_list[0]
        for i in range(N-1):
            if tmp_list[i] >= mid:
                tmp_list[i+1] = C_list[i+1] + D_list[i]
            elif tmp_list[i] + D_list[i] >= mid:
                tmp_list[i+1] = C_list[i+1] + (tmp_list[i]+D_list[i]-mid)
            else:
                # 이거는 아예 mid가 너무 큰값이라는 의미
                break
            
        if tmp_list[N-1] >= mid:
            start = mid + 1
        else:
            end = mid - 1

    else:
        return (start+end)//2


N, T = map(int, input().split())


for _ in range(T):
    tmp = list(map(int, input().split()))
    
    C_list = [tmp[2*i] for i in range(N)]
    D_list = [tmp[2*i+1] for i in range(N-1)]
    
    end = max(C_list) + max(D_list)
    start = min(C_list)
    
    answer = binary_search(start, end)
    print(answer)
    