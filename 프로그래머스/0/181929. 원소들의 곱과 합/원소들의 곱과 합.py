import math
def solution(num_list):
    prod = math.prod(num_list)
    sum_2=(lambda x:sum(x)**2)(num_list)
    answer=1 if prod<sum_2 else 0
    return answer