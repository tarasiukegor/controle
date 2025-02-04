# src/ui.py
import pygame

class DialogueUI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)

    def render_dialogue(self, dialogue, choices):
        self.screen.fill((0, 0, 0))  # Clear screen
        if dialogue:
            text = self.font.render(dialogue["text"], True, (255, 255, 255))
            self.screen.blit(text, (50, 50))
        for i, choice in enumerate(choices):
            choice_text = self.font.render(f"{i + 1}. {choice['text']}", True, (255, 255, 255))
            self.screen.blit(choice_text, (50, 100 + i * 40))
        pygame.display.flip()