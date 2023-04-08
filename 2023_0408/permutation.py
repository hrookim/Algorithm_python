from pprint import pprint

def perm(start, r):
    if start == r:
        permutation.append(array[:r])
    else:
        for change in range(start, N):
            array[start], array[change] = array[change], array[start]
            perm(start+1, r)
            array[start], array[change] = array[change], array[start]

            

array = ["A", "B", "C", "D", "E"]
N = len(array)
r = 3
permutation = []
perm(0, r)
pprint(permutation)