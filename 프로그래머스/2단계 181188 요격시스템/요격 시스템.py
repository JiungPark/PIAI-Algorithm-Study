def solution(targets):
    count = 0
    targets.sort(key= lambda x: x[1])
    end_point = float('-inf')
    
    for target in targets:
        start, end = target
        
        if start >= end_point:
            end_point = end
            count += 1
        
            
    return count







