def solution(cipher, code):
    answer = ''
    arr=list(cipher)
    for i in range(code-1,len(cipher),code):
        answer+=cipher[i]
    return answer