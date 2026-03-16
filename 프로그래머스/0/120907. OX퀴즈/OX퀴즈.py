def solution(quiz):
    answer = []
    for q in quiz:
        q=q.split()
        a,op,b,_,c=q
        res= int(a) + int(b) if op == '+' else int(a) - int(b)
        # print(result)
        answer.append('X' if res!=int(c) else 'O')
    return answer