import pygame
from bomberman import bomberman
from wall import wall
from maze import maze

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)
GREEN = (152, 139, 152)

# Sets the height and width of each grid location
WIDTH = 20
HEIGHT = 20

# Margin between each cell
MARGIN = 5

def draw_board(screen, m):
    screen.fill(GREEN)
    for j in range(m.MAZE_SIZE-1, -1, -1):
        for i in range(m.MAZE_SIZE):
            color = WHITE
            if isinstance(m.maze[i][j], wall) and not m.maze[i][j].is_destructable:
                color = BLACK
            if isinstance(m.maze[i][j], wall) and m.maze[i][j].is_destructable:
                color = GREY
            if isinstance(m.maze[i][j], bomberman):
                color = RED
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * i + MARGIN,
                              (MARGIN + HEIGHT) * j + MARGIN,
                              WIDTH,
                              HEIGHT])

def main():
    # Game setup
    Bomberman = bomberman(0, 0)
    Maze = maze(Bomberman)
    Maze.build()

    # Graphics setup
    pygame.init()
    pygame.display.set_caption('Bomberman')

    # Start screen logic
    screen = pygame.image.load("startscreen.png")

    screen = pygame.display.set_mode([1200, 800])
    clock = pygame.time.Clock()

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == ord("w"):
                    Maze.move_bomberman(0, 1)
                    Maze.print_maze()
                if event.key == ord("d"):
                    Maze.move_bomberman(1, 0)
                    Maze.print_maze()
                if event.key == ord("a"):
                    Maze.move_bomberman(-1, 0)
                    Maze.print_maze()
                if event.key == ord("s"):
                    Maze.move_bomberman(0, -1)
                    Maze.print_maze()

        draw_board(screen, Maze)
        Bomberman.handle_keys() # handle the keys

        screen.fill((255,255,255)) # fill the screen with white
        Bomberman.draw(screen) # draw the bomberman to the screen
        pygame.display.update() # update the screen

        clock.tick(40)
        
if __name__ == "__main__":
    main()