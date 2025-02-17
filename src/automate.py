from graphes import *


class automate:
    def __init__(self,graphe,depart): # graphe pondéré, sommet entrant
        self._data = graphe
        self._entrant = depart
        self._oujesuis = depart

    def restart(self):
        self._oujesuis = self._entrant

    def transition(self,valeur):
        for v in self._data.liste_voisins(self._oujesuis):
            if valeur in self._data.poids(self._oujesuis,v):
                print(f"{v}")
                self._oujesuis = v
                return
        raise(TransitionInvalide('pas de transition trouvée pour cette valeur'))

    def liste_transition(self):
        return [ x for v in self._data.liste_voisins(self._oujesuis)
                 for x in self._data.poids(self._oujesuis,v) ]

class TransitionInvalide(Exception):
    pass


