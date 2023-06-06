import pygame
import config

class GameView:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game

        self.color_circles = [
            {"rect": pygame.Rect((50 + i * 70, 500, 50, 50)), "start_pos": (50 + i * 70, 500)} for i in range(len(config.colors))
        ]

        self.dragging_circle = None
        self.drag_offset = None

    def render_original_positions(self):
        for circle in self.color_circles:
            rect = circle["rect"]
            rect.x, rect.y = circle["start_pos"]
            pygame.draw.ellipse(self.screen, config.colors[self.color_circles.index(circle)], rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for circle in self.color_circles:
                if circle["rect"].collidepoint(event.pos):
                    self.dragging_circle = circle
                    self.drag_offset = event.pos[0] - circle["rect"].x, event.pos[1] - circle["rect"].y
                    break
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if self.dragging_circle is not None:
                row, col = self.get_drop_location(event.pos)
                if row is not None and col is not None:
                    color = config.colors[self.color_circles.index(self.dragging_circle)]
                    self.game.handle_drop_event(row, col, color)  # Aufruf der Methode in game.py
                self.dragging_circle = None
                self.drag_offset = None

    def update(self):
        if self.dragging_circle is not None:
            self.dragging_circle["rect"].x, self.dragging_circle["rect"].y = pygame.mouse.get_pos()[0] - self.drag_offset[0], pygame.mouse.get_pos()[1] - self.drag_offset[1]

    def render(self):
        self.screen.fill((0, 0, 0))

        # Render Mastermind Board
        board_width = config.board_columns * (config.circle_size + config.circle_spacing)
        board_height = config.board_rows * (config.circle_size + config.circle_spacing)
        board_start_x = (self.screen.get_width() - board_width - config.feedback_area_width - config.margin * 2) // 2
        board_start_y = (self.screen.get_height() - board_height) // 2

        for row in range(config.board_rows):
            for col in range(config.board_columns):
                circle_x = board_start_x + col * (config.circle_size + config.circle_spacing)
                circle_y = board_start_y + row * (config.circle_size + config.circle_spacing)
                pygame.draw.circle(self.screen, (128, 128, 128), (circle_x, circle_y), config.circle_size // 2)

        # Render Feedback Rows
        feedback_start_x = board_start_x + board_width + config.margin
        feedback_start_y = board_start_y
        feedback_row_height = config.circle_size // 2

        for row in range(config.board_rows):
            feedback_row_y = feedback_start_y + row * (feedback_row_height + config.circle_spacing)
            for col in range(config.board_columns):
                feedback_circle_x = feedback_start_x + col * (feedback_row_height + config.circle_spacing)
                feedback_circle_y = feedback_row_y + feedback_row_height // 2
                pygame.draw.circle(self.screen, (128, 128, 128), (feedback_circle_x, feedback_circle_y), feedback_row_height // 2)

        # Render Menu Button
        menu_button_rect = pygame.Rect(config.margin, config.margin, 100, 50)
        pygame.draw.rect(self.screen, (255, 0, 0), menu_button_rect)
        font = pygame.font.Font(None, 24)
        text = font.render("Menu", True, (255, 255, 255))
        text_rect = text.get_rect(center=menu_button_rect.center)
        self.screen.blit(text, text_rect)

        # Render Color Circles
        for circle in self.color_circles:
            rect = circle["rect"]
            if circle is self.dragging_circle:
                rect.x, rect.y = pygame.mouse.get_pos()[0] - self.drag_offset[0], pygame.mouse.get_pos()[1] - \
                                 self.drag_offset[1]
            else:
                rect.x, rect.y = circle["start_pos"]
            pygame.draw.ellipse(self.screen, config.colors[self.color_circles.index(circle)], rect)

    def get_drop_location(self, pos):
        board_start_x = (self.screen.get_width() - config.board_columns * (config.circle_size + config.circle_spacing)) // 2
        board_start_y = (self.screen.get_height() - config.board_rows * (config.circle_size + config.circle_spacing)) // 2

        row = (pos[1] - board_start_y) // (config.circle_size + config.circle_spacing)
        col = (pos[0] - board_start_x) // (config.circle_size + config.circle_spacing)

        if 0 <= row < config.board_rows and 0 <= col < config.board_columns:
            return row, col
        else:
            return None, None
