# src/location.py
import pygame

class Location:
    def __init__(self, screen, name):
        self.screen = screen
        self.name = name
        self.font = pygame.font.Font(None, 36)
        self.npcs = []  # List of NPCs in this location

    def add_npc(self, npc):
        self.npcs.append(npc)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear screen
        text = self.font.render(f"You are in {self.name}", True, (255, 255, 255))
        self.screen.blit(text, (50, 50))

        for i, npc in enumerate(self.npcs):
            npc_text = self.font.render(f"{i + 1}. Talk to {npc.name}", True, (255, 255, 255))
            self.screen.blit(npc_text, (50, 100 + i * 40))

        exit_text = self.font.render("Press E to exit to main map", True, (255, 255, 255))
        self.screen.blit(exit_text, (50, 400))
        pygame.display.flip()