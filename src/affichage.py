
from my_curses import *

# Dictionnaire permettant de coder la façon dont on affiche les objets
# Les clés entières permettent notamment d'encoder les cases du labyrinthe
affichage = {
	## Objets
	# bottes de sept lieux
	52: {
		"couleur": JAUNE,
		"caractere": "‼"
	},
	# Carte
	51: {
		"couleur": JAUNE,
		"caractere": "█"
	},
	# Casque d'observation
	50: {
		"couleur": JAUNE,
		"caractere": "▲"
	},

	# Chemin

	0: {
		"couleur": BLANC,
		"caractere": " "
	},

	## Murs et intersections

	-1: {
		"couleur": BLANC,
		"caractere": "1"
	},
	-2: {
		"couleur": BLANC,
		"caractere": "─"
	},
	-3: {
		"couleur": BLANC,
		"caractere": "│"
	},
	-4: {
		"couleur": BLANC,
		"caractere": "┼"
	},
	-5: {
		"couleur": BLANC,
		"caractere": "├"
	},
	-6: {
		"couleur": BLANC,
		"caractere": "┤"
	},
	-7: {
		"couleur": BLANC,
		"caractere": "┬"
	},
	-8: {
		"couleur": BLANC,
		"caractere": "┴"
	},
	-9: {
		"couleur": BLANC,
		"caractere": "└"
	},
	-10: {
		"couleur": BLANC,
		"caractere": "┘"
	},
	-11: {
		"couleur": BLANC,
		"caractere": "┌"
	},
	-12: {
		"couleur": BLANC,
		"caractere": "┐"
	},

	## Joueur
	"joueur": {
		"couleur": BLEU,
		"caractere": "☺"
	},

	## Depart et Arrivee
	4: {
		"couleur": VERT,
		"caractere": "D"
	},
	5: {
		"couleur": VERT,
		"caractere": "A"
	},

	## Ennemis
	"minotaure" : {
		"couleur" : ROUGE,
		"caractere" : "☺"},
	
	"spectre" : {
		"couleur" : MAGENTA,
		"caractere" : "☺"
	}
}


