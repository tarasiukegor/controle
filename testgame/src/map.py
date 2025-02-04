# src/map.py
import pygame

class MainMap:
    def __init__(self, screen):
        self.screen = screen
        self.locations = {
            "Tavern": pygame.Rect(100, 100, 200, 100),
            "City Hall": pygame.Rect(400, 100, 200, 100),
            "Forest": pygame.Rect(100, 300, 200, 100),
            "Market": pygame.Rect(400, 300, 200, 100),
        }
        self.font = pygame.font.Font(None, 36)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        for name, rect in self.locations.items():
            pygame.draw.rect(self.screen, (0, 128, 255), rect)  # Draw location rectangles
            text = self.font.render(name, True, (255, 255, 255))
            self.screen.blit(text, (rect.x + 10, rect.y + 10))
        pygame.display.flip()

    def get_clicked_location(self, mouse_pos):
        for name, rect in self.locations.items():
            if rect.collidepoint(mouse_pos):
                return name
        return None