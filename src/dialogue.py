from graphes import GraphePondere
from automate import automate

# Structure des dialogues sous forme de graphes
dialogues = {
    "Ivrogne": GraphePondere(),
    "Barman": GraphePondere()
}

# on va faire la fonction qui va automatiser la creation des dialogues
dialogues["Ivrogne"].ajouter_sommet("Hé, l'ami ! T'aurais pas une p'tite goutte à m'offrir ? J'ai la gorge plus sèche qu'un vieux parchemin...")
dialogues["Ivrogne"].ajouter_sommet("Ahh, merci l'ami ! T'es un vrai bon !")
dialogues["Ivrogne"].ajouter_sommet("Tss… radin ! Va donc, j'boirai sans toi !")


dialogues["Barman"].ajouter_sommet("Bienvenue, voyageur ! Qu'est-ce qui vous amène à la taverne aujourd'hui ?")
dialogues["Barman"].ajouter_sommet("Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.")
dialogues["Barman"].ajouter_sommet("Le premier verre est à 10 pièces.")
dialogues["Barman"].ajouter_sommet("Le second, un peu plus rare, est à 100 pièces.")
dialogues["Barman"].ajouter_sommet("Voilà, un verre bien rempli pour vous.")
dialogues["Barman"].ajouter_sommet("Pas de problème, peut-être une autre fois. À la prochaine !")

dialogues["Ivrogne"].ajouter_arc("Hé, l'ami ! T'aurais pas une p'tite goutte à m'offrir ? J'ai la gorge plus sèche qu'un vieux parchemin...", "Ahh, merci l'ami ! T'es un vrai bon !", ["Tiens"])
dialogues["Ivrogne"].ajouter_arc("Hé, l'ami ! T'aurais pas une p'tite goutte à m'offrir ? J'ai la gorge plus sèche qu'un vieux parchemin...", "Tss… radin ! Va donc, j'boirai sans toi !", ["laisse moi"])

dialogues["Barman"].ajouter_arc("Bienvenue, voyageur ! Qu'est-ce qui vous amène à la taverne aujourd'hui ?","Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix." , ["Je veux boire quelque chose bien fort"])
dialogues["Barman"].ajouter_arc("Bienvenue, voyageur ! Qu'est-ce qui vous amène à la taverne aujourd'hui ?","Pas de problème, peut-être une autre fois. À la prochaine !", ['Au revoir'])

dialogues["Barman"].ajouter_arc("Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.","Le premier verre est à 10 pièces.", ["qq chose pas chere"])
dialogues["Barman"].ajouter_arc("Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.","Le second, un peu plus rare, est à 100 pièces.", ["chere"])
dialogues["Barman"].ajouter_arc("Alors, quel breuvage désireriez-vous ? Nous avons plusieurs choix.","Pas de problème, peut-être une autre fois. À la prochaine !",["je ne veux paaaaaaas"])

dialogues["Barman"].ajouter_arc("Le second, un peu plus rare, est à 100 pièces.","Voilà, un verre bien rempli pour vous.", ["Tiens le 10"])
dialogues["Barman"].ajouter_arc("Le second, un peu plus rare, est à 100 pièces.","Pas de problème, peut-être une autre fois. À la prochaine !", ["j'ai pas d'argent"])

dialogues["Barman"].ajouter_arc("Le premier verre est à 10 pièces.", "Voilà, un verre bien rempli pour vous.",["Tiens le 100"])
dialogues["Barman"].ajouter_arc("Le premier verre est à 10 pièces.", "Pas de problème, peut-être une autre fois. À la prochaine !",["je ne veux pas cette boisson"])







# on utilise la fonction automate pour creer la systeme des dialogues
dialogue_systems = {
    "Ivrogne": automate(dialogues["Ivrogne"], "Hé, l'ami ! T'aurais pas une p'tite goutte à m'offrir ? J'ai la gorge plus sèche qu'un vieux parchemin..."),
    "Barman": automate(dialogues["Barman"], "Bienvenue, voyageur ! Qu'est-ce qui vous amène à la taverne aujourd'hui ?")
}