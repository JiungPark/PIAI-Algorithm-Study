def solution(park, routes):
    # 공원의 크기 파악
    H = len(park)
    W = len(park[0])
    
    # 방향 벡터 정의
    direction_map = {
        'N': (-1, 0),
        'S': (1, 0),
        'W': (0, -1),
        'E': (0, 1)
    }
    
    # 로봇 강아지 초기 위치 파악
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x, y = i, j
                break
    
    # 명령에 따라 이동
    for route in routes:
        direction, distance = route.split()
        distance = int(distance)
        dx, dy = direction_map[direction]
        
        # 이동 가능한지 확인
        nx, ny = x, y
        valid_move = True
        for _ in range(distance):
            nx += dx
            ny += dy
            if not (0 <= nx < H and 0 <= ny < W) or park[nx][ny] == 'X':
                valid_move = False
                break
        
        # 이동이 가능하면 이동
        if valid_move:
            x, y = nx, ny
    
    return [x, y]

