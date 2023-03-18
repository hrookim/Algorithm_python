original_set = [1, 2, 3, 4]

bit = [0 for _ in range(len(original_set))]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                # print(bit)



def backtrack(a, k, input):
    global MAXCANDIDATES
    C = [0] * MAXCANDIDATES
    
    if k == input:
        # process_solution(a, k)
        print("찾았다")
    else:
        k += 1
        ncandidates = construct_candidates(a, k, input, C)
        for i in range(ncandidates):
            a[k] = C[i]
            backtrack(a, k, input)
    

def construct_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2


MAXCANDIDATES = 2
NMAX = 4
a = [0] * NMAX
backtrack(a, 0, 3)