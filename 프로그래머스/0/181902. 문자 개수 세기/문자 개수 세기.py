def solution(my_string):
    answer = [0]*52
    b=0
    # print(ord('z'),ord('A'))
    for v in my_string:
        if 'A'<=v<='Z':
            b=ord(v)-ord('A')
        else:
            b=ord(v)-ord('a')+26
        answer[b]+=1
    return answer