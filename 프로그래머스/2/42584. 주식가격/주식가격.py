# def solution(prices):
#     n = len(prices)
#     answer = [0] * n # 가격이 떨어지지 않은 기간을 저장할 배열
    
#     # 스택(stack)을 사용해 이전 가격과 현재 가격 비교
#     stack = [0] # 스택 초기화
#     for i in range(1,n):
#         while stack and prices[i] < prices[stack[-1]]:
#             # 가격이 떨어졌으므로 이전 가격의 기간 계산
#             j = stack.pop()
#             answer[j] = i - j
#         stack.append(i)
#     # 스택에 남아 있는 가격들은 가격이 떨어지지 않은 경우
#     while stack:
#         j = stack.pop()
#         answer[j] = n - 1 - j
        
#     return answer

def solution(prices):
    n = len(prices)
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            answer[i] += 1
            if prices[i] > prices[j]:
                break

    return answer

# 입출력 예시
prices = [1, 2, 3, 2, 3]
print(solution(prices))  # 출력: [4, 3, 1, 1, 0]
