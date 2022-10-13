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
	
	if j != len(labyrinthe[0]) : #On regarde si on est au bord
		if labyrinthe[i][j + 1] == -1 and labyrinthe[i][j + 2] != connexe :
			admissible = True
			mursAdmissibles.append((i, j + 1, labyrinthe[i][j + 2]))
			
#Tester en haut
	
	if i != len(labyrinthe) : #On regarde si on est au bord
		if labyrinthe[i - 1][j] == -1 and labyrinthe[i - 2][j] != connexe :
			admissible = True
			mursAdmissibles.append((i -1, j, labyrinthe[i - 2][j]))
	
#Tester en bas
	
	if i != len(0) : #On regarde si on est au bord
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
		
			
	