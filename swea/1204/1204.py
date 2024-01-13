# swea 1204 Python

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    scores = list(map(int, input().split()))

    dictionary_of_scores = {}
    
    for score in scores:
        if score in dictionary_of_scores:
            dictionary_of_scores[score] += 1
        else:
            dictionary_of_scores[score] = 1
    
    sorted_dictionary = sorted(dictionary_of_scores.items(), key = lambda item: (item[1], item[0]), reverse=True)
    
    answer = sorted_dictionary[0][0]
    
    print(f"#{N} {answer}")
