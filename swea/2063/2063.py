# swea 2063 Python

T = int(input())
numbers = sorted(list(map(int, input().split())))

target_index = T // 2

print(f"{numbers[target_index]}")
