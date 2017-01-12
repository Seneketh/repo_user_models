import pygame

bgcolor = (36,36,72)
black = (0, 0, 0)
obstaclecolor = (18,108,18)
playercolor = (108, 18, 18)
green = (0, 255, 0)
blue = (0,0,255)
selected = (255, 0, 0)
red = (255, 0, 0)
menu_background = (100, 100, 100)
white = (255, 255, 255)

def updateScreen(game_display, playerbody, obstacles):
    game_display.fill(bgcolor)
    pygame.draw.rect(game_display, playercolor, [playerbody.xloc - playerbody.xsize * 0.5, playerbody.yloc - playerbody.ysize * 0.5 , playerbody.xsize, playerbody.ysize])
    for obstacle in obstacles:
        pygame.draw.rect(game_display, obstaclecolor, [obstacle.xloc - obstacle.xsize * 0.5, obstacle.yloc, obstacle.xsize, obstacle.ysize])
