import pygame
import dijkstra
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

DIMX = 5
DIMY = 5

WIDTH = 20
HEIGHT = 20
MARGIN = 5






grid = []
for row in range(DIMY):
    grid.append([])
    for column in range(DIMX):
        grid[row].append(0)

pygame.init()
WINDOW_SIZE = [(WIDTH+MARGIN)*DIMX + MARGIN, (HEIGHT+MARGIN)*DIMY + MARGIN]
screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption('Maze')

done = False
clock = pygame.time.Clock()
brush = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            brush = True
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1]// (WIDTH + MARGIN)
            grid[row][column]=1
        elif event.type == pygame.MOUSEBUTTONUP:
            brush = False
        elif event.type == pygame.MOUSEMOTION and brush:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1]// (WIDTH + MARGIN)
            grid[row][column]= -1 # !!!
            print("Click ", pos, "Grid coordinates: ", row, column)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                path = dijkstra.build_path(dijkstra.dijkstra_array(grid, (0,0), (4,4)), (0,0),(4,4))
                print('dijkstra')
                print(path)
                for cell in path:
                    grid[cell[0]][cell[1]] = "O"
    screen.fill(BLACK)

    for row in range(DIMY):
        for column in range(DIMX):
            color = WHITE
            if grid[row][column] == -1:
                color = GREEN
            if grid[row][column] == "O":
                color = RED
            pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                            (MARGIN + WIDTH) * row + MARGIN,
                                            WIDTH,
                                            HEIGHT])

    clock.tick(60)
    pygame.display.flip()

pygame.quit()