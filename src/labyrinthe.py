
import random as rd

def estAdmissible(labyrinthe : list, i :int, j :int, connexe : int) -> list :
	"""
	

	Paramètres :
		labyrinthe : matrice du labyrinthe
		i : ligne de la case testée (oligne réelle)
		j : colonne de la case testée (colonne réelle)
		connexe : numéro de la composante connexe à laquell appartient la case

	Pour la case considérée, test si il y a des murs qui peuvent être cassés dans les quatre directions cardinales.
	Renvoie une liste, éventuellement vide, de tuples de taille 3 sous la forme (x, y, connexe2)
	x et y désigne les coordonnées matricielle (ligne, colonne) du mur admissible, connexe2 désigne le numéro de la composante connexe de l'autre côté dudit mur.
	"""
	mursAdmissibles = [] #Liste des murs qui peuvent être cassés
	
#Tester à gauche
	
	if j != 0 : #On regarde si on est au bord
		if labyrinthe[i][j - 1] == -1 and labyrinthe[i][j - 2] != connexe :
			mursAdmissibles.append((i, j - 1, labyrinthe[i][j - 2])) #On note les coordonnées du mur à casser et la composante connexe suivante
	
#Tester à droite
	
	if j != len(labyrinthe[0]) - 1 : #On regarde si on est au bord
		if labyrinthe[i][j + 1] == -1 and labyrinthe[i][j + 2] != connexe :
			mursAdmissibles.append((i, j + 1, labyrinthe[i][j + 2]))
			
#Tester en haut
	
	if i != 0 : #On regarde si on est au bord
		if labyrinthe[i - 1][j] == -1 and labyrinthe[i - 2][j] != connexe :
			mursAdmissibles.append((i -1, j, labyrinthe[i - 2][j]))
	
#Tester en bas
	if i != len(labyrinthe) - 1 : #On regarde si on est au bord
		if labyrinthe[i + 1][j] == -1 and labyrinthe[i + 2][j] != connexe :
			mursAdmissibles.append((i + 1, j, labyrinthe[i + 2][j]))
			
	return mursAdmissibles

def percerUnMur(labyrinthe : list, n : int, p : int) -> None :
	"""
	
	Paramètres :
		- labyrinthe : la matrice du labyrinthe dans lequel il faut ouvrir un mur
		- n : nombres de lignes du labyrinthe (ne compte que les cases, pas le nombre réel de ligne de la matrice)
		- p : nombre de colonnes du labyrinthe (ne compte que les cases, pas le nombre réel de colonnes)
	
	Procédure qui sélectionne aléatoirement deux cases mitoyennes et n'appartenant pas à la même composante connexe, retire le mur entre les deux et fusionne les composantes connexes.'

	"""
	i = rd.randint(0, n -1) * 2 #ligne de la case choisie
	j = rd.randint(0, p - 1) * 2 #colonne de la case choisie
	# Les mutliplications par deux assurent de ne pas tomber sur un mur mais bien sur une case
	connexe = labyrinthe[i][j] #Numéro de la composante connexe de la case considérée
	mursAdmissibles = [] #Initialisation d'une liste
	
	#Recherche d'un mur à casser
	while len(mursAdmissibles) == 0 :
		mursAdmissibles = estAdmissible(labyrinthe, i, j, connexe)
		i = rd.randint(0, n -1) * 2
		j = rd.randint(0, p - 1) * 2
		
	mur = mursAdmissibles[rd.randint(0, len(mursAdmissibles) - 1)] #Sélection du mur à casser
	
	connexe2 = mur[2]
	connexeNouveau = min(connexe, connexe2)
	connexeAncien = max(connexe, connexe2)
	labyrinthe[mur[0]][mur[1]] = connexeNouveau
	
	for k in range(len(labyrinthe)) :
		for l in range(len(labyrinthe[0])) :
			if labyrinthe[k][l] == connexeAncien:
				labyrinthe[k][l] = connexeNouveau

def genereCase(i: int, j: int, n: int, p: int) -> int:
	# Intersection mur
	if i%2==1 and j%2==1:
		return -2

	# Mur
	if i%2==(j+1)%2:
		return -1
	
	# chemin
	if i%2==0 and j%2==0:
		return i*p + j

	return -5


def genererLabyrintheBrut(n: int, p: int) -> list[list[int]]:
	"""
		n: nombre de lignes du labyrinthe
		p: nombre
		Génère un labyrinthe de dimension n*p
	"""

	colonnes = p*2 -1
	lignes = n*2 -1

	labyrinthe = [[genereCase(i, j, lignes, colonnes) for j in range(colonnes)] for i in range(lignes)]

	return labyrinthe

def genereLabyrinthe(n: int, p: int) -> list[list[int]]:
	labyrinthe = genererLabyrintheBrut(n, p)

	for i in range(n*p - 1):
		percerUnMur(labyrinthe, n, p)


	return labyrinthe

#lab = genereLabyrinthe(5, 5)
lab= genereLabyrinthe(50, 50)
for i in range(len(lab)):
	line = ""
	for j in range(len(lab[0])):
		line += f"{lab[i][j]},"
	print(f"[{line}]")
