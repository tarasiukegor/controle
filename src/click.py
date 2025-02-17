import pygame
from map import gamestate,inside_locations, HEIGHT,WIDTH
from dialogue import *

pygame.init()

def handle_click(pos,location_map):
    for location, cord in location_map._location.items():
        distance = ((pos[0] - cord[0]) ** 2 + (pos[1] - cord[1]) ** 2) ** 0.5

        if distance < 30 and location == gamestate.current_location:
            if location in inside_locations:
                gamestate.game_state = "Inside"
                gamestate.inside_posistion = inside_locations["Strasbourg Tavern"].liste_sommets()[0]
                print(f'entrant {location}')
            return
        
        if distance < 30 and location in location_map.liste_voisins(gamestate.current_location):
            gamestate.current_location = location
            print(f'changer la location a {location}')
            return
        
def handle_inside_click(pos, inside_map):
    for spot, cord in inside_map._location.items():
        distance = ((pos[0] - cord[0]) ** 2 + (pos[1] - cord[1]) ** 2) ** 0.5
        if distance < 30 and spot in inside_map.liste_voisins(gamestate.inside_posistion):
            gamestate.inside_posistion = spot
            print(f'se deplace a {spot}')
            return
        if distance < 30 and spot == gamestate.inside_posistion:
            if spot in dialogue_systems:
                gamestate.start_dialogue(spot)
                dialogue_systems[spot].restart()
                print(f'commence dialogue avec: {spot}')
                return

    exit_button_rect = pygame.Rect(20, HEIGHT - 50, 100, 40)
    
    if exit_button_rect.collidepoint(pos):
        gamestate.game_state = "Strasbourg Map"
        gamestate.inside_posistion = None
        gamestate.exit_dialogue()
        print("quittant a la carte")
