

def creeBrouillard(n: int, p: int):
	"""
		Type: Fonction
		Paramètres:
			- n: entier, correspond au nombre de lignes contenant des chemins avant la destruction de murs
			- p: entier, correspond au nombre de colonnes contenant des chemins avant la destruction de murs

		Retourne: Matrice de 0 ou 1 caractérisant la découverte des cases par le joueur
	"""
	nbLignes = 2*n - 1
	nbColonnes = 2*p - 1

	brouillard = [[0 for j in range(nbColonnes)] for i in range(nbLignes)]
	return brouillard

def metAJourBrouillard(brouillard, iPlayer: int, jPlayer: int, distanceVue: int):
	"""
		Type: procédure
		Paramètres:
			- brouillard: brouillard à mettre à jour
			- iPlayer:

		Résumé:
			Met à jour les cases découvertes par le joueur
	"""
	nbLignes = len(brouillard)
	nbColonnes = len(brouillard[0])

	# Actualise chaque cases dans un rayon de distanceVue
	for i in range(-distanceVue, distanceVue):
		for j in range(-distanceVue + abs(i), distanceVue - abs(i)):

			if iPlayer + i > nbLignes-1 or jPlayer + j > nbColonnes-1:
				continue
			if iPlayer + i < 0 or jPlayer + j < 0:
				continue

			brouillard[iPlayer + i][jPlayer + j] = 1



