import re
def solution(my_string):
    answer = 0
    nums=re.findall('[0-9]+', my_string)
    answer=sum([int(n) for n in nums])
    return answer