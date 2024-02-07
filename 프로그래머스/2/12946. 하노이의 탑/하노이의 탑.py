'''
...->n-2을 3번기둥으로-> n-1을 2번 기둥으로-> n을 3번 기둥으로
만약 n이 4이다.
### (1,2,3)원판 묶음을 하나로 볼때 ###
[[1,2],[1,3],[2,3]]
### 여기서 [1,2]와 [2,3]은 한번 더 풀어야함, (1,2)원판 묶음을 하나로 볼 때(중간 idx제외한 부분)
[1,2]의 경우: [[1,3],[1,2],[3,2]], [2,3]의 경우: [[2,1],[2,3],[1,3]]\
### 여기서 마지막으로 한번 더 풀어야함(중간 idx제외)
[2,1]의 경우: [[2,3],[2,1],[3,1]], [2,3]의 경우: [[2,1],[2,3],[1,3]],
[1,3]의 경우: [[1,2],[1,3],[2,3]]
'''
'''
def hanoi(start, end):
    a = [1, 2, 3]
    a.remove(start)
    a.remove(end)
    mid = a[0]  # 중간 기둥은 나머지 하나의 기둥
    return [[start, mid], [start, end], [mid, end]]

def change_hanoi(x):
    for i in [1, 2, 3]:
        for j in [1, 2, 3]:
            if i != j and x == [i, j]:
                return hanoi(i, j)
    return None  

def update(li_n, li_n_1, li_n_2):
    new_list = []
    if li_n_1 is not None:
        new_list += li_n_1
    new_list.append(li_n[1])
    if li_n_2 is not None:
        new_list += li_n_2
    return new_list  

def add_mid(x, y):
    x.insert(len(x) // 2, y)
    return x

def transform_hanoi(x, y):
    n_list = update(hanoi(x, y), change_hanoi(hanoi(x, y)[0]), change_hanoi(hanoi(x, y)[2]))
    return n_list

def solution(n):
    current_list = []
    answer = []
    if n == 1:
        return []
    elif n == 2:
        return hanoi(1, 3)
    # n=3일때는 (1,2)원판을 한묶음으로 했을 때, [1,3]으로 옮겨야하고 이것은 [[1,2],[1,3],[2,3]]인데
    # 여기에서 중간값을 제외하고 나머지 부분을 (1,2)원판을 옮기는 것으로 바꿔야함
    else:
        current_list = hanoi(1, 3)
        for _ in range(n - 2):
            mid_idx = (len(current_list) + 1) // 2 - 1
            mid_value = current_list[mid_idx]
            for idx, li in enumerate(current_list):
                # 만약 리스트의 길이가 l이면 index가 (l+1)/2 인 부분을 제외하고 나머지에 다 변환 수행
                if idx != mid_idx:
                    tmp = transform_hanoi(li[0], li[1])
                    for j in tmp:
                        answer.append(j)
            add_mid(answer, mid_value)
            current_list = answer.copy()  
            answer = []  
        return current_list
'''

## 시간초과 및 답이 아님 --> 재귀함수 사용
def hanoi(n, start, end, aux):
    if n == 1:
        return [[start, end]]
    else:
        # 1. n-1개의 원판을 보조 기둥으로 옮김
        moves = hanoi(n - 1, start, aux, end)
        # 2. 가장 큰 원판을 목표 기둥으로 옮김
        moves.append([start, end])
        # 3. 보조 기둥에 있는 n-1개의 원판을 목표 기둥으로 옮김
        moves += hanoi(n - 1, aux, end, start)
        return moves

def solution(n):
    return hanoi(n, 1, 3, 2)






        

    
    