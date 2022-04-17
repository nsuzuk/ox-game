import pygame
import draw

def win_judge(board):
    for x in range(3):
        tate = board[x][0] + board[x][1] + board[x][2] 
        yoko = board[0][x] + board[1][x] + board[2][x]
        naname1 = board[0][0] + board[1][1] + board[2][2]
        naname2 = board[0][2] + board[1][1] + board[2][0]
        if tate == 3 or yoko == 3 or naname1 == 3 or naname2 == 3:
            draw.caption("Round Win !")
            return (1)
        if tate == 15 or yoko == 15 or naname1 == 15 or naname2 == 15:
            draw.caption("Cross Win !")
            return (1)
    return (0)

def drow_judge(board):
    for x in range(3):
        for y in range(3):
            if board[x][y] == 0:
                return (0)
    draw.caption("Drow !")
    return (1)

def judge(board):
    if win_judge(board):
        return (1)
    if drow_judge(board):
        return (1)
    return (0)
    
def chart_judge(x, y, round, board, flag):
    for i in range(3):
        if i * 60 + 100 <= x <= i * 60 + 150:
            for j in range(3):
                if j * 60 + 80 <= y <= j * 60 + 130:
                    if board[i][j] == 0:
                        board[i][j] = flag[round % 2]
                        draw.draw(i, j, board)
                        judge(board)
                        return(round + 1)
    return(round)

def judge_button(flag, x, y):
    if 80 <= y <= 130:
        if 40 <= x <= 180:
            return (1)
        elif 220 <= x <= 360:
            return (-1)
    return(flag)
