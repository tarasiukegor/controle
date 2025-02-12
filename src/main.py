import pygame
from sys import exit
from graphes import Graphe
from map import gamestate, village, draw_loc
from click import handle_click
# Initialize pygame
pygame.init()

font = pygame.font.Font(None,36)

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Adventure")
# map_surface = pygame.image.load('assets/map.png')
# map_surface = pygame.transform.scale(map_surface, (800,600))
# player_surface = pygame.image.load('controle/assets/player_stand.png')
# player_surface = pygame.transform.scale(player_surface,(40,50))

print("popa")

while True:


    screen.fill(('White'))

    
    
    
    draw_loc(village,screen,"controle/assets/map.png")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if gamestate.game_state == "Village":
                handle_click(event.pos,village)
                
            elif gamestate.game_state == "inside":
                print(f'you are inside of {gamestate.current_location}')

    
    pygame.display.update() 
    









