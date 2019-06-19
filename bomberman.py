import pygame

class bomberman():

    def __init__(self, x_pos, y_pos):
        self.image = pygame.image.load("SBred.png")
        self.x_pos = x_pos
        self.y_pos = y_pos

    def handle_keys(self):
        """ Handles Keys """
        key = pygame.key.get_pressed()
        DIST = 5 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            self.y_pos += DIST # move down
        elif key[pygame.K_UP]: # up key
            self.y_pos -= DIST # move up
        if key[pygame.K_RIGHT]: # right key
            self.x_pos += DIST # move right
        elif key[pygame.K_LEFT]: # left key
            self.x_pos -= DIST # move left

    def draw(self, surface):
        # blit bomberman at the current position
        surface.blit(self.image, (self.x_pos, self.y_pos))

    # def setup_graphics():
