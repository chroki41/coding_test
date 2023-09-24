# https://school.programmers.co.kr/learn/courses/30/lessons/92335#

def solution(n, k):
    num_s = ""
    while n != 0:
        num_s = str(n % k) + num_s
        n = n // k
    num_l = num_s.split("0")
    
    prime_num = 0
    for item in num_l:
        if item != '' and item != '1':
            if is_prime(int(item)):
                prime_num += 1
    return prime_num


def is_prime(num):
    for i in range(2, int(num**(1/2))+1):
        if num%i == 0:
            return False
    return True
