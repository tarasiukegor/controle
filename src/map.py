from graphes import Graphe
import pygame

pygame.init()

font = pygame.font.Font("Controle/assets/fonts/PublicPixel.ttf", 14)
WIDTH, HEIGHT = 800, 600

class GameState():
    def __init__(self):
        self.current_location = None
        self.prevoius_location = []
        self.game_state = None
        self.inside_position = None
        self.current_npc = None
        self.inventory = []
        self.money = 150
        self.quests = {}
        self.reputation = 0
        
        
    
        
    def add_quest(self, quest):
        self.quests[quest.name] = quest

    def start_dialogue(self,npc):
        self.current_npc = npc

    def exit_dialogue(self):
        self.current_npc = None

    def enter_inside_location(self,new_location):
        self.prevoius_location.append((self.current_location, self.inside_position))
        print(self.prevoius_location)

        self.current_location = new_location
        self.game_state = "Inside"
        
        self.inside_position = inside_locations[new_location].liste_sommets()[0]
        # print(vars(gamestate))
    
    def exit_inside_location(self):
        if self.prevoius_location:
            self.current_location, self.inside_position= self.prevoius_location.pop()
            # print(vars(gamestate))
        else:
            self.inside_position = None
            self.game_state = "Strasbourg Map"  
            # print(vars(gamestate))
                


gamestate = GameState()


def create_location(name,sommets_cord, liens, asset):
    graph = Graphe(name,asset)
    
    for sommet, cord in sommets_cord:
        graph.ajouter_sommet(sommet, cord)

    for sommet1, sommet2 in liens:
        graph.ajouter_arete(sommet1, sommet2)

    return graph


strasbourg = create_location(
    "Strasbourg Map",
    [
        ["Strasbourg Square", (WIDTH // 2, HEIGHT // 2)],
        ["Strasbourg Mairie", (550, 280)]
    ],
                            
    [
        ("Strasbourg Square", "Strasbourg Mairie")
    ],
    "Controle/assets/map.png")

strasbourg_mairie = create_location(
    "Mairie",
    [
        ["Entrance",(WIDTH // 2, HEIGHT - 100)],
        ["Office", (WIDTH // 2, HEIGHT // 2)],
    ],
    [
        ("Entrance","Office"),
    ],
    "Controle/assets/town_hall.jpg")

office = create_location(
    "Office",
    [
        ["Entrance",(WIDTH // 2, HEIGHT - 100)],
        ["Maire", (WIDTH // 2, HEIGHT // 3)]
    ],
    [
        ("Entrance","Maire"),
    ],
    "Controle/assets/maire.jpg")




tavern_bar = create_location(
    "Table Taverne",
    [
        ["Retour au Taverne", (WIDTH // 2, HEIGHT - 100)],
        ["Barman", (WIDTH//2, HEIGHT // 2)],
        ["Ivrogne", (600, 300)]
        
    ],
    [
        ("Retour au Taverne", "Barman"),
        ("Retour au Taverne","Ivrogne")
    ],
    "Controle/assets/tavern_bg.png"
)

strasbourg_tavern = create_location("Tavern",
    [["Entrance", (WIDTH // 2, HEIGHT - 100)],
     ["Bar Taverne", (WIDTH // 2, HEIGHT // 2)],
    ],

    [("Entrance", "Bar Taverne"),],
    "Controle/assets/tavern_bg.png"
)


inside_locations = {
    "Strasbourg Mairie": strasbourg_mairie,
    "Office": office,
    "Strasbourg Tavern" : strasbourg_tavern,
    "Bar Taverne": tavern_bar,


}



# strasbourg_forge = create_location("Forge",
#     [["Entrance", (WIDTH // 2, HEIGHT - 100)],
#      ["Anvil", (WIDTH // 2, HEIGHT // 2)],
#      ["Smith", (WIDTH - 200, HEIGHT // 3)]],

#     [("Entrance", "Anvil"),
#      ("Anvil", "Smith")],
#     "Controle/assets/test_pic.jpg"
# )


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
        if name == gamestate.inside_position:
            color = "Green"
        pygame.draw.circle(screen, color, coord, 20)
        screen.blit(font.render(name, True, "White"), coord)

        for loca in location_name.liste_voisins(name):
            pygame.draw.line(screen, "White", coord, location_name._location[loca])

