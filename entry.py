import pygame
from bomberman import bomberman
from wall import wall
from maze import maze

# pygame.draw.rect(screen, (0, 200, 0), pygame.Rect(30, 30, 60, 60))

BLACK = (0, 0, 0)

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
    screen.blit(bg, (0, 0))

    playing = True

    while playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playing = False
            pressed = pygame.key.get_pressed()
            """ if pressed[pygame.K_UP]:
                if pressed[pygame.K_DOWN]: 
                if pressed[pygame.K_LEFT]: 
                if pressed[pygame.K_RIGHT]: """
        pygame.display.flip()
        
if __name__ == "__main__":
    main()