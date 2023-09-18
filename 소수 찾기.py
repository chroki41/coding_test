#https://school.programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations

def solution(numbers):
    answer = 0
    temp = []
    for i in range(len(numbers)):
        temp.append(numbers[i])
    list_of_num = []
    for i in range(1, len(numbers)+1):
        combi = list(permutations(temp, i))
        for j in range(len(combi)):
            combi[j] = int("".join(combi[j]))
        list_of_num = list_of_num + combi
    list_of_num = list(set(list_of_num))
    for item in list_of_num:
        if is_prime(item) and item != 1 and item != 0:
            answer+=1
    
    return answer

def is_prime(number):
    for i in range(number-2):
        if number%(i+2) == 0:
            return False
    return True
