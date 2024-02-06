import copy
import numpy as np
# n_list = []
# s_list = []
# l_list = []
# def partial(sequence,k):
#     global n_list
#     global s_list
#     for n in sequence:
#         while n < k+1:
#             n_list.append(n)
#             if sum(n_list) >k:
#                 n_list = []
#             elif sum(n_list) == k:
#                 s_list.append(n_list)
#                 n_list = []
#     return partial(n_list,k)

# def solution(sequence, k):
#     partial(sequence,k)
#     for li in s_list:
#         min_len = np.float('inf')
#         if len(li) <= min_len:
#             min_len = len(li)
#             l_list.append(li)
            
#     return l_list[0]
# 시간 초과

# def solution(sequence, k):
#     n_list = []
#     l_list = []
#     length = 0
#     while length < k+1:
#         length += 1
#         for idx, n in enumerate(sequence): 
#             if idx+length< len(sequence):
#                 hap = sum([sequence[idx+i] for i in range(length)])
#                 if hap == k:
#                     n_list.append([idx+i for i in range(length)])
#         if len(n_list) != 0:
#             break
#     for li in n_list:
#         min_len = np.float('inf')
#         if len(li) <= min_len:
#             min_len = len(li)
#             l_list.append(li)
#     final_list = l_list[0]
#     return [final_list[0],final_list[-1]]
# 시간초과 +틀림

def solution(sequence, k):
    shortest_length = float('inf')
    shortest_start = 0
    shortest_end = 0
    
    start = 0
    current_sum = 0
    
    for end in range(len(sequence)):
        current_sum += sequence[end]
        
        while current_sum > k and start <= end:
            current_sum -= sequence[start]
            start += 1
        
        if current_sum == k:
            subsequence_length = end - start + 1
            if subsequence_length < shortest_length:
                shortest_length = subsequence_length
                shortest_start = start
                shortest_end = end
    
    return shortest_start, shortest_end

        
    
        
        

    
            
        
            
        
    
            
            
                
    
    
             
            
        
        
    
    
    
    
    
    
    
    
   