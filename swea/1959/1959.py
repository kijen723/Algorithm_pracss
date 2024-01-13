# swea 1959 Python

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    length_A, length_B = len(A), len(B)
    answer = 0
    
    if length_A < length_B:
        A, B = B, A
        length_A, length_B = length_B, length_A
    
    for i in range(length_A - length_B + 1):
        temp = 0

        for j in range(length_B):
            temp += A[j + i] * B[j]
        
        answer = max(answer, temp)
    
    print(f"#{test_case} {answer}")
