
import random as rd

def saveLabInFile(labyrinthe, n: int, p: int, fileName: str, mode = "a"):
	text = ""
	for i in range(n):
		line = ""

		for j in range(p):
			n = labyrinthe[i][j]
			if n < -9:
				line += f"{labyrinthe[i][j]},"
			elif n < -0:
				line += f"{labyrinthe[i][j]},"
			elif n < 10:
				line += f" {labyrinthe[i][j]},"
			else:
				line += f"{labyrinthe[i][j]},"

		text += f"{line}\n"

	with open(fileName, "a") as file:
		file.write(text)
		file.write("----------------------------------------------\n")


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
	i = -1 # = rd.randint(0, n -1) * 2 #ligne de la case choisie
	j = -1 # rd.randint(0, p - 1) * 2 #colonne de la case choisie
	# Les mutliplications par deux assurent de ne pas tomber sur un mur mais bien sur une case
	connexe = labyrinthe[i][j] #Numéro de la composante connexe de la case considérée
	mursAdmissibles = [] #Initialisation d'une liste

	#Recherche d'un mur à casser
	while len(mursAdmissibles) == 0 :
		i = rd.randint(0, n -1) * 2
		j = rd.randint(0, p - 1) * 2
		connexe = labyrinthe[i][j]
		mursAdmissibles = estAdmissible(labyrinthe, i, j, connexe)

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
		return -4

	# Mur
	if i%2 == (j+1)%2:
		return -1

	# chemin
	if i%2==0 and j%2==0:
		return i*p + j

	# Même si ça ne devrait jamais arriver, on renvoie une valeur par défaut
	return -99



def formatteMur(labyrinthe, i: int, j: int, n: int, p: int):
	"""
		Type: Procédure
		Paramètres:
			- labyrinthe: la matrice encodant le labyrinthe
			- i: entier, correspond à la ligne de l'élément à modifier
			- j: entier, correspond à la colonne de l'élément à modifier
			- n: entier, correspond au nombre de lignes de labyrinthe
			- p: entier, correspond au nombre de colonnes de labyrinthe

			- labyrinthe[i][j] doit impérativement correspondre à un mur, soit un élément
			initialement encodé par un -1

		Résumé:
			transforme un mur quelconque en un mur horizontal ou vertical codé respectivement
			par -2 et -3.
	"""

	vertical = False
	horizontal = False

	# Teste si le mur est vertical
	if i==0:
		vertical = True
	else:
		if labyrinthe[i-1][j] < -3:
			vertical = True

	if i == n-1:
		vertical = True
	else:
		if labyrinthe[i+1][j] < -3:
			vertical = True

	# test si le mur est horizontal
	if j == 0:
		horizontal = True
	else:
		if labyrinthe[i][j-1] < -3:
			horizontal = True

	if j == p-1:
		horizontal = True
	else:
		if labyrinthe[i][j+1] < -3:
			horizontal = True

	### On compile le tout
	if horizontal:
		labyrinthe[i][j] = -2
	elif vertical:
		labyrinthe[i][j] = -3





def formatteIntersection(labyrinthe, i, j):
	"""
		Type: Procédure
		Paramètres:
			- labyrinthe: la matrice encodant le labyrinthe
			- i: entier, correspond à la ligne de l'élément à modifier
			- j: entier, correspond à la colonne de l'élément à modifier

			- labyrinthe[i][j] doit impérativement correspondre à une intersection, soit un élément
			initialement encodé par un -4

		Résumé:
			Comme formatteMur, permet de transformer une intersection en un angle si les coins ne
			sont pas connectés

			Exemple:
				Si le l'intersection est connecté à gauche et en bas, alors "┼" deviendra "┐" à l'affichage
	"""

	# booléens caractérisant les liaisons
	horizontal_gauche = False
	horizontal_droite = False
	vertical_haut = False
	vertical_bas = False

	# teste d'une liaison au dessus
	if labyrinthe[i-1][j] < 0:
		vertical_haut = True

	# teste d'une liaison en dessous
	if labyrinthe[i+1][j] < 0:
		vertical_bas = True

	# teste d'une liaison à gauche
	if labyrinthe[i][j-1] < 0:
		horizontal_gauche = True

	# teste d'une liaison à droite
	if labyrinthe[i][j+1] < 0:
		horizontal_droite = True

	### On compile le tout

	## 4 liaison
	if vertical_bas and vertical_haut and horizontal_droite and horizontal_gauche:
		labyrinthe[i][j] = -4

	## 3 liaisons
	elif vertical_bas and vertical_haut and horizontal_droite:
		labyrinthe[i][j] = -5
	elif vertical_bas and vertical_haut and horizontal_gauche:
		labyrinthe[i][j] = -6
	elif horizontal_gauche and horizontal_droite and vertical_bas:
		labyrinthe[i][j] = -7
	elif horizontal_gauche and horizontal_droite and vertical_haut:
		labyrinthe[i][j] = -8

	## 2 liaisons
	elif vertical_haut and horizontal_droite:
		labyrinthe[i][j] = -9
	elif vertical_haut and horizontal_gauche:
		labyrinthe[i][j] = -10
	elif vertical_bas and horizontal_droite:
		labyrinthe[i][j] = -11
	elif vertical_bas and horizontal_gauche:
		labyrinthe[i][j] = -12

	## 1 seule liaison
	elif vertical_bas or vertical_haut:
		labyrinthe[i][j] = -3
	elif horizontal_gauche or horizontal_droite:
		labyrinthe[i][j] = -2


def formatteLabyrinthe(labyrinthe, n: int, p: int) :
	"""
		Type: Procédure
		Paramètres:
			- labyrinthe: la matrice encodant le labyrinthe
			- i: entier, correspond à la ligne de l'élément à modifier
			- j: entier, correspond à la colonne de l'élément à modifier
			- n: entier, correspond au nombre de lignes de labyrinthe
			- p: entier, correspond au nombre de colonnes de labyrinthe

		Résumé:
			Permet de formatter les murs et les intersections du labyrinte à des
			fins d'affichage, les murs deviennent horizontaux ou verticaux et les
			intersections des coins...
	"""

	for i in range(n):
		for j in range(p):
			if labyrinthe[i][j] == -1:
				formatteMur(labyrinthe, i, j, n, p)
			elif labyrinthe[i][j] == -4:
				formatteIntersection(labyrinthe, i, j)


def genererLabyrintheBrut(n: int, p: int) -> list[list[int]]:
	"""
		Type: Fonction
		Paramètres:
			- n: nombre de lignes du labyrinthe
			- p: nombre

		Résumé:
			Génère un labyrinthe de dimension n*p
	"""

	colonnes = p*2 -1
	lignes = n*2 -1

	labyrinthe = [[genereCase(i, j, lignes, colonnes) for j in range(colonnes)] for i in range(lignes)]

	return labyrinthe

def genereLabyrinthe(n: int, p: int, debug = False) -> list[list[int]]:
	labyrinthe = genererLabyrintheBrut(n, p)

	colonnes = p*2 -1
	lignes = n*2 -1

	for i in range(n*p - 1):
		percerUnMur(labyrinthe, n, p)
		if debug:
			saveLabInFile(labyrinthe, lignes, colonnes, "./debug.txt")



	formatteLabyrinthe(labyrinthe, lignes, colonnes)

	return labyrinthe

#lab = genereLabyrinthe(5, 5)
'''
lab= genereLabyrinthe(5, 5)
for i in range(len(lab)):
	line = ""
	for j in range(len(lab[0])):
		line += f"{lab[i][j]},"
	print(f"[{line}]")
'''
