
from my_curses import *

affichage = {
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
	}
}

