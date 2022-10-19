
from utils import selectionneCaseAleatoire
from affichage import *

from my_curses import *


def creeCasque(labyrinthe: list, joueur: dict):
	"""
		type: Fonction
		paramètres:
			- jeu: dictionnaire au format jeu

		Cree un objet
	"""

	i, j = selectionneCaseAleatoire(labyrinthe)

	casque = {
		"id": 50,
		"i": i,
		"j": j
	}
	labyrinthe[i][j] = 50

	return casque

def utiliseCasque(joueur: dict):
	joueur["distanceVue"] += 2

