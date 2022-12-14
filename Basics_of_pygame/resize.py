import pygame
pygame.init()
display = pygame.display.set_mode((700,700), 0, 32)
sprite1 = pygame.image.load('./images/butterfly.png')
sprite1 = pygame.transform.scale(sprite1, (80,80))  # width, height
spriteHeight = sprite1.get_height()
spriteWidth = sprite1.get_width() 
pygame.display.set_caption("Hello Pygame")
display.fill((0,0,0))
game_over = False
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    display.blit(sprite1, (display.get_width()/2 - spriteWidth/2, display.get_height()/2 - spriteHeight/2))  # 700/2 - 256/2 = 350 - 128 = 222
    pygame.display.update()
pygame.quit()