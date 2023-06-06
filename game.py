import pygame
import sys
from menu_view import MenuView
from game_view import GameView

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.is_running = False
        self.current_view = None

        # Fenstergröße festlegen
        self.window_width = 800
        self.window_height = 600

    def start(self):
        self.is_running = True
        self.current_view = MenuView(self.screen, self)

        while self.is_running:
            self.clock.tick(60)
            self.handle_events()
            self.update()
            self.render()

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False
            else:
                self.current_view.handle_event(event)

    def update(self):
        self.current_view.update()

    def render(self):
        self.screen.fill((0, 0, 0))

        self.current_view.render()

        pygame.display.flip()

    def handle_drop_event(self, row, col, color):
        print(f"Drop Event: Row={row}, Column={col}, Color={color}")

    def show_options(self):
        print("Show Options")

    def quit_game(self):
        pygame.quit()
        sys.exit()

game = Game()
game.start()
