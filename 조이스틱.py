# https://school.programmers.co.kr/learn/courses/30/lessons/42860

def solution(name):
    answer = 10000000
    stringset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    string_list = [char for char in stringset]
    distance_list = [50 for item in name]
    for i in range(len(name)):
        if name[i] != "A":
            distance_list[i] = i
    
    for i in range(len(name)):
        distance_list[i] == i
    
    
    for i in range(len(name)//2 + 1):
        l_r = name[-i:] + name[:-i]
        r_l = name[i: :-1] + name[i+1:][::-1]
        for n in [l_r,r_l]:
            # 끝에 A들은 셀 필요 없으므로 자르기
            while n and n[-1] == 'A':
                n = n[:-1]
            cnt = [0 for char in n]
            answer = min(answer, i + (len(cnt)-1))
    answer = max(answer, 0)
    for item in name:
        answer += change_letter(item, string_list)

    return answer

def change_letter(char, string_list):
    for i in range(26):
        if string_list[i] == char:
            return min(i, 26-i)
