import numpy as np
import math
def y(x,r):
    return np.sqrt(r**2-x**2)

def solution(r1, r2):
    # y는 무조건 양수, 
    y1 = [y(i,r1) for i in range(-r1, r1+1)]
    y2 = [y(i,r2) for i in range(-r2, r2+1)]
    big_num = 0
    small_num = 0
    for i in y2:
        if i == 0:
            big_num +=1
        else:
            big_num += math.floor(i)*2 +1
    for i in y1:
        if i != 0:
            if math.floor(i) == i:
                small_num += (i-1)*2 +1
            else:
                small_num += math.floor(i)*2 +1
    return big_num -small_num
                
