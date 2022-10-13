def genereMatriceConnexe(n : int, p : int) -> list :
	"""
	
	Paramètres :
		n (int) : nombre de colonnes du labyrinthe
		p (int) : nombre de lignes du labyrinthe
		
	Créé la "liste de connexité" du labyrinthe.
	L'indice des éléments de la liste indiquent le numéro de la composante connexe considérée.
	Chaque éléments sont des dictionnaires dont les clefs sont "liensPossibles" et "liensImpossibles", pointant tout deux vers deux listes de tuples.
	Un tuple représente un couple de coordonnées correspondant à un sommet.
	Si le sommet appartient à l'une des deux listes, alors il appartient à la composante connexe associée au dictionnaire.
	S'il appartient à la liste "liensPossibles", alors ce sommet peut être choisi pour créer un lien avec un autre sommet.
	S'il appartient à la liste "liensImpossibles", alors le sommet admet pour voisin uniquement des sommet qui appartiennent à la même composante connexe.
	
	Lors de la création de la liste, chaque composante connexe se voit attribuer un unique sommet dans sa liste "liensPossibles", la liste "liens"Impossibles" restant initialement vide.'

	"""
	
	connexe = []
	for i in range(n) :
		for j in range(p) :
			connexe.append({"liensPossibles" : [(i, j)], "liensImpossibles" : []})
	return connexe