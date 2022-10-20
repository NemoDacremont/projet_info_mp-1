
from utils import selectionneCaseAleatoire
from affichage import *

from my_curses import *


def creeBottes(labyrinthe: list, joueur: dict):
	"""
		type: Fonction
		paramètres:
			- jeu: dictionnaire au format jeu

		Cree un objet
	"""

	i, j = selectionneCaseAleatoire(labyrinthe)

	bottes = {
		"id": 52,
		"i": i,
		"j": j
	}
	labyrinthe[i][j] = 52

	return bottes

def utiliseBottes(joueur: dict):
	joueur["vitesse"] += 10


