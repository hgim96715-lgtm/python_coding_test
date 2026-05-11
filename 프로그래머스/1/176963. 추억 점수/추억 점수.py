def solution(name, yearning, photo):
    answer = []
    score = dict(zip(name, yearning))
    # print(score)
    for phot in photo:
        total=0
        for ph in phot:
            total+=score.get(ph,0)
        answer.append(total)
    return answer