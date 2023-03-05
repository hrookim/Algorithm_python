# 행렬이용?
import sys
sys.stdin = open('input.txt')


def multiply(matrix1, matrix2):
    temp = [[0, 0], [0, 0]]
    temp[0][0] = ((matrix1[0][0] * matrix2[0][0]) + (matrix1[0][1] * matrix2[1][0])) % 1000000007
    temp[0][1] = ((matrix1[0][0] * matrix2[0][1]) + (matrix1[0][1] * matrix2[1][1])) % 1000000007
    temp[1][0] = ((matrix1[1][0] * matrix2[0][0]) + (matrix1[1][1] * matrix2[1][0])) % 1000000007
    temp[1][1] = ((matrix1[1][1] * matrix2[1][1]) + (matrix1[1][0] * matrix2[0][1])) % 1000000007
    return temp


def how_many(matrix, N):
    if N == 1:
        return matrix
    else:
        result = how_many(matrix, N//2)
        if N % 2 == 0:
            return multiply(result, result)
        else:
            return multiply(multiply(result, result), matrix)
        
        
N = int(input())
matrix = [[1, 1], [1, 0]]
a = how_many(matrix, N)[0][1] % 1000000007

print(a)

        
