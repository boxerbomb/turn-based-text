import pygame
from pygame.locals import *

BLOCK_SIZE=16
SCREEN_WIDTH = (BLOCK_SIZE*20)+(1*BLOCK_SIZE)
SCREEN_HEIGHT = (BLOCK_SIZE*20)+(3*BLOCK_SIZE)
SIZE = SCREEN_WIDTH, SCREEN_HEIGHT

RED = (255, 0, 0)
BLUE = (0,0,255)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

board = [
[0,0,1,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0],
[0,0,1,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0],
[0,0,0,1,1,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
]


obj_board = [
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,34,32,32,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,33,33,33,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,30,31,30,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0],
[0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0],
[0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0,0],
[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]


grid_image = pygame.image.load("res/grid.png")


grass_tiles = []
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass1.png"))
grass_tiles.append(pygame.image.load("res/grass2.png"))
grass_tiles.append(pygame.image.load("res/grass3.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))
grass_tiles.append(pygame.image.load("res/grass0.png"))


floor_tiles = []
floor_tiles.append(pygame.image.load("res/floor0.png"))
floor_tiles.append(pygame.image.load("res/floor0.png"))
floor_tiles.append(pygame.image.load("res/floor1.png"))
floor_tiles.append(pygame.image.load("res/floor2.png"))
floor_tiles.append(pygame.image.load("res/floor3.png"))
floor_tiles.append(pygame.image.load("res/floor4.png"))
floor_tiles.append(pygame.image.load("res/floor0.png"))

tall_grass_tiles = []
tall_grass_tiles.append(pygame.image.load("res/tall_grass_0.png"))
tall_grass_tiles.append(pygame.image.load("res/tall_grass_1.png"))
tall_grass_tiles.append(pygame.image.load("res/tall_grass_2.png"))
tall_grass_tiles.append(pygame.image.load("res/tall_grass_3.png"))
tall_grass_tiles.append(pygame.image.load("res/tall_grass_4.png"))

#30
b_wall = pygame.image.load("res/b_wall.png")
#31
b_door = pygame.image.load("res/b_door.png")
#32
b_roof = pygame.image.load("res/b_roof.png")
#33
b_roof_edge = pygame.image.load("res/b_roof_edge.png")
#34
b_chiminey = pygame.image.load("res/b_chiminey.png")



running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill(GRAY)

    screen.blit(grid_image,(0,0))

    # Backdrop
    for y in range(0,20):
        for x in range(0,20):
            color_index = board[y][x]
            if color_index==0:
                grass_index = hash(hash(x)-hash(y)+hash(x*x)-hash(x*y))%18
                screen.blit(grass_tiles[grass_index], ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            else:
                floor_index = hash(hash(y)-hash(x)+hash(y*y-x)-hash(x*y))%7
                screen.blit(floor_tiles[floor_index], ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))

    # Objects
    for y in range(0,20):
        for x in range(0,20):
            tile_index = obj_board[y][x]
            if tile_index==0:
                pass
            elif tile_index==1:
                tall_grass_index = hash(hash(y)-hash(x)+hash(y*y-x)-hash(x*y))%4
                screen.blit(tall_grass_tiles[tall_grass_index], ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==30:
                screen.blit(b_wall, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==31:
                screen.blit(b_door, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==32:
                screen.blit(b_roof, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==33:
                screen.blit(b_roof_edge, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))
            elif tile_index==34:
                screen.blit(b_chiminey, ((x+1)*BLOCK_SIZE,(y+1)*BLOCK_SIZE))

    # Debug Lines
    #for x in range(0,SCREEN_WIDTH,BLOCK_SIZE):
    #    pygame.draw.line(screen, RED, (x,0), (x,SCREEN_HEIGHT))
    #for y in range(0,SCREEN_HEIGHT,BLOCK_SIZE):
    #    pygame.draw.line(screen, RED, (0,y), (SCREEN_WIDTH,y))

    pygame.display.flip()
    #running=False
pygame.image.save_extended(screen,"final.jpg")
pygame.quit()
