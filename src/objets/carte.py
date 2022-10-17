
from utils import selectionneCaseAleatoire
from affichage import *

from my_curses import *


def creeCarte(labyrinthe: list, joueur: dict):
	"""
		type: Fonction
		paramètres:
			- jeu: dictionnaire au format jeu

		Cree un objet
	"""

	i, j = selectionneCaseAleatoire(labyrinthe)

	carte = {
		"id": 51,
		"i": i,
		"j": j
	}
	labyrinthe[i][j] = 51

	return carte

def utiliseCarte(joueur: dict):
	joueur["brouillardEstPersistant"] = True


