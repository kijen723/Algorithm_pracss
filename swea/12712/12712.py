# swea 12712 Python

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    flies = []
    answer = 0
    
    for i in range(N):
        flies.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            kill1 = flies[i][j]
            kill2 = flies[i][j]
            
            for k in range(1, M):
                if i + k <= N - 1:
                    kill1 += flies[i+k][j]
                
                if i - k >= 0:
                    kill1 += flies[i-k][j]
                
                if j + k <= N - 1:
                    kill1 += flies[i][j+k]
                
                if j - k >= 0:
                    kill1 += flies[i][j-k]
            
            for k in range(1, M):
                if i + k <= N - 1 and j + k <= N - 1:
                    kill2 += flies[i+k][j+k]
                
                if i - k >= 0 and j - k >= 0:
                    kill2 += flies[i-k][j-k]
                
                if j + k <= N - 1 and i - k >= 0:
                    kill2 += flies[i-k][j+k]
                
                if j - k >= 0 and i + k <= N - 1:
                    kill2 += flies[i+k][j-k]
            
            answer = max(answer, kill1, kill2)
    
    print(f"#{test_case} {answer}")
