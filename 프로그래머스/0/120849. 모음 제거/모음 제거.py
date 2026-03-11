def solution(my_string):
    answer = ''
    for s in my_string:
        if s in "aeiou":
            answer+=''
        else:
            answer+=s
    return answer