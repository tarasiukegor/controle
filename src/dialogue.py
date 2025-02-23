from graphes import GraphePondere
from automate import *
from map import *


def cree_phrases(character,phrases):
    for i in phrases:
        dialogues_list[character].ajouter_sommet(i)

def cree_arcs(character, arcs):
    for first, second, third, *commands, in arcs:
        dialogues_list[character].ajouter_arc(first,second,third, commands if commands else None)



# structure des dialogues_list sous forme de graphes
dialogues_list = {
    "Chaffeur" : GraphePondere(),
    "Ivrogne": GraphePondere(),
    "Barman": GraphePondere(),
    "Maire": GraphePondere(),
}


chaffeur_phrases = [
    "Eh bien, monseigneur, prêt pour Strasbourg?",
    "Oh, vous serez surpris ! La ville a énormément changé ces cinq dernières années. Une prospérité fulgurante !",
    "Eh bien, avant, c'était un simple carrefour commercial, mais aujourd'hui, Strasbourg est devenu le centre logistique de la région. Les marchands affluent, les contrats se multiplient… et tout ça en très peu de temps !",
    "Peut-être… ou alors, il y a des forces noires à l'œuvre, héhé. *il rit en jetant un coup d'œil à Michel*",
    "*Quelques heures passent* Nous y voilà, monseigneur. Bonne négociation.",
    "Au revoir"
]

cree_phrases("Chaffeur",chaffeur_phrases)
cree_arcs("Chaffeur",[
    (chaffeur_phrases[0],chaffeur_phrases[1],["Allons-y. Plus vite j'y suis, mieux c'est."],),
    (chaffeur_phrases[1],chaffeur_phrases[2],["Ah ? Comment ça ?"]),
    (chaffeur_phrases[2],chaffeur_phrases[3],["Une croissance aussi rapide... Intéressant."]),
    (chaffeur_phrases[3],chaffeur_phrases[4],["Tss… ne raconte pas de bêtises."]),
    (chaffeur_phrases[4],chaffeur_phrases[5],["Au revoir"], exit_chaffeur)
    ])
    

ivrogne_phrases = [
    "Hé, l'ami ! T'aurais pas une p'tite goutte à m'offrir ? J'ai la gorge plus sèche qu'un vieux parchemin...",
    "Ahh, merci l'ami ! T'es un vrai bon !",
    "Bonne journée, mon ami",
    "Tss… radin ! Va donc, j'boirai sans toi !",
    # "Merci mon ami, je n'oublierai jamais ta gentillesse.",
    # "Mettez-le à la porte du bar, c'est une \"personne\" désagréable."

]

cree_phrases("Ivrogne", ivrogne_phrases)
cree_arcs("Ivrogne", [
    (ivrogne_phrases[0],ivrogne_phrases[1], ["Tiens"], (acheter, [10]), (reputation_status, [1])), # j'ai pas du temps pour finir, mais l'idee c'est de le donner du vin ou jsp, et a la prochaine interaction, il nous dit que je suis son ami etc
    (ivrogne_phrases[1],ivrogne_phrases[2], ["Vas y"]),
    (ivrogne_phrases[0],ivrogne_phrases[3], ["Laisse moi"]),
])


barman_phrases = [
    "Bienvenue, voyageur ! Qu'est-ce qui vous amène à la taverne aujourd'hui ?",
    "Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.",
    "Le premier verre est à 10 pièces.",
    "Le second, un peu plus rare, est à 100 pièces.",
    "Voilà, un verre bien rempli pour vous.",
    "Pas de problème, peut-être une autre fois. À la prochaine !",
    "Désolé, vous n'avez pas assez d'argent.",
]
# cree_phrases("Barman", barman_phrases)
# cree_arcs("Barman",[
#     (barman_phrases[],barman_phrases[], []),
#     (barman_phrases[],barman_phrases[], []),
#     (barman_phrases[],barman_phrases[], []),
#     (barman_phrases[],barman_phrases[], []),
#     (barman_phrases[],barman_phrases[], []),
# ])

# dialogues_list["Barman"].ajouter_arc("Bienvenue, voyageur ! Qu'est-ce qui vous amène à la taverne aujourd'hui ?","Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix." , ["Je veux boire quelque chose bien fort"])
# dialogues_list["Barman"].ajouter_arc("Bienvenue, voyageur ! Qu'est-ce qui vous amène à la taverne aujourd'hui ?","Pas de problème, peut-être une autre fois. À la prochaine !", ['Au revoir'])

# dialogues_list["Barman"].ajouter_arc("Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.","Le premier verre est à 10 pièces.", ["qq chose pas chere"])
# dialogues_list["Barman"].ajouter_arc("Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.","Le second, un peu plus rare, est à 100 pièces.", ["chere"])
# dialogues_list["Barman"].ajouter_arc("Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.","Pas de problème, peut-être une autre fois. À la prochaine !",["je ne veux paaaaaaas"])

# dialogues_list["Barman"].ajouter_arc("Le second, un peu plus rare, est à 100 pièces.","Voilà, un verre bien rempli pour vous.", ["Tiens le 100"])
# dialogues_list["Barman"].ajouter_arc("Le second, un peu plus rare, est à 100 pièces.","Pas de problème, peut-être une autre fois. À la prochaine !", ["j'ai pas d'argent"])

# dialogues_list["Barman"].ajouter_arc("Le premier verre est à 10 pièces.", "Voilà, un verre bien rempli pour vous.",["Tiens le 10"])
# dialogues_list["Barman"].ajouter_arc("Le premier verre est à 10 pièces.", "Pas de problème, peut-être une autre fois. À la prochaine !",["je ne veux pas cette boisson"])




# dialogues_list["Barman"].ajouter_arc("Désolé, vous n'avez pas assez d'argent.",
#                                 "Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.",
#                                 ["Je va choisir un autre"])



maire_phrases = [
    "Bienvenue à Strasbourg, messire. J'attendais votre arrivée.\n(Il sourit, un peu trop largement, et fait un geste mécanique de la main.)\nPrenez place, je vous en prie.",
    "Ah... avant que nous commencions, j'ai une requête particulière. J'ai une allergie rare au bronze. Cette boîte que vous portez... pourriez-vous la remettre à mon serviteur ?",
    "Alors, dites-moi… quel est l'objet de votre visite ?",
    "Comme vous voulez. C'est votre choix, bien sûr.\n(Il se redresse légèrement.)",
    "Merci, c'est très apprécié.\n(Son sourire s'élargit.)",
    "Merveilleux ! Je suis toujours ravi d'accueillir de nouveaux partenaires. Encore plus lorsqu'ils viennent d'Allemagne... Vous comprenez, nous avons des relations internationales de plus en plus vastes.\n(Le maire croise les mains et s'appuie légèrement sur son bureau.)\nMais voyez-vous…\n(Il hésite un instant.)\nIci, la situation est… complexe.",
    "Pour être franc avec vous, je ne suis pas l'homme le plus puissant de cette ville. Strasbourg a prospéré rapidement ces dernières années, mais ce n'est pas uniquement grâce à la mairie.",
    "La mafia a une influence considérable ici. Sans leur approbation, aucun accord de coopération ne pourra être signé. Je dois donc vous envoyer auprès de leur représentant.",
    "(Le maire sort une carte de Strasbourg et trace un chemin dessus avec son doigt.) Rendez-vous à la taverne. Là-bas, asseyez-vous sur le troisième tabouret en partant de la gauche. Un informateur viendra s'asseoir à votre droite. Il vous dira ce qu'il y a à savoir. (Le maire se lève et tend la main vers la porte.)",
    "Bonne chance, messire Michel. Vous en aurez besoin."

]


cree_phrases("Maire", maire_phrases)
cree_arcs("Maire", [
    (maire_phrases[0],maire_phrases[2], ["bonjour"]),
    (maire_phrases[2],maire_phrases[5], ["Je viens négocier un accord de coopération entre ma seigneurie et Strasbourg."]),
    (maire_phrases[2],maire_phrases[5], ["Je suis ici pour discuter d'opportunités commerciales."]),

    (maire_phrases[1], maire_phrases[3], ["Non, je préfère la garder."], (reputation_status, [-1])),
    (maire_phrases[1], maire_phrases[4], ["Oh, désolé, je ne savais pas, voilà pour vous"], (reputation_status, [1]),
                                                                                            (remove_from_inventory, ["Bronze Cigarette Box",] )),

    
    (maire_phrases[3], maire_phrases[5], ["Je suis ici pour discuter d'opportunités commerciales."]),
    (maire_phrases[4], maire_phrases[5], ["Donc, Je suis ici pour discuter d'opportunités commerciales."]),
    (maire_phrases[5], maire_phrases[6], ["Que voulez-vous dire par là ?"]),
    (maire_phrases[6],maire_phrases[7], ["Quelle absurdité... alors que proposez-vous ?"]),
    (maire_phrases[7],maire_phrases[8], ["Je vais voir"], (map_update, [strasbourg, [
                                                                                    ["Strasbourg Tavern", (170, 180)],
                                                                                    ["Strasbourg Forge", (650, 460)],
                                                                                    ["Strasbourg Marche", (130, 300)]
                                                                                    ],
                                                                                    
                                                                                    [
                                                                                        ("Strasbourg Square", "Strasbourg Tavern"),
                                                                                        ("Strasbourg Square", "Strasbourg Forge"),
                                                                                        ("Strasbourg Square", "Strasbourg Marche"),
                                                                                    ],])),
    (maire_phrases[8],maire_phrases[9], ["Au revoir"]),
    
    
])


# on utilise la fonction automate pour creer la systeme des dialogues_list 
dialogue_systems = {
    "Chaffeur": automate(dialogues_list["Chaffeur"], dialogues_list["Chaffeur"].liste_sommets()[0],gamestate),
    "Ivrogne": automate(dialogues_list["Ivrogne"], ivrogne_phrases[0], gamestate),
    "Maire": automate(dialogues_list["Maire"], dialogues_list["Maire"].liste_sommets()[0],gamestate)
    # "Barman": automate(dialogues_list["Barman"], dialogues_list["Barman"].liste_sommets()[0], gamestate),
}
