def solution(board, k):
    answer = 0
    for i,boa in enumerate(board):
        for j,bo in enumerate(boa):
            if i+j<=k:
                answer+=bo
    return answer