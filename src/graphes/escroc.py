from automate import *

x = GraphePondere()
L=["inactif",
   "voulez-vous de ce beau tapis ?",
   "merci, ravi de faire des affaires avec vous !",
   "200€",
   "au revoir"] 
for s in L:
    x.ajouter_sommet(s)

for a,b,e in [ (L[0],L[1],["bonjour !"]),
               (L[1],L[4],["non merci"]),
               (L[1],L[3],["combien ?"]),
               (L[3],L[4],["non merci"]),
               (L[3],L[2],["Ok !"]),
               (L[2],L[4],["au revoir"])]:
    x.ajouter_arc(a,b,e)

escroc = automate(x,"inactif")