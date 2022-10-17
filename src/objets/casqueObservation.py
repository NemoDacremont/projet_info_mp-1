
from utils import selectionneCaseAleatoire

def creeCasque(jeu):
	"""
		type: Fonction
		paramètres:
			- jeu: dictionnaire au format jeu

		Cree un objet
	"""

	labyrinthe = jeu["labyrinthe"]

	i, j = selectionneCaseAleatoire(labyrinthe)

	casque = {
		"i": i,
		"j": j
	}

	return casque




