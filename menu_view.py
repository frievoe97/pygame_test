import pygame
from button import Button

class MenuView:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.buttons = [
            Button("Start Game", (300, 250), 200, 50, self.start_game),
            Button("Options", (300, 320), 200, 50, self.game.show_options),
            Button("Quit", (300, 390), 200, 50, self.game.quit_game)
        ]

    def handle_event(self, event):
        for button in self.buttons:
            button.handle_event(event)

    def update(self):
        pass

    def render(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.Font(None, 48)
        welcome_text = font.render("Welcome to My Game", True, (255, 255, 255))
        text_rect = welcome_text.get_rect(center=(self.screen.get_width() // 2, 150))
        self.screen.blit(welcome_text, text_rect)

        for button in self.buttons:
            button.render(self.screen)

    def start_game(self):
        from game_view import GameView  # Hier importieren wir GameView lokal
        self.game.current_view = GameView(self.screen, self.game)

