def solution(picture, k):
    answer =[]
    for p in picture:
        ch=''
        for r in p:
            ch+=r*k
        # print(ch)
        for _ in range(k):
            answer.append(ch)
    return answer