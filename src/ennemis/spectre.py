from random import randint
from affichage import *

"""
Module régissant le Spectre
---------------------------

Le Spectre est une créature du Labyrinthe qui traque constamment le héros.
Initiallement assez lent, il deviendra de plus en plus rapide lorsque la partie traîne en longueur.
S'il touche le joueur, celui-ci est téléporté aléatoirement dans le labyrinthe.
De plus, la vitesse du Minotaure augmente alors de 1 (cf minotaure.py)

Il est repréré en jeu par un cercle magenta.
"""

def creeSpectre(labyrinthe : list, joueur : dict) -> dict :

	"""
	Pramètres :
		labyrinthe : matrice du labyrinthe considéré
		joueur : dictionnaire contenant les informations du joueur

	Return :
		Dictionnaire au format d'un Spectre

	Remarques : le Spectre va poursuivre le joueur, son dictionnaire contient donc le chemin qui le relie au joueur.
	Plutôt que de générer ses coordonnées aléatoirement, on génère un chemin depuis le joueur et on place le Spectre au bout.
	Le déplacement sera ainsi très facile à calculer en exploitant l'acyclicité du labyrinthe.
	"""

	#Dimensions du labyrinthes (nombres de cases sans les murs)
	n, p = len(labyrinthe) // 2, len(labyrinthe[0]) // 2

	#Coordonnées du joueur (pour que le monstre n'apparaisse pas à-côté)
	iJoueur = joueur["iJoueur"]
	jJoueur = joueur["jJoueur"]

	#Trouver le chemin qui reliera le joueur au Spectre
	chemin = trouverLeChemin(labyrinthe, iJoueur, jJoueur)
	#Le Spectre ne doit pas être trop proche du joueur
	while len(chemin) < (n + p) // 2 :
		chemin = trouverLeChemin(labyrinthe, iJoueur, jJoueur)

	#On récupère les coordonnées du spectre au bout du chemin et on retire sa position
	iSpectre, jSpectre = chemin.pop()

	Spectre = {
		"ID" : 101,
		"iSpectre" : iSpectre,
		"jSpectre" : jSpectre,
		"chemin" : chemin,
		"mouvement" : 0,
		"vitesse" : 3}

	return Spectre

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
		if labyrinthe[i][j - 1] >= 0 and j - 1 != depart[1] :
			cheminsAdmissibles.append((i, j - 1))

	#Tester à droite
	if j != len(labyrinthe[0]) - 1 : #On regarde si on est au bord
		if labyrinthe[i][j + 1] >= 0 and j + 1 != depart[1] :
			cheminsAdmissibles.append((i, j + 1))

	#Tester en haut
	if i != 0 : #On regarde si on est au bord
		if labyrinthe[i - 1][j] >= 0 and i - 1 != depart[0] :
			cheminsAdmissibles.append((i - 1, j))

	#Tester en bas
	if i != len(labyrinthe) - 1 : #On regarde si on est au bord
		if labyrinthe[i + 1][j] >= 0 and i + 1 != depart[0] :
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
		prochainChemin = cheminsAdmissibles[randint(0, len(cheminsAdmissibles) - 1)]
		chemin.append(prochainChemin)
		cheminsAdmissibles = cheminsPossibles(labyrinthe, prochainChemin[0], prochainChemin[1], chemin[-2])

	return chemin


def teleportation(labyrinthe : list, Spectre : dict, Joueur : dict) -> None :
	
	"""
	Paramètres
	----------
	
		labyrinthe : matrice du labyrinthe
		Spectre : dictionnaire contenant tous les paramètres du spectre
		Joueur : dictionnaire contenant tous les paramètres du joueur
	
	Procédure qui gère la téléportation du joueur.
	Lorsque appelée, le joueur est replacé aléatoirement dans le labyrinthe.
	Pour ce faire, un nouveau chemin est calculé en partant du Spectre, puis le joueur est mis au bout et l'attribut "chemin" du Spectre set mis à jour.
	"""
	
	#Variables locales pour alléger
	n = len(labyrinthe) // 2
	p = len(labyrinthe[0]) // 2
	iJoueur = Joueur["iJoueur"]
	jJoueur = Joueur["jJoueur"]
	
	#Calcul du chemin
	cheminBrut = trouverLeChemin(labyrinthe, iJoueur, jJoueur)
	#On veut s'assurer que la téléportation emmène assez loin du Spectre
	while len(cheminBrut) < (n + p) // 2 :
		cheminBrut = trouverLeChemin(labyrinthe, iJoueur, jJoueur)
	chemin = []
	#On retourne le chemin pour qu'il aille du Joueur au Spectre, et pas l'inverse
	for i in range(1, len(cheminBrut)) :
		chemin.append(cheminBrut[-i]) #On ommet la dernière case qui correspond à la position du Spectre

	#On met à jour les coordonnées du joueur
	Joueur["iJoueur"] = chemin[0][0]
	Joueur["jJoueur"] = chemin[0][1]
	#On met à jour le chemin du Spectre
	Spectre["chemin"] = chemin

def metAJourSpectre(labyrinthe : list, Spectre : dict, Joueur : dict, jeu : dict, minotaure : dict) -> None :
	
	"""
	Paramètres
	----------
	
		labyrinthe : matrice du labyrinthe
		Spectre : dictionnaire contenant tous les paramètres du spectre
		Joueur : dictionnaire contenant tous les paramètres du joueur
		jeu : dictionnaire contenant toutes les information du jeu en cours
		minotaure : dictionnaire contenant toutes les informations du minotaure
	
	Procédure de mise à jour du Spectre.
	Lorsque appelée, les paramètres du Spectre sont modifiées, en particulier sa position et le chemin le reliant au joueur.
	Par défaut, le Spectre n'a lpas le droit de bouger à chaque appel.
	Le Spectre doit être mis-à-jour APRES le joueur et AVANT le minotaure.
	"""
	
	#Variables locales pour simplifier l'écriture
	iJoueur = Joueur["iJoueur"]
	jJoueur = Joueur["jJoueur"]
	chemin = Spectre["chemin"]
	temps = jeu["referenceTemps"]
	
	#On met à jour la quatité de mouvement du spectre
	
	Spectre["mouvement"] += Spectre["vitesse"]
	
	#On vérifie que le joueur n'est pas à-côté du Spectre
	if len(chemin) > 1 :
		
		#Si le joueur avance vers le Spectre, le chemin devient plus petit
		if (iJoueur, jJoueur) == chemin[1] :
			Spectre["chemin"] = chemin[1 :]
			
		#Sinon le chemin devient plus long (sauf si le joueur reste sur place)
		elif (iJoueur, jJoueur) != chemin[0] :
			Spectre["chemin"] = [(iJoueur, jJoueur)] + chemin
			
		#Ensuite, le spectre avance vers le joueur (s'il a le droit de bouger)
		if Spectre["mouvement"] >= temps :
			Spectre["mouvement"] -= temps
			Spectre["iSpectre"] = chemin[-1][0]
			Spectre["jSpectre"] = chemin[-1][1]
			Spectre["chemin"].pop()

	
	#Dans le cas contraire, le Spectre touche le Joueur, qui est téléporté plus loin
	else :
		Spectre["iSpectre"] = Joueur["iJoueur"]
		Spectre["jSpectre"] = Joueur["jJoueur"]
		teleportation(labyrinthe, Spectre, Joueur)
		minotaure["vitesse"] += 1
	



def afficheSpectre(spectre : dict, brouillard : list, utiliseBrouillard : bool) -> None:
	
	"""
	Paramètres
	----------
		spectre : dictionnaire contenant toutes les informations du spectre
		brouillard : matrice de 0 et de 1 indiquant pour chaque case si elle est nimbée dans le brouillard
		utiliseBrouillard : indique si le brouillard est utilisé ou non
	
	Procédure d'affichage du Spectre dans le labyrinthe
	Celui-ci n'apparaîtra que s'il se trouve sur une case hors du brouillard.
	"""

	iSpectre = spectre["iSpectre"]
	jSpectre = spectre["jSpectre"]

	if not utiliseBrouillard or brouillard[iSpectre][jSpectre] :
		couleur = affichage["spectre"]["couleur"]
		caractere = affichage["spectre"]["caractere"]

		# On doit faire un déccalage de 1 à cause de l'affichage de la bordure
		i = spectre["iSpectre"] + 1
		j = spectre["jSpectre"] + 1

		set_color(couleur)
		print_at_xy(j, i, caractere)

