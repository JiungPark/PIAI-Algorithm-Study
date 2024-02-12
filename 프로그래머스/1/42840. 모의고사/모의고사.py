def solution(answers):
    scores = [0]*3
    patterns = [[1,2,3,4,5], [2,1,2,3,2,4,2,5],[3,3,1,1,2,2,4,4,5,5]]
    for i, answer in enumerate(answers):
        for j, pattern in enumerate(patterns):
            if answer == pattern[i%len(pattern)]:
                scores[j] += 1
    score_num = []
    max_score = max(scores)
    for i,score in enumerate(scores):
        if score == max_score:
            score_num.append(i+1)
    return score_num