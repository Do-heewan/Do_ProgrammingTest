def solution(array):
    array.sort() # 1번 : 메소드 : 클래스 내에서 동작하는 함수

    a = len(array) // 2
    answer = array[a]
    
    return answer