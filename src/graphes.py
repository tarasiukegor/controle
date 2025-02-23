class Graphe:
    def __init__(self, name, asset):
        self._name = name
        self._data = dict()
        self._location = dict()
        self._asset = asset
        
    def ajouter_sommet(self,sommet,cord): # (x,y)
        if sommet in self._data:
            raise(SommetError("sommet déjà présent"))            
        self._data[sommet] = []
        self._location[sommet] = cord

    
    def supprimer_sommet(self,sommet,f=False):
        if sommet not in self._data:
            raise(SommetError("sommet n'existe pas"))
        if f:
            for p in self.liste_predecesseurs(sommet):
                self.supprimer_arc(p,sommet)
            del self._data[sommet]
        else:
            if len(self.liste_predecesseurs(sommet)) != 0 or len(self._data[sommet]) != 0:
                raise(ArcError("il y a encore des arcs !"))
            del self._data[sommet]                

    def ajouter_arc(self,A,B):
        if A not in self._data or A not in self._data:
            raise(SommetError("sommet absent"))
        if B in self._data[A]:
            raise(ArcError("arc déjà présent"))
        self._data[A].append(B)

    def supprimer_arc(self,A,B):
        if A not in self._data or B not in self._data:
            raise(SommetError("sommet n'existe pas"))
        for i in range(len(self._data[A])):
            if self._data[A][i] == B:
                del self._data[A][i]
                return
        raise(ArcError("arc n'existait déjà pas"))

    def ajouter_arete(self,A,B):
        self.ajouter_arc(A,B)
        self.ajouter_arc(B,A)

    def supprimer_arete(self,A,B):
        self.supprimer_arc(A,B)
        self.supprimer_arc(B,A)

    def liste_sommets(self):
        return list(self._data.keys())

    def liste_voisins(self,sommet):
        return self._data[sommet].copy()

    def liste_predecesseurs(self,sommet):
        L = []
        for s in self._data.keys():
            for v in self._data[s]:
                if v == sommet:
                    L.append(s)
        return L

class SommetError(Exception):
    pass

class ArcError(Exception):
    pass


    
class GraphePondere:
    def __init__(self):
        self._sommets = [] # indice : numéro, valeur : nomsommet
        self._numero = dict() # clé : nomsommet , valeur : numéro
        self._mat = [[]]
        self._commands ={}

    def ajouter_sommet(self,sommet):
        if sommet in self._numero:
            raise(SommetError("sommet déjà présent"))
        n = len(self._sommets)
        self._numero[sommet] = n
        self._sommets.append(sommet)
        for ligne in self._mat:
            ligne.append(None)
        self._mat.append( [ None for i in range(n+1) ] )

    def ajouter_arc(self,A,B,e, commands=None):
        try:
            nA = self._numero[A]
            nB = self._numero[B]
        except KeyError:
            raise(SommetError("Sommet non trouvé"))
        
        self._mat[nA][nB] = e
        
        # self._commands[(A, B)] = commands if commands else []
    
        self._commands[(A, B)] = [] # on definit la liste des commands

        if commands: # si il ya des commands
            if not isinstance(commands, list):  
                raise ValueError("ca doit etre un liste") # errreur si c'est pas une liste 
        
            for command in commands: 
                if isinstance(command, tuple) and callable(command[0]):  
                    self._commands[(A, B)].append(command) 
                elif callable(command):  
                    self._commands[(A, B)].append((command, ())) 
                else:
                    raise ValueError("invalid fomat")



    def ajouter_arete(self,A,B,e = None):
        self.ajouter_arc(A,B,e)
        self.ajouter_arc(B,A,e)

    def supprimer_arc(self, A, B):
        try:
            nA = self._numero[A]
            nB = self._numero[B]
        except KeyError:
            raise SommetError("Sommet non trouvé")
        self._mat[nA][nB] = None

    def supprimer_sommet(self, sommet):
        if sommet not in self._numero:
            raise SommetError("Sommet non trouvé")

        index = self._numero.pop(sommet)
        self._sommets.pop(index)

        self._mat.pop(index)
        for row in self._mat:
            row.pop(index)

        for i, s in enumerate(self._sommets):
            self._numero[s] = i

    def supprimer_tous_arcs(self):
        n = len(self._sommets)
        self._mat = [[None] * n for _ in range(n)] 

    def supprimer_tous_sommets(self):
        self._sommets.clear()
        self._numero.clear()
        self._mat = [[]]

    def liste_sommets(self):
        return self._sommets.copy()

    def liste_voisins(self,sommet):
        ns = self._numero[sommet]
        V = []
        for i in range(len(self._sommets)):
            if self._mat[ns][i] != None:
                V.append(self._sommets[i])
        return V
        # return [self._sommets[i] for i in range(len(self._sommets)) if self._mat[ns][i] != None ]
    
    def liste_predecesseurs(self,sommet):
        ns = self._numero[sommet]
        V = []
        for i in range(len(self._sommets)):
            if self._mat[i][ns] != None: # seul changement par rapport à voisins
                V.append(self._sommets[i])
        return V
        # return [self._sommets[i] for i in range(len(self._sommets)) if self._mat[i][ns] != None ]
    
    def poids(self,A,B):
        return self._mat[self._numero[A]][self._numero[B]]

    def poidschemin(self,L):
        # L liste de sommets
        # calculer le poids total du chemin qui passe par les sommets de L
        total = 0
        for i in range(len(L)-1):
            total += self.poids(L[i],L[i+1])
        return total