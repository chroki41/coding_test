# https://school.programmers.co.kr/learn/courses/30/lessons/12945

def solution(num):
    fib_list = [0 for i in range(num)]
    fib_list[0] = 1
    fib_list[1] = 1
    for i in range(2, num):
        # print(i, fib_list[i-1], fib_list[i-2], (fib_list[i-1] + fib_list[i-2])%1234567)
        fib_list[i] = (fib_list[i-1] + fib_list[i-2])%1234567

    # print(fib_list)
    return fib_list[-1]
