
from random import randint

def selectionneCaseAleatoire(labyrinthe):
	nbLignes = len(labyrinthe)
	nbColonnes = len(labyrinthe[0])

	i = 0
	j = 0
	x = -1
	while x < 0:
		i = randint(0, nbLignes)
		j = randint(0, nbColonnes)

		x = labyrinthe[i][j]

	return i, j

