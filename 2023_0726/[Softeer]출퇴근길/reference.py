import sys
sys.stdin = open('input.txt')

def DFS(now, adj, visit):
    if visit[now] == 1:
        return
    else:
        visit[now] = 1
        for neighbor in adj[now]:
            DFS(neighbor, adj, visit)
    return


if __name__ == "__main__":
    n, m = map(int, input().split())  # 정점, 간선 
    adj = [[] for _ in range(n + 1)]  # 노드별 이동 가능한 노드들 정보
    adjR = [[] for _ in range(n + 1)]  # adj_reverse
    for _ in range(m):
        a, b, = map(int, input().split())
        adj[a].append(b)  # a노드에서 b노드로 갈수 있음
        adjR[b].append(a)
    S, T = map(int, input().split())  # S->T S가 집 T가 회사

    # print(adj)
    # print(adjR)

    # 목적: S->T와 T->S로 모두에서 방문 가능한 정점의 개수를 출력한다.
    fromS = [0] * (n + 1)
    fromS[T] = 1  # S->T 1로 미리 세팅
    DFS(S, adj, fromS)

    fromT = [0] * (n + 1)
    fromT[S] = 1  # T->S 1로 미리 세팅
    DFS(T, adj, fromT)

    toS = [0] * (n + 1)
    DFS(S, adjR, toS)

    toT = [0] * (n + 1)
    DFS(T, adjR, toT)

    count = 0
    print(fromS)
    print(fromT)
    print(toS)
    print(toT)
    for i in range(1, n + 1):
        if fromS[i] and fromT[i] and toS[i] and toT[i]:  # 이렇게가는거랑 저렇게 가는거랑 모두 1일때만
            count += 1

    print(count - 2)