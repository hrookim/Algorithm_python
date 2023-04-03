import sys 
sys.stdin = open('input3.txt') 

def is_number(char):
    return True if 48 <= ord(char) <= 57 else False

N = int(input())


numbers = []
for _ in range(N):
    words = input().strip()
    i = 0
    len_words = len(words)
    while i < len_words:
        if is_number(words[i]):
            j = i + 1
            while j < len_words and is_number(words[j]):
                j += 1
            else:
                numbers.append(int(words[i:j]))
                i = j
        else:
            i += 1
                
numbers.sort()
for number in numbers:
    print(number)
