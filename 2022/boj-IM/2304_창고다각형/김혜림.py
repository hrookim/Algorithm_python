import sys
sys.stdin = open('input.txt')


def make_structure(nemos):
    length = 0
    for nemo in nemos:
        if nemo[0] > length:
            length = nemo[0]

    structure = [0] * (length + 1)

    for nemo in nemos:
        structure[nemo[0]] = nemo[1]

    return structure


def get_max_h(structure):
    max_h = max_i = 0

    for i, h in enumerate(structure):
        if h > max_h:
            max_h = h
            max_i = i
    return max_h, max_i


def get_surface(structure):
    max_h, max_i = get_max_h(structure)
    tmp_h = 0
    surface = 0
    for i, h in enumerate(structure[:max_i + 1]):
        if h > tmp_h:
            surface += h
            tmp_h = h
        else:
            surface += tmp_h

    tmp_h = 0
    for i, h in enumerate(structure[max_i + 1:][::-1]):
        if h > tmp_h:
            surface += h
            tmp_h = h
        else:
            surface += tmp_h

    return surface


N = int(input())

nemos = [list(map(int, input().split())) for _ in range(N)]

structure = make_structure(nemos)
print(get_surface(structure))
