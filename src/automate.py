from graphes import *
from map import *

class automate:
    def __init__(self,graphe,depart,gamestate): # graphe pondéré, sommet entrant
        self._data = graphe
        self._entrant = depart
        self._oujesuis = depart
        self.gamestate = gamestate

    def restart(self):
        self._oujesuis = self._entrant

    def transition(self,valeur):
        
        for v in self._data.liste_voisins(self._oujesuis):
            if valeur in self._data.poids(self._oujesuis,v):
                print(f"{v}")
                commands = self._data._commands.get((self._oujesuis, v), [])
                for command, args in commands:
                    command(*args)
                    
                self._oujesuis = v
                return
        raise(TransitionInvalide('pas de transition trouvée pour cette valeur'))

    def liste_transition(self):
        return [ x for v in self._data.liste_voisins(self._oujesuis)
                 for x in self._data.poids(self._oujesuis,v) ]
    

class TransitionInvalide(Exception):
    pass

def exit_chaffeur():
        gamestate.current_npc = None
        gamestate.current_location = "Strasbourg Square"
        gamestate.game_state = "Strasbourg Map"


def remove_from_inventory(item):
    gamestate.inventory.remove(item)
    print(f"succesfully removed {item}")

def reputation_status(number): 
    gamestate.reputation += number
    print(f"up rep by {number}, current rep: {gamestate.reputation}")

def map_update(name, sommets, liens):
    for sommet, cord in sommets:
        name.ajouter_sommet(sommet, cord)

    for sommet1, sommet2 in liens:
        name.ajouter_arete(sommet1, sommet2)

def create_inside_location(name_var,name,sommets_cord, liens, asset):
    name_var = Graphe(name,asset)
    for sommet, cord in sommets_cord:
        name_var.ajouter_sommet(sommet, cord)

    for sommet1, sommet2 in liens:
        name_var.ajouter_arete(sommet1, sommet2)

    inside_locations[name] = name_var
    print(inside_locations)

def acheter(item_cost):
    gamestate.money -= item_cost

def change_smmt(npc, target):
    npc._entrant = target
    npc.restart()
    



