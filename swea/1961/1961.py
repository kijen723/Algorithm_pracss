# swea 1964 Python

T = int(input())

for test_case in range(1, T + 1):
    print(f"#{test_case}")
    
    N = int(input())
    
    matrix = []
    answer = [[], [], []]
    
    for i in range(N):
        matrix.append(list(map(str, input().split())))
    
    for i in range(N):
        temp1, temp2, temp3 = "", "", ""
        
        for j in range(N):
            temp1 += matrix[N - 1 - j][i]
            temp2 += matrix[N - 1 - i][N - 1 - j]
            temp3 += matrix[j][N - 1 - i]
        
        print(f"{temp1} {temp2} {temp3}")
