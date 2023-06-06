import pygame

class Button:
    def __init__(self, text, position, width, height, callback):
        self.text = text
        self.position = position
        self.width = width
        self.height = height
        self.callback = callback
        self.rect = pygame.Rect(self.position, (self.width, self.height))
        self.is_hovered = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.callback()

    def render(self, surface):
        color = (255, 255, 255)
        if self.is_hovered:
            color = (200, 200, 200)
        pygame.draw.rect(surface, color, self.rect)
        font = pygame.font.Font(None, 32)
        text = font.render(self.text, True, (0, 0, 0))
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
