# https://school.programmers.co.kr/learn/courses/30/lessons/12980

# def solution(n):
    
#     dp = [i for i in range(n+1)]
#     for i in range(1, n+1):
#         if (i)%2 == 0:
#             dp[i] = min(dp[i-1] + 1, dp[i//2])
#         else:
#             dp[i] = dp[i-1] + 1
#     return dp[-1]

def solution(n):
    answer = 0
    while n != 1:
        if n%2 == 0:
            n /= 2
        else:
            n -= 1
            answer +=1
    return answer + 1
