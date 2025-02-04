# src/main.py
import pygame
from map import MainMap
from location import Location
from npc import NPC
from ui import DialogueUI
from graphes import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    clock = pygame.time.Clock()
    ui = DialogueUI(screen)
    main_map = MainMap(screen)

    # Define locations
    tavern = Location(screen, "Tavern")
    city_hall = Location(screen, "City Hall")
    forest = Location(screen, "Forest")
    market = Location(screen, "Market")

    mapm = Graphe()
    
    # Add NPCs to locations
    bartender = NPC("Bartender")
    bartender.add_dialogue(1, "Welcome to the tavern!", character="Bartender")
    bartender.add_dialogue(2, "What can I get you?", character="Bartender")
    bartender.add_choice(1, 2, "What's on the menu?")
    tavern.add_npc(bartender)

    mayor = NPC("Mayor")
    mayor.add_dialogue(1, "Welcome to City Hall!", character="Mayor")
    mayor.add_dialogue(2, "How can I help you?", character="Mayor")
    mayor.add_choice(1, 2, "What's new in the city?")
    city_hall.add_npc(mayor)

    # Game state
    current_location = None
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not current_location:
                    clicked_location = main_map.get_clicked_location(event.pos)
                    if clicked_location:
                        if clicked_location == "Tavern":
                            current_location = tavern
                        elif clicked_location == "City Hall":
                            current_location = city_hall
                        elif clicked_location == "Forest":
                            current_location = forest
                        elif clicked_location == "Market":
                            current_location = market
            elif event.type == pygame.KEYDOWN:
                if current_location:
                    if event.key == pygame.K_e:  # Exit to main map
                        current_location = None
                    elif event.key == pygame.K_1:  # Talk to NPC 1
                        if current_location.npcs:
                            current_location.npcs[0].start_dialogue(1)

        if current_location:
            current_location.draw()
        else:
            main_map.draw()

        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()