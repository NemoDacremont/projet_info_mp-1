

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

	# Remplit par défaut par des 0 encodant la non-découverte des cases.
	brouillard = [[0 for j in range(nbColonnes)] for i in range(nbLignes)]

	return brouillard

def metAJourBrouillard(brouillard: list, joueur: dict, distanceVue: int, brouillardEstPersistant: bool = False):
	"""
		Type: procédure
		Paramètres:
			- brouillard: brouillard à mettre à jour
			- iPlayer:
			- brouillardEstPersistant: bool = False

		Résumé:
			Met à jour les cases découvertes par le joueur
	"""
	# Allège les notations
	iJoueur = joueur["iJoueur"]
	jJoueur = joueur["jJoueur"]
	nbLignes = len(brouillard)
	nbColonnes = len(brouillard[0])

	# Actualise chaque cases dans un rayon de distanceVue lorsque le brouillard est persistant, permet d'avoir
	# une complexité en O(1)
	if brouillardEstPersistant:
		for i in range(-distanceVue, distanceVue):
			for j in range(-distanceVue + abs(i), distanceVue - abs(i)):

				# Teste si les cases à modifier ne sont pas pas en réalité hors du labyrinthe, ie quand on est au bord
				if iJoueur + i > nbLignes-1 or jJoueur + j > nbColonnes-1:
					continue
				if iJoueur + i < 0 or jJoueur + j < 0:
					continue

				brouillard[iJoueur + i][jJoueur + j] = 1

	# Si le brouillard n'est pas persistant, on doit balayer l'entierté de la matrice et ne placer des 1 que lorsqu'on est
	# dans le champ de vision
	else:
		for i in range(nbLignes):
			for j in range(nbColonnes):
				# teste si la case est dans le champ de vision
				if (i - iJoueur)**2 + (j - jJoueur)**2 < distanceVue**2:
					brouillard[i][j] = 1

				else:
					brouillard[i][j] = 0




