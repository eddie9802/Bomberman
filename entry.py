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
GREEN = (152, 139, 152)
YELLOW = (255, 255, 0)

# Sets the height and width of each grid location
WIDTH = 90
HEIGHT = 90

# Margin between each cell
MARGIN = 1

def draw_board(screen, m):
    screen.fill(BLACK)
    for j in range(m.MAZE_SIZE -1 , -1, -1):
        for i in range(m.MAZE_SIZE):
            color = WHITE
            if isinstance(m.maze[i][j], wall) and not m.maze[i][j].is_destructable :
                color = BLACK
            elif isinstance(m.maze[i][j], wall) and m.maze[i][j].is_destructable and not m.maze[i][j].is_destroyed:
                color = GREY
            elif isinstance(m.maze[i][j], wall) and m.maze[i][j].has_bomberman:
                color = RED
            elif isinstance(m.maze[i][j], wall) and not m.maze[i][j].has_bomberman and m.maze[i][j].has_bomb:
                color = YELLOW
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * i + MARGIN,
                              (MARGIN + HEIGHT) * j + MARGIN,
                              WIDTH,
                              HEIGHT])
                        
def bomb_timeout(all_bombs, m):
    for bomb in all_bombs:
        seconds=(pygame.time.get_ticks()-bomb[0].start_timer)/1000
        if seconds > 3:
            all_bombs.remove(bomb)
            m.maze[bomb[1]][bomb[2]].has_bomb = False

def main():
    
    # Game setup
    b = bomberman(0, 0)
    m = maze(b)
    m.build()

    # Graphics setup
    pygame.init()
    pygame.display.set_caption('Bomberman')
    screen = pygame.display.set_mode([1001, 1001])
    #bg = pygame.transform.scale(pygame.image.load("bg.png"), (1200, 800))
    clock = pygame.time.Clock() # Manages how fast the screen updates
    #screen.blit(bg, (0, 0))

    playing = True
    all_bombs = []
    while playing:  
        bomb_timeout(all_bombs, m)      
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == ord("w"):
                    m.move_bomberman(0, -1)
                if event.key == ord("d"):
                    m.move_bomberman(1, 0)   
                if event.key == ord("a"):
                    m.move_bomberman(-1, 0)
                if event.key == ord("s"):
                    m.move_bomberman(0, 1)
                if event.key == ord(" "):
                    m.maze[b.x_pos][b.y_pos].has_bomb = True
                    m.maze[b.x_pos][b.y_pos].start_timer = pygame.time.get_ticks()
                    all_bombs.append((m.maze[b.x_pos][b.y_pos], b.x_pos, b.y_pos))
        draw_board(screen, m)      
        pygame.display.flip()
        
if __name__ == "__main__":
    main()