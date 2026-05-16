from collections import Counter
def solution(participant, completion):
    answer = Counter(participant) - Counter(completion)
    # print(Counter(participant),Counter(completion))
    return list(answer.keys())[0]