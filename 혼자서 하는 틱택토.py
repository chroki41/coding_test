# https://school.programmers.co.kr/learn/courses/30/lessons/160585#

from itertools import combinations

def solution(board):
    total_num = [0, 0]
    for element in board:
        for char in element:
            if char == "O":
                total_num[0] += 1
            elif char == "X":
                total_num[1] += 1
    if not (total_num[0] - total_num[1] <= 1 and total_num[0] - total_num[1] >= 0):
        return 0
    bingo_case = [(0, 1, 2), (0, 4, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (3, 4, 5), (6, 7, 8), (2, 4, 6)]
    x_list = list(combinations(bingo(board, "X"), 3))
    o_list = list(combinations(bingo(board, "O"), 3))
    x_bool = False
    o_bool = False
    o_num = 0
    x_num = 0
    for item in x_list:
        if item in bingo_case:
            x_bool = True
            x_num += 1
    for item in o_list:
        if item in bingo_case:
            o_bool = True
            o_num += 1
    if x_bool and o_bool:
        return 0
    
    if x_bool and total_num[0] - total_num[1] == 1:
        return 0
    
    if o_bool and total_num[0] == total_num[1]:
        return 0
    
    return 1

def bingo(board, character):
    places = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == character:
                places.append(3*i + j)
    return places
