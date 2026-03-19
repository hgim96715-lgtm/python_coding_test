def solution(keyinput, board):
    answer = [0,0]
    for k in keyinput:
        if k=='left':
            if answer[0] - 1 >= -(board[0]//2):
                answer[0]-=1
        elif k=='right':
            if answer[0] + 1 <= (board[0]//2):
                answer[0]+=1
        elif k=='up':
            if answer[1] + 1 <= (board[1]//2):
                answer[1]+=1
        elif k=='down':
            if answer[1] - 1 >= -(board[1]//2):
                 answer[1]-=1
    return answer