def solution(price, money, count):
    answer = 0
    for p in range(1,count+1):
        answer+=p*price
    return answer-money if answer>money else 0