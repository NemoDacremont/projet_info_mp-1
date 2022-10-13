
from labyrinthe import genereLabyrinthe
import my_curses as curse

OBJETS = {
	-1: {
		"couleur": curse.BLANC,
		"caractere": "┼"
	},
	-2: {
		"couleur": curse.BLANC,
		"caractere": ""
	}
}

def load():



	game = {
		"labyrinthe": genereLabyrinthe(n, p)
	}

def update(game):
	"""
		Met à jour les données du jeu	
	"""

	pass

def draw(game):
	"""
		Affiche l'interface
	"""
	curse.clear()


