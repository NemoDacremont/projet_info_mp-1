
import random as rd

def estAdmissible(labyrinthe, i, j, connexe) :
	mursAdmissibles = [] #Liste des murs qui peuvent être cassés
	admissible = False
	
#Tester à gauche
	
	if j != 0 : #On regarde si on est au bord
		if labyrinthe[i][j - 1] == -1 and labyrinthe[i][j - 2] != connexe :
			admissible = True
			mursAdmissibles.append((i, j - 1, labyrinthe[i][j - 2])) #On note les coordonnées du mur à casser et la composante connexe suivante
	
#Tester à droite
	
	if j != len(labyrinthe[0]) - 1 : #On regarde si on est au bord
		if labyrinthe[i][j + 1] == -1 and labyrinthe[i][j + 2] != connexe :
			admissible = True
			mursAdmissibles.append((i, j + 1, labyrinthe[i][j + 2]))
			
#Tester en haut
	
	if i != 0 : #On regarde si on est au bord
		if labyrinthe[i - 1][j] == -1 and labyrinthe[i - 2][j] != connexe :
			admissible = True
			mursAdmissibles.append((i -1, j, labyrinthe[i - 2][j]))
	
#Tester en bas
	if i != len(labyrinthe) - 1 : #On regarde si on est au bord
		if labyrinthe[i + 1][j] == -1 and labyrinthe[i + 2][j] != connexe :
			admissible = True
			mursAdmissibles.append((i + 1, j, labyrinthe[i + 2][j]))
			
	return admissible, mursAdmissibles

def percerUnMur(labyrinthe : list, n : int, p : int) :
	i = rd.randint(0, n -1) * 2 #ordonnée de la case choisie
	j = rd.randint(0, p - 1) * 2 #abscisse de la case choisie
	connexe = labyrinthe[i][j] #Numéro de la composante connexe de la case considérée
	admissible = False #Booléen qui indique si un mur peut être cassé
	
	#Recherche d'un mur à casser
	while not admissible :
		admissible, mursAdmissibles = estAdmissible(labyrinthe, i, j, connexe)
		i = rd.randint(0, n -1) * 2
		j = rd.randint(0, p - 1) * 2
		
	mur = mursAdmissibles[rd.randint(0, len(mursAdmissibles) - 1)] #Sélection du mur à casser
	
	labyrinthe[mur[0]][mur[1]] = connexe
	connexeFusion = mur[2] #Numéro de la composante connexe à absorber
	
	for k in range(len(labyrinthe)) :
		for l in range(len(labyrinthe[0])) :
			if labyrinthe[k][l] == connexeFusion:
				labyrinthe[k][l] = connexe

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
lab= genereLabyrinthe(6, 6)
for i in range(len(lab)):
	line = ""
	for j in range(len(lab[0])):
		line += f"{lab[i][j]},"
	print(f"[{line}]")
