def solution(numbers):
    numbers=sorted(numbers,reverse=True)
    answer = max([numbers[0]*numbers[1] for i in range(len(numbers)-1)])
    return answer