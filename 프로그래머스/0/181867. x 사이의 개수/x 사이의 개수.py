def solution(myString):
    answer = myString.split("x")
    a=[]
    for x in answer:
        a.append(len(x))
    return a