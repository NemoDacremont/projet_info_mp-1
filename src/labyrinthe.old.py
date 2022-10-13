'''
def creeMatriceAdjacence(n: int, p: int) -> list[list[int]]:
	"""
		n: nombre de lignes
		p: nombre de colonnes

		Permet de générer une matrice d'adjacence représentant un graphe à n*p sommets ayant aucune arête
	"""
	adjacence = [[0 for j in range(p)] for i in range(n)]

	return adjacence

def retireLien(adjacence: list[list[int]], trucBizarreAnael, nbUnionsFaites: int):
	# On choisit dans un premier temps quels parties lier
	representant1 = randint(0, nbUnionsFaites)
	representant2 = randint(0, nbUnionsFaites)

	# On choisit ensuite quelle mur on retire
	

	pass

def creeLabyrinthe(n: int, p: int):
		# on travaillera plutôt avec des graphes après réflexion

		adjacence = creeMatriceAdjacence(n, p)

		# À la fin de la boucle for, on aura retirer n*p liens
		# on aura donc toutes les cases liées car chaque itération permet
		# de faire un lien entre 2 parties disjointes du graphe de départ
		for i in range(n*p):
			retireLien(adjacence)

		return out


print(create(10, 5))
'''
