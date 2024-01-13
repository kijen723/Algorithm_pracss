# swea 1954 Python

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    
    answer = [[0] * N for i in range(N)]
    pos = [0, -1]
    dir_pos = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    num, count, now_dir = 1, 2, 0
    
    for i in range((N * 2) - 1):
        for j in range(N):
            pos = [pos[0] + dir_pos[now_dir % 4][0], pos[1] + dir_pos[now_dir % 4][1]]
            answer[pos[0]][pos[1]] = num
            num += 1
        
        if count == 2:
            count = 0
            N -= 1
        
        count += 1 
        now_dir += 1
    
    print(f"#{test_case}")
    for i in answer:
        print(*i)
