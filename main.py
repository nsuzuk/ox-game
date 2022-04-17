import pygame
import sys

import draw
import judge

pygame.init()
pygame.display.set_caption("OXゲーム")
sysfont1 = pygame.font.SysFont(None, 50)
sysfont2 = pygame.font.SysFont(None, 60)
board =[[0 for i in range(3)] for j in range(3)]
flag = [1, 5]

def initialize():
    for i in range(3):
        for j in range(3):
            board[i][j] = 0

def start():
    draw.draw_button("Start!", sysfont2, 50, 90, sysfont2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                return (judge.judge_button(0, x, y))
            elif event.type == pygame.QUIT:
                return (-1)

def restart():
    draw.draw_button("Restart!", sysfont1, 45, 90, sysfont2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                return (judge.judge_button(3, x, y))
            elif event.type == pygame.QUIT:
                return (-1)

def pause():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                return (3)
            elif event.type == pygame.QUIT:
                return (0)

def run_game():
    draw.squeare()
    initialize()

    round = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                round = judge.chart_judge(x, y, round, board, flag)
                if judge.judge(board):
                    return (2)
            elif event.type == pygame.QUIT:
                return (-1)

def main():
    game_flag = 0
    
    while True:
        if game_flag == 0:
            game_flag = start()
        if game_flag == 1:
            game_flag = run_game()
        if game_flag == 2:
            game_flag = pause()
        if game_flag == 3:
            game_flag = restart()
        if game_flag == -1:
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    main()
