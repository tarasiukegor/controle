from graphes import Graphe
import pygame
# from main import screen
pygame.init()
width,heigth = 800,600
font = pygame.font.Font(None,20)


class GameState():
    def __init__(self):
        self.current_location = "Rue"
        self.game_state = "Village"

    
gamestate = GameState()

def create_location(name,sommets_cord,liens):
    name = Graphe()
    for sommet,cord in sommets_cord:
        name.ajouter_sommet(sommet,cord) 
    for sommet1,sommet2 in liens:
        name.ajouter_arete(sommet1,sommet2)
    return name


village = create_location('Village',
                        [['Rue', (width//2,heigth//2)],
                        ["auberge strasbourg",(100,300)],
                        ['Forge', (500,200)],
                        ["Marche",(150,100)]],

                        [('Rue','auberge strasbourg'),
                        ('Rue','Forge'),
                        ('Rue','Marche')]
                        )


# ["Auberge",(100,100)],['Forge', (500),(200)],["Marche",(150,100)]

# ('Rue','Forge'),('Rue','Marche')

def draw_loc(location_name,screen,asset):
    surf = pygame.image.load(asset)
    surf = pygame.transform.scale(surf, (width,heigth))
    screen.blit(surf, (0,0))
    for name, coord in village._location.items():
        color = (0,255,0) if name == gamestate.current_location else (0,0,255)
     
        pygame.draw.circle(screen,color, coord,20)
        screen.blit(font.render(name,True,(255,255,255)),coord)

        for loca in village.liste_voisins(name):

            pygame.draw.line(screen,(255,255,255),coord,location_name._location[loca])



# print(f"liste des sommets: {village.liste_sommets()}") 
# print(f'des arrets: {village._data}')
# print(f"des coords: {village._location}")   
