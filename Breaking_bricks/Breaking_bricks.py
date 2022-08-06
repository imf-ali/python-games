import imp
import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Breaking Bricks")

bat = pygame.image.load('./images/paddle.png')
bat = bat.convert_alpha()
bat_rect = bat.get_rect()
bat_rect[0] = (screen.get_width() - bat_rect[2]) / 2
bat_rect[1] = screen.get_height() - 100

ball = pygame.image.load('./images/football.png')
ball = ball.convert_alpha()
ball_rect = ball.get_rect()
ball_start = ((screen.get_width() - ball_rect[2])/2,200)
ball_speed = (3.0 , 3.0)
ball_served = False
vx ,vy = ball_speed
ball_rect.topleft = ball_start

brick = pygame.image.load('./images/brick.png')
brick = brick.convert_alpha()
brick_rect = brick.get_rect()
bricks = []
brick_gap = 10 
brick_rows = 5
brick_col = screen.get_width() // (brick_rect[2] + brick_gap)
side_gap = (screen.get_width() - (brick_rect[2] + brick_gap) * brick_col + brick_gap) // 2

for y in range(brick_rows):
    brickY = y * (brick_rect[3] + brick_gap)
    for x in range(brick_col):
        brickX = x * (brick_rect[2] + brick_gap) + side_gap
        bricks.append((brickX,brickY))

clock = pygame.time.Clock()
game_over = False
while not game_over:
    dt = clock.tick(50)
    screen.fill((0,0,0))

    for b in bricks:
        screen.blit(brick,b)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    pressed = pygame.key.get_pressed()

    if pressed[K_LEFT]:
        bat_rect[0] -= 0.5 * dt
        if bat_rect[0] < 0:
            bat_rect[0] = 0
    if pressed[K_RIGHT]:
        bat_rect[0] += 0.5 * dt
        if bat_rect[0] > screen.get_width() - bat_rect[2]:
            bat_rect[0] = screen.get_width() - bat_rect[2]

    if pressed[K_SPACE]:
        ball_served = True
    
    if ball_served:
        ball_rect[0] += vx
        ball_rect[1] += vy

        if((bat_rect[0] <= ball_rect[0] <= bat_rect[0] + bat_rect[2]) and 
            (bat_rect[1] <= ball_rect[1] + ball_rect[3]) and
            (vy > 0)):
            vy = -vy
            vx *= 1.2
            vy *= 1.2

        delete_bricks = None
        for b in bricks:
            bx, by =b
            if  ((bx <= ball_rect[0] <= bx + brick_rect[2]) and
                (by <= ball_rect[1] <= by + brick_rect[3])):
                delete_bricks = b

                if (ball_rect[0] <= bx + 2) or (ball_rect[0] >= bx + brick_rect[2] - 2):
                    vx = -vx
                if (ball_rect[1] <= by + 2) or (ball_rect[1] >= by + brick_rect[3] - 2):
                    vy = -vy
                break

        if delete_bricks is not None:
            bricks.remove(delete_bricks)

        if ball_rect[0] <= 0:
            ball_rect[0] = 0
            vx = -vx
        
        if ball_rect[1] <= 0:
            ball_rect[1] = 0
            vy = -vy

        if ball_rect[0] > screen.get_width() - ball_rect[2]:
            ball_rect[0] = screen.get_width() - ball_rect[2]
            vx = -vx

        if ball_rect[1] > screen.get_height() - ball_rect[3]:
            ball_served = False
            ball_rect.topleft = ball_start
        
        
    screen.blit(bat,bat_rect)
    screen.blit(ball,ball_rect)

    pygame.display.update()

pygame.quit()