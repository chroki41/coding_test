# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = []
    
    list_of_words = []
    i = 0
    for j in range(len(words)):
        item = words[j]
        i += 1
        # print(j, words[j-1], item, words[j-1][-1], item[0])
        if item in list_of_words or (j > 0  and item[0] != words[j-1][-1]):
            if i % n != 0:
                return [i % n, (i//n) + 1]
            elif i % n == 0:
                return [n, i//n]
        list_of_words.append(item)
        
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    # print('Hello Python')

    return [0, 0]
