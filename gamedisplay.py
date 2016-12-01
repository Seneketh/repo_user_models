import pygame

bgcolor = (36,36,72)
black = (0, 0, 0)
obstaclecolor = (18,108,18)
playercolor = (108, 18, 18)
green = (0, 255, 0)
blue = (0,0,255)
selected = (255, 0, 0)

<<<<<<< HEAD

def updateScreen(game_display, playerbody, obstacles):
=======
<<<<<<< HEAD

def updateScreen(game_display, playerbody, obstacles):
=======
def updateScreen(game_display, playerbody, obstacles, collumnwidth):
>>>>>>> e18bfcd2e94310b5d61e50c1aa64366a765b0e94
>>>>>>> 1355fbf206f406fe839a3608b52f55cd4afdf123
    game_display.fill(bgcolor)
    pygame.draw.rect(game_display, playercolor, [playerbody.xloc - playerbody.xsize * 0.5, playerbody.yloc - playerbody.ysize * 0.5 , playerbody.xsize, playerbody.ysize])
    for obstacle in obstacles:
<<<<<<< HEAD
        pygame.draw.rect(game_display, obstaclecolor, [obstacle.xloc - obstacle.xsize * 0.5, obstacle.yloc, obstacle.xsize, obstacle.ysize])
=======
<<<<<<< HEAD
        pygame.draw.rect(game_display, obstaclecolor, [obstacle.xloc - obstacle.xsize * 0.5, obstacle.yloc, obstacle.xsize, obstacle.ysize])
=======
        pygame.draw.rect(game_display, obstaclecolor, [obstacle.xloc * collumnwidth, obstacle.yloc * collumnwidth, obstacle.xsize * collumnwidth, obstacle.ysize * collumnwidth])
>>>>>>> e18bfcd2e94310b5d61e50c1aa64366a765b0e94
>>>>>>> 1355fbf206f406fe839a3608b52f55cd4afdf123
