# swea 1206 Python

for test_case in range(1, 11):
    N = int(input())
    heights = list(map(int, input().split()))
    answer = 0

    for i in range(2, N - 2):
        left_count = min(heights[i] - heights[i - 1], heights[i] - heights[i - 2])
        right_count = min(heights[i] - heights[i + 1], heights[i] - heights[i + 2])

        if left_count > 0 and right_count > 0:
            answer += min(left_count, right_count)

    print(f"#{test_case} {answer}")
