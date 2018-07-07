import sys

# Pygame installieren: pip install pygame
import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ball.gif")
        self.rect = self.image.get_rect()
        self.speed = [2, 2]  # speed in x and y direction
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()

    def update(self):
        """Update called by the update of the Group method."""
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.speed[1] = -self.speed[1]

    def is_clicked(self):
        """Check whether this Ball has been clicked."""
        x,y = pygame.mouse.get_pos()
        return self.rect.collidepoint(x, y)

    def bounce(self):
        self.speed[0] *= -1


class FizzBuzzGame:
    def __init__(self, width, height):
        pygame.init()

        self.width, self.height = width, height
        self.screen = pygame.display.set_mode((width, height))
        self.sprites = pygame.sprite.GroupSingle(Ball())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN and \
                self.sprites.sprite.is_clicked():

            self.sprites.sprite.bounce()

    def start_game_loop(self):
        clock = pygame.time.Clock()

        while True:
            clock.tick(60)  # limit runtime to 60 Frames/Second

            # handle events
            for event in pygame.event.get():
                self.handle_event(event)

            # update all Sprites
            self.sprites.update()

            # draw the screen: background, sprites, text
            self.screen.fill((0,0,0))
            # for each sprite in the group draw/blit the image into a rect
            self.sprites.draw(self.screen)
            # flip the buffer
            pygame.display.flip()


if __name__ == "__main__":
    game = FizzBuzzGame(320, 240)
    game.start_game_loop()
