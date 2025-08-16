def solution(array):
    array.sort()
    median = len(array) // 2
    answer = array[median]
    return answer