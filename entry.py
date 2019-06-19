import pygame
from bomberman import bomberman
from wall import wall
from maze import maze

# pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(30, 30, 60, 60))
# Defines colous of blocks within game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
RED = (255, 0, 0)

# Sets the height and width of each grid location
WIDTH = 20
HEIGHT = 20

# Margin between each cell
MARGIN = 5

def main():
    
    # Game setup
    b = bomberman(0, 0)
    m = maze(b)
    m.build()

    # Graphics setup
    pygame.init()
    pygame.display.set_caption('Bomberman')
    screen = pygame.display.set_mode([1200, 800])
    bg = pygame.transform.scale(pygame.image.load("bg.png"), (1200, 800))
    clock = pygame.time.Clock() # Manages how fast the screen updates
    screen.blit(bg, (0, 0))

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == ord("w"):
                    m.move_bomberman(0, 1)
                    m.print_maze()
                if event.key == ord("d"):
                    m.move_bomberman(1, 0)
                    m.print_maze()
                if event.key == ord("a"):
                    m.move_bomberman(-1, 0)
                    m.print_maze()
                if event.key == ord("s"):
                    m.move_bomberman(0, -1)
                    m.print_maze()
                
        pygame.display.flip()
        
if __name__ == "__main__":
    main()