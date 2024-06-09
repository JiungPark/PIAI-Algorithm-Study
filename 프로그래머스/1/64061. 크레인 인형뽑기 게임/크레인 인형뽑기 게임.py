def solution(board, moves):
    # 각 열에 대한 스택을 생성
    lanes = [[] for _ in range(len(board[0]))]
    # board를 역순으로 탐색하며, 각 열의 인형을 lanes에 추가
    
    for i in range(len(board) -1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j]:
                lanes[j].append(board[i][j])
                
    # 인형에 담을 bucket을 생성
    bucket = []
    
    # 사라진 인형의 총 개수를 저장할 변수를 초기화
    answer = 0
    
    # moves를 순회하며 각 열에서 인형을 뽑아 bucket에 추가
    for m in moves:
        if lanes[m-1]:
            doll = lanes[m-1].pop()

            if bucket and bucket[-1] == doll: # 바구니에 인형이 있고 가장 위에 있는 인형과 같은 경우

                bucket.pop()
                answer += 2
            else: # 바구니에 인형이 없거나 가장 위에 있는 인형과 다른 경우
                bucket.append(doll)
    return answer