import pygame
pygame.init()
display = pygame.display.set_mode((640,480), 0, 32)
sprite1 = pygame.image.load('./images/football.png')
pygame.display.set_caption("Hello Pygame")
display.fill((0,0,0))
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    display.blit(sprite1, (320,240))  # x,y coordinates
    pygame.display.update()
pygame.quit()