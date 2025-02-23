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
                gamestate.inside_position = inside_locations[location].liste_sommets()[0]
                # print(vars(gamestate))
                print(f'entrant {location}')
            return
        
        if distance < 30 and location in location_map.liste_voisins(gamestate.current_location):
            gamestate.current_location = location
            # print(vars(gamestate))
            print(f'changer la location a {location}')
            return
        
def handle_inside_click(pos, inside_map):
    for spot, cord in inside_map._location.items():
        distance = ((pos[0] - cord[0]) ** 2 + (pos[1] - cord[1]) ** 2) ** 0.5
        
        if distance < 30 and spot in inside_map.liste_voisins(gamestate.inside_position):
            gamestate.inside_position = spot
            print(f'se deplace a {spot}')
            # print(vars(gamestate))
            return
        
        if distance < 30 and spot == gamestate.inside_position:
            if spot in inside_locations:
                gamestate.enter_inside_location(spot)
                print(f'entering into {spot}')
                # print(vars(gamestate))
                return
            
            if spot in dialogue_systems:
                gamestate.start_dialogue(spot)
                dialogue_systems[spot].restart()
                print(f'commence dialogue avec: {spot}')
                print(dialogue_systems[gamestate.current_npc]._oujesuis)
                return
            
        if distance < 30 and spot == inside_map.liste_sommets()[0]:
            gamestate.exit_inside_location()
            gamestate.exit_dialogue()
            print("quittant")



        
