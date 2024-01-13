# swea 1936 Python

A, B = map(int, input().split())

if A > B:
    if A == 3 and B == 1:
        print("B")
    else:
        print("A")
else:
    if B == 3 and A == 1:
        print("A")
    else:
        print("B")
