
from random import randint

def selectionneCaseAleatoire(labyrinthe):
	"""
		Type: Fonction
		paramètre:
			- labryinthe: dictionnaire au format d'un labyrinthe
	"""
	nbLignes = len(labyrinthe)
	nbColonnes = len(labyrinthe[0])

	i = 0
	j = 0
	x = -1

	# permet de ne sélectionner qu'une case étant un chemin, on ne peut donc pas générer
	# sur un objet, la case de départ, un mur, etc...
	while x != 0:
		i = randint(0, nbLignes - 1)
		j = randint(0, nbColonnes - 1)

		x = labyrinthe[i][j]

	return i, j

