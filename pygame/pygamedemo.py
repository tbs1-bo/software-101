import sys
import pygame

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("ball.gif")
        self.rect = self.image.get_rect()
        self.speedx = 2  # speed in x and y direction
        self.speedy = 2
        self.screen_width = pygame.display.get_surface().get_width()
        self.screen_height = pygame.display.get_surface().get_height()

    def update(self):
        """Update called by the update of the Group method."""
        self.rect = self.rect.move((self.speedx, self.speedy))  # move in direction

        # bounce from wall if necessary
        if self.rect.left < 0 or self.rect.right > self.screen_width:
            self.bounce(xdir=True, ydir=False)
        if self.rect.top < 0 or self.rect.bottom > self.screen_height:
            self.bounce(xdir=False, ydir=True)

    def is_clicked(self):
        """Check whether this Ball has been clicked."""
        x,y = pygame.mouse.get_pos()
        return self.rect.collidepoint(x, y)

    def bounce(self, xdir=True, ydir=False):
        """Bounce the ball in x- and/or y-direction."""
        if xdir:
            self.speedx *= -1
        if ydir:
            self.speedy *= -1


class FizzBuzzGame:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.sprites = pygame.sprite.GroupSingle(Ball())

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.sprites.sprite.is_clicked():
                self.sprites.sprite.bounce()

    def start_game_loop(self):
        clock = pygame.time.Clock()

        while True:
            # handle events
            for event in pygame.event.get():
                self.handle_event(event)

            self.sprites.update()  # update all Sprites

            self.screen.fill((0,0,0))  # black background
            self.sprites.draw(self.screen)  # draw sprites on screen

            # flip the buffer
            pygame.display.flip()
            clock.tick(60)  # limit runtime to 60 Frames/Second


if __name__ == "__main__":
    game = FizzBuzzGame(width=320, height=240)
    game.start_game_loop()
