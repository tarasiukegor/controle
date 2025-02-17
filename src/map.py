from graphes import Graphe
import pygame

pygame.init()

font = pygame.font.Font("Controle/assets/fonts/Minecraft.ttf", 20)
WIDTH, HEIGHT = 800, 600

class GameState():
    def __init__(self):
        self.current_location = "Strasbourg Square"
        self.game_state = "Strasbourg Map"
        self.inside_posistion = None
        self.current_npc = None
        self.inventory = []
        self.money = 150

    
    def start_dialogue(self,npc):
        self.current_npc = npc

    def exit_dialogue(self):
        self.current_npc = None


gamestate = GameState()


def create_location(name,sommets_cord, liens, asset):
    graph = Graphe(name,asset)
    
    for sommet, cord in sommets_cord:
        graph.ajouter_sommet(sommet, cord)

    for sommet1, sommet2 in liens:
        graph.ajouter_arete(sommet1, sommet2)

    return graph

def create_inside_location(name,sommets_cord, liens,asset):
    return create_location(name,sommets_cord, liens,asset)


strasbourg = create_location("Strasbourg Map",
    [["Strasbourg Square", (WIDTH // 2, HEIGHT // 2)],
     ["Strasbourg Tavern", (100, 300)],
     ["Strasbourg Forge", (500, 200)],
     ["Strasbourg Marche", (150, 100)]],

    [("Strasbourg Square", "Strasbourg Tavern"),
     ("Strasbourg Square", "Strasbourg Forge"),
     ("Strasbourg Square", "Strasbourg Marche")],
     "Controle/assets/map.png"

)

strasbourg_tavern = create_inside_location("Tavern",
    [["Entrance", (WIDTH // 2, HEIGHT - 100)],
     ["Bar", (WIDTH // 2, HEIGHT // 2)],
     ["Barman", (WIDTH // 4, HEIGHT // 3)],
     ["Ivrogne", (WIDTH - 200, HEIGHT // 3)]],

    [("Entrance", "Bar"),
     ("Bar", "Barman"),
     ("Bar", "Ivrogne")],
    "Controle/assets/tavern_bg.png"
)

strasbourg_forge = create_inside_location("Forge",
    [["Entrance", (WIDTH // 2, HEIGHT - 100)],
     ["Anvil", (WIDTH // 2, HEIGHT // 2)],
     ["Smith", (WIDTH - 200, HEIGHT // 3)]],

    [("Entrance", "Anvil"),
     ("Anvil", "Smith")],
    "Controle/assets/test_pic.jpg"
)

inside_locations = {
    "Strasbourg Tavern": strasbourg_tavern,
    "Strasbourg Forge": strasbourg_forge
}

def draw_loc(location_name, screen, asset):
    surface = pygame.transform.scale(pygame.image.load(asset), (WIDTH, HEIGHT))
    screen.blit(surface, (0, 0))

    for name, coord in location_name._location.items():
        color = "Green" if name == gamestate.current_location else "Blue"
        pygame.draw.circle(screen, color, coord, 20)
        screen.blit(font.render(name, True, "White"), coord)

        for loca in location_name.liste_voisins(name):
            pygame.draw.line(screen, "White", coord, location_name._location[loca])


def draw_inside(location_name, screen, asset):
    surface = pygame.transform.scale(pygame.image.load(asset), (WIDTH, HEIGHT))
    screen.blit(surface, (0, 0))

    for name, coord in location_name._location.items():
        color = "Yellow" if name in ["Ivrogne","Barman"] else "Blue"
        if name == gamestate.inside_posistion:
            color = "Green"
        pygame.draw.circle(screen, color, coord, 20)
        screen.blit(font.render(name, True, "White"), coord)

        for loca in location_name.liste_voisins(name):
            pygame.draw.line(screen, "White", coord, location_name._location[loca])
    pygame.draw.rect(screen, "Red", (20, HEIGHT - 50, 100, 40)) 
    screen.blit(font.render("Exit", True, "White"), (40, HEIGHT - 45))  