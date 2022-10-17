from random import randint

def cheminsPossibles(labyrinthe : list, i : int, j : int, depart : tuple) -> list :
	"""
	

	Paramètres
	----------
	labyrinthe : matrice du labyrinthe considéré
	i : numéro de la ligne à partir de laquelle on cherche un  chemin
	j : numéro de la colonne à partir de laquelle on cherche un  chemin
	depart : coordonnées de la case précédante dans le chemin total

	Return
	------
	Une liste (éventuellement vide) de tuples (i, j) des coordonnées des cases foù il est possible d'aller sans retourner en arrière'

	"""
	cheminsAdmissibles = [] #Liste des chemins possibles

	#Tester à gauche
	if j != 0 : #On regarde si on est au bord
		if labyrinthe[i][j - 1] <= 0 and j - 1 != depart[1] :
			cheminsAdmissibles.append((i, j - 1))

	#Tester à droite
	if j != len(labyrinthe[0]) - 1 : #On regarde si on est au bord
		if labyrinthe[i][j + 1] <= 0 and j + 1 != depart[1] :
			cheminsAdmissibles.append((i, j + 1))

	#Tester en haut
	if i != 0 : #On regarde si on est au bord
		if labyrinthe[i - 1][j] <= 0 and i - 1 != depart[0] :
			cheminsAdmissibles.append((i - 1, j))

	#Tester en bas
	if i != len(labyrinthe) - 1 : #On regarde si on est au bord
		if labyrinthe[i + 1][j] <= 0 and i + 1 != depart[0] :
			cheminsAdmissibles.append((i + 1, j))

	return cheminsAdmissibles

def trouverLeChemin(labyrinthe : list, iDepart : int, jDepart : int) -> list :
	"""
	

	Paramètres
	----------
		labyrinthe : matrice du labyrinthe
		iDepart : numéro de la ligne d'où commence le chemin
		jDepart : numéro de la colonne d'où commence le chemin
	
	Return
	------
		Une liste ordonnée de tuples(i, j) formant les coordonnées dans l'ordre reliant la case de départ (iDepart, jDepart) à une arrivée (dernier élément de la liste)
		L'extrémité du chemin est forcément dans un cul-de-sac
	"""
	#Inintialisation
	chemin = [(iDepart, jDepart)]
	cheminsAdmissibles = cheminsPossibles(labyrinthe, iDepart, jDepart, (None, None))
	#La boucle se termine car le graphe est acyclique
	while len(cheminsAdmissibles) > 0 :
		prochainChemin = cheminsAdmissibles[randint(0), len(cheminsAdmissibles)]
		chemin.append(prochainChemin)
		cheminsAdmissibles = cheminsPossibles(labyrinthe, prochainChemin[0], prochainChemin[1], chemin[-2])
	
	return chemin
		
		