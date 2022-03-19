import sys
sys.stdin = open('input.txt')

seq1 = [0] + list(input())
seq2 = [0] + list(input())

len1, len2 = len(seq1), len(seq2)


matrix = [[0]*len1 for _ in range(len2)]

for j in range(1, len1):
    for i in range(1, len2):
        if seq1[j] != seq2[i]:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])
        else:
            matrix[i][j] = matrix[i-1][j-1] + 1

print(matrix[len2-1][len1-1])
