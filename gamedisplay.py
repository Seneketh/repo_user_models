import pygame


bgcolor = (36,36,72)
black = (0, 0, 0)
obstaclecolor = (18,108,18)
playercolor = (108, 18, 18)
green = (0, 255, 0)
blue = (0,0,255)
selected = (255, 0, 0)

def updateScreen(game_display, playerbody, obstacles, collumnwidth):
    game_display.fill(bgcolor)
    pygame.draw.rect(game_display, playercolor, [playerbody.xloc * collumnwidth, playerbody.yloc * collumnwidth, playerbody.xsize*collumnwidth, playerbody.ysize * collumnwidth])
    for obstacle in obstacles:
        pygame.draw.rect(game_display, obstaclecolor, [obstacle.xloc * collumnwidth, obstacle.yloc * collumnwidth, obstacle.xsize * collumnwidth, obstacle.ysize * collumnwidth])