def solution(food):

    left_side = []
    for i in range(1, len(food)):
        count = food[i] // 2
        left_side.append(str(i) * count)
    
    left_part = ''.join(left_side)
    
    center = '0'
    
    right_part = ''.join(left_side[::-1])
    
    final_placement = left_part + center + right_part
    
    return final_placement


