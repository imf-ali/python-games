import pygame
pygame.init()

def drawGrid(screen,rows,cols,x_gap,y_gap,grid_size):
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen,(100,100,100),[x * grid_size + x_gap,y * grid_size + y_gap,grid_size,grid_size],1)

def main():
    screen = pygame.display.set_mode((800,700))
    pygame.display.set_caption('Tetris')
    grid_size = 30
    cols = screen.get_width() // grid_size
    rows = screen.get_height() // grid_size
    x_gap = (screen.get_width() - cols * grid_size) // 2
    y_gap = (screen.get_height() - rows * grid_size) // 2

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
        screen.fill((0,0,0))
        drawGrid(screen,rows,cols,x_gap,y_gap,grid_size)
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()