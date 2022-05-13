import sys 
sys.stdin = open('input3.txt') 
input = sys.stdin.readline

input()
az = list(map(int, input().split()))
bz = list(map(int, input().split()))
totalz = sorted(az + bz)
print(*totalz)