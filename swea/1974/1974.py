# swea 1974.py

T = int(input())

for test_case in range(1, T + 1):
    answer = 1
    width = []
    
    for i in range(9):
        width.append(list(map(int, input().split())))
        
        if len(set(width[i])) != 9:
            answer = 0
    
    if answer == 1:
        for i in range(9):
            length = []
            
            for j in range(9):
                length.append(width[j][i])
                
            if len(set(length)) != 9:
                answer = 0
                break
    
    if answer == 1:
        for i in range(3):
            for j in range(3):
                square = []
                
                for k in range(3):
                    for l in range(3):
                        square.append(width[k+(i*3)][l+(j*3)])
                        
                if len(set(square)) != 9:
                    answer = 0
                    break
    
    print(f"#{test_case} {answer}")
