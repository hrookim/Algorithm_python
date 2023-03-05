import sys
# input = sys.stdin.readline
sys.stdin = open('input.txt')

N, M = map(int, input().split())
dict_pokemons = {str(n): sys.stdin.readline().rstrip() for n in range(1, N+1)}
questions = [sys.stdin.readline().rstrip() for _ in range(M)]

new_dict = {}
for k, v in dict_pokemons.items():
    new_dict[v] = k

for q in questions:
    if dict_pokemons.get(q):
        print(dict_pokemons.get(q))
    else:
        print(new_dict[q])