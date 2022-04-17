import pygame

SURFACE = pygame.display.set_mode((400,300))
SURFACE.fill((255, 255, 255))

def squeare():
    SURFACE.fill((255, 255, 255))
    pygame.draw.rect(SURFACE, (255, 140, 0), (90, 70, 190, 190))
    for x in range(9):
        left = (60 * (x // 3)) + 100
        top = (60 * (x % 3)) + 80
        pygame.draw.rect(SURFACE, (255, 228, 181), (left, top, 50, 50))
        pygame.display.update()

def draw_button(text2, charactar, x, y, quit):
    SURFACE.fill((240, 250, 250))
    pygame.draw.rect(SURFACE, (200, 240, 100), (40, 80, 140, 50))
    pygame.draw.rect(SURFACE, (200, 240, 100), (220, 80, 140, 50))
    message = charactar.render(text2, True, (0, 128, 128))
    message2 = quit.render("Quit", True, (0, 128, 128))
    SURFACE.blit(message,[x, y])
    SURFACE.blit(message2,[240, 90])
    pygame.display.update()

def caption(text):
    sysfont = pygame.font.SysFont(None, 72)
    message = sysfont.render(text, True, (0, 128, 128))
    message_rect = message.get_rect()
    message_rect.center = (200, 35)
    SURFACE.blit(message,message_rect)
    pygame.display.update()

def circle(i, j):
    i = 125 + 60 * i
    j = 105 + 60 * j
    pygame.draw.circle(SURFACE, (255, 0, 0), (i,j), 22, 5)

def cross(i, j):
    st_left = 60 * i + 104
    st_top = 60 * j + 84
    st1 = (st_left, st_top)
    st2 = ((st_left + 42), st_top)
    end1 = (st_left + 42, st_top + 42)
    end2 = (st_left, (st_top + 42))
    pygame.draw.line(SURFACE, (0, 0, 255), st1, end1, 7)
    pygame.draw.line(SURFACE, (0, 0, 255), st2, end2, 7)

def draw(i, j, board):
    if board[i][j] == 1:
        circle(i, j)
    elif board[i][j] == 5:
        cross(i, j)
    pygame.display.update()
