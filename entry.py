import pygame
from bomberman import bomberman
from wall import wall
from maze import maze

BLACK = (0, 0, 0)

MARGIN = 5

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

    pygame.Start()

    screen = pygame.display.set_mode([1200, 800])
    clock = pygame.time.Clock()

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                playing = False
                
        Bomberman.handle_keys() # handle the keys

        screen.fill((255,255,255)) # fill the screen with white
        Bomberman.draw(screen) # draw the bomberman to the screen
        pygame.display.update() # update the screen

        clock.tick(40)
        
if __name__ == "__main__":
    main()