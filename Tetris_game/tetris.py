import pygame
pygame.init()

def drawGrid(screen, row, col, grid_size, x_gap, y_gap):
    for y in range(row):
            for x in range(col):
                pygame.draw.rect(screen,(100,100,100),[x * grid_size + x_gap,y * grid_size + y_gap,grid_size,grid_size],1)

def main():
    grid_size = 30

    screen = pygame.display.set_mode((500,600))
    pygame.display.set_caption("Tetris")
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
        drawGrid(screen, rows,cols,grid_size, x_gap, y_gap)
        pygame.display.update()
    pygame.quit() 

if __name__ == '__main__':
    main()