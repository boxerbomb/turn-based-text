import pygame
from pygame.locals import *

SIZE = 400, 400
RED = (255, 0, 0)
BLUE = (0,0,255)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

board = [
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
[1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
[1,0,0,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
[1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]


rect = Rect(50, 60, 200, 80)
print(f'x={rect.x}, y={rect.y}, w={rect.w}, h={rect.h}')
print(f'left={rect.left}, top={rect.top}, right={rect.right}, bottom={rect.bottom}')
print(f'center={rect.center}')

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill(GRAY)
    for y in range(0,20):
        for x in range(0,20):
            current_rect = Rect(y*20,x*20,20,20)
            color_index = board[y][x]
            if color_index==0:
                pygame.draw.rect(screen, RED, current_rect)
            else:
                pygame.draw.rect(screen, BLUE, current_rect)
    pygame.display.flip()

    pygame.image.save_extended(screen,"images/img.jpg")
    pygame.quit()
