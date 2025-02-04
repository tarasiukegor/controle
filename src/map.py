from graphes import Graphe
import pygame
# from main import screen
pygame.init()
width,heigth = 800,200
font = pygame.font.Font(None,20)
def create_location(name,sommets_cord,liens):
    name = Graphe()
    for sommet,cord in sommets_cord:
        name.ajouter_sommet(sommet,cord) 
    for sommet1,sommet2 in liens:
        name.ajouter_arete(sommet1,sommet2)
    return name


village = create_location('village',
                        [['Rue', (width//2,heigth//2)],["Auberge",(100,300)],['Forge', (500,200)],["Marche",(150,100)]], 
                        [('Rue','Auberge'),('Rue','Forge'),('Rue','Marche')])


# ["Auberge",(100,100)],['Forge', (500),(200)],["Marche",(150,100)]

# ('Rue','Forge'),('Rue','Marche')

def draw_loc(location_name,screen):
    for i in village._location:
        screen.blit(font.render(i,True,(0,0,0)),location_name._location[i])
        for loca in village.liste_voisins(i):

            pygame.draw.line(screen,(0,0,0),location_name._location[i],location_name._location[loca])

for i in village._location:
    print(village._location[i])



print(village)
print(village.liste_sommets()) 
print(village._data)
print(village._location)   
