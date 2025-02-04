import pygame
from sys import exit
from graphes import Graphe
from map import *
# Initialize pygame
pygame.init()

font = pygame.font.Font(None,36)

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("RPG Adventure")
map_surface = pygame.image.load('assets/map.png')
map_surface = pygame.transform.scale(map_surface, (800,600))
player_surface = pygame.image.load('assets/player_stand.png')
player_surface = pygame.transform.scale(player_surface,(40,50))
# mappp = Graphe()
# for a,x,y in [("rue",10,10),('forest',150,150)]:
#     mappp.ajouter_sommet(a,x,y)
#     print(b)
# print(mappp.liste_sommets())
# forest_s = pygame.image.load("assets/tavern_bg.png")

while True:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # screen.blit()
    # screen
    # screen.blit(map_surface, (0,0))
    # screen.blit(player_surface, (WIDTH//2,HEIGHT//2))
    screen.fill((255,255,255))
    draw_loc(village,screen)

    pygame.display.update()