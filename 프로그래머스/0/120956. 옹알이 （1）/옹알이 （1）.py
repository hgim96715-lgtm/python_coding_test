import re
def solution(babbling):
    answer = 0
    for b in babbling:
        if re.fullmatch("(aya|ye|woo|ma)+", b):
            answer+=1
    return answer