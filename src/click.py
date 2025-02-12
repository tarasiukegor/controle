# import pygame

# class Button:
#     def __init__(self, x, y, width, height, text, font, color):
#         self.rect = pygame.Rect(x, y, width, height)
#         self.text = text
#         self.font = font
#         self.color = color

#     def draw(self, screen):
#         pygame.draw.rect(screen, self.color, self.rect)
#         text_surface = self.font.render(self.text, True, (0, 0, 0))
#         screen.blit(text_surface, (self.rect.x + 10, self.rect.y + 10))

#     def is_clicked(self, pos):
#         return self.rect.collidepoint(pos)

import pygame
from map import gamestate
pygame.init()

def handle_click(pos,location_map):
    # global current_location,game_state
    
    for location, cord in location_map._location.items():
        distance = ((pos[0]-cord[0])**2 + (pos[1]-cord[1])**2) ** 0.5
        
        if distance < 30 and location == gamestate.current_location: 
            gamestate.game_state = "inside"
            print (f'Inside {location}')
            print (gamestate.game_state)
            return
        if distance < 30 and location in location_map.liste_voisins(gamestate.current_location): 
            gamestate.current_location = location
            print (f'changes location to {location}')
            print (gamestate.current_location)
            return
        

        