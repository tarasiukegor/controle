import pygame
import textwrap
from sys import exit
from map import gamestate, draw_loc, WIDTH,HEIGHT, strasbourg,inside_locations,draw_inside, font
from click import handle_click, handle_inside_click 
from dialogue import *
from intro import *

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Controle")


run_intro(screen)

while True:
    screen.fill('black')
    if gamestate.game_state == "Inside" and gamestate.current_location in inside_locations:
        draw_inside(inside_locations[gamestate.current_location], screen, inside_locations[gamestate.current_location]._asset)
    
    if gamestate.game_state == "Strasbourg Map":
        draw_loc(strasbourg, screen, "Controle/assets/map.png")

    if gamestate.current_npc:

        background_npc = pygame.Surface((WIDTH,HEIGHT))  
        background_npc.set_alpha(200)           # set alpha pour changer le "opacity" de couleur
        background_npc.fill("Black")              
        screen.blit(background_npc, (0,0)) 
        
        automate_npc = dialogue_systems[gamestate.current_npc]
        wrapped_text = textwrap.wrap(automate_npc._oujesuis, width=55)
        y_offset = 20  # y pour placer des phrases         
        for line in wrapped_text:
            text_surface = font.render(line, True, "white")
            screen.blit(text_surface, (30, y_offset))
            y_offset += 30  # augemente y
        
        choices = automate_npc.liste_transition()
        choice_buttons = []
        
        for i, choice in enumerate(choices):
            button_x, button_y = 70, 300 + i * 40
            button_width, button_height = 600, 30

            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            pygame.draw.rect(screen, "bisque4", button_rect)

            text_surface = font.render(choice, True, "White")
            text_rect = text_surface.get_rect(center=button_rect.center) 
            screen.blit(text_surface, text_rect.topleft)

            choice_buttons.append((button_rect, choice))
        
        exit_button_rect = pygame.Rect(680, 560, 120, 40)
        exit_text = font.render("Exit", True, "White")
        text_rect = exit_text.get_rect(center=exit_button_rect.center)
        if not automate_npc.liste_transition():

            pygame.draw.rect(screen, (0,0,0,100), exit_button_rect)
            screen.blit(exit_text, text_rect)



    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if gamestate.current_npc:
                npc_dialogue = dialogue_systems[gamestate.current_npc]
                for button_rect, choice in choice_buttons:
                    if button_rect.collidepoint(event.pos):
                        npc_dialogue.transition(choice)
                        break  
                
                if exit_button_rect.collidepoint(event.pos):
                    gamestate.current_npc = None 
            else:
                if gamestate.game_state == "Strasbourg Map":
                    handle_click(event.pos, strasbourg)
                elif gamestate.game_state == "Inside":
                        
                    handle_inside_click(event.pos, inside_locations[gamestate.current_location])

    

    pygame.display.update()
    