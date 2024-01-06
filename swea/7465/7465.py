# swea 7465.py

from collections import deque

def bfs(index):
    queue = deque()
    queue.append(index)
    
    while queue:
        target = queue.popleft()
        
        for i in relationships[target]:
            if check[i]:
                queue.append(i)
        
        check[target] = 0


T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    answer = 0
    relationships = [[] for i in range(N + 1)]
    check = [1] * (N + 1)
    
    for i in range(M):
        a, b = map(int, input().split())
        relationships[a].append(b)
        relationships[b].append(a)
    
    for i in range(1, N + 1):
        if check[i]:
            bfs(i)
            answer += 1
    
    print(f"#{test_case} {answer}")
