# def solution(arr):
#     answer = []
#     pow_2=[]
#     for i in range(1000):
#         pow_2+=[pow(2,i)]
#     while len(arr) not in pow_2:
#         arr.append(0)
        
#     return arr

def solution(arr):
    length = len(arr)
    target = 1 << (length - 1).bit_length()
    return arr + [0] * (target - length)