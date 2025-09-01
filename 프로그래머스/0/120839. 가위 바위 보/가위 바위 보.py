def solution(rsp):
    answer = ''
    for ix in rsp:
        if ix == "2":
            answer += "0"
        elif ix == "5":
            answer += "2"
        else:
            answer += "5"
    return answer