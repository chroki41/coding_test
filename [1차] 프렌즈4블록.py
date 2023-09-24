# https://school.programmers.co.kr/learn/courses/30/lessons/17679

def solution(m, n, board):
    list_to_remove = [1]
    removed_num = 0
    
    new_board = [["1" for j in range(n)] for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            new_board[i][j] = board[i][j]
    board = new_board

    while len(list_to_remove) != 0:
        list_to_remove = delete_item(m, n, board)
        removed_num += len(list_to_remove)
        for item in list_to_remove:
            board[item[0]][item[1]] = "0"
        for i in range(m):
            board = slide_board(m, n, board)
            
    return removed_num


def slide_board(m, n, board):
    for i in reversed(range(m-1)):
        for j in range(n):
            if board[i][j] != "0" and board[i+1][j] == "0":
                board[i+1][j] = board[i][j]
                board[i][j] = "0"
    return board

def delete_item(m, n, board):
    list_to_remove = []
    for i in range(m-1):
        for j in range(n-1):
            temp = board[i][j]
            if temp == board[i+1][j] and temp == board[i][j+1] and temp == board[i+1][j+1] and temp != "0":
                if (i, j) not in list_to_remove:
                    list_to_remove.append((i, j))
                if (i+1, j) not in list_to_remove:
                    list_to_remove.append((i+1, j))
                if (i, j+1) not in list_to_remove:
                    list_to_remove.append((i, j+1))
                if (i+1, j+1) not in list_to_remove:
                    list_to_remove.append((i+1, j+1))
    return list_to_remove
