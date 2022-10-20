from random import randint
from ennemis.pathfinding import *
from affichage import *

"""
Module régissant le Minotaure
-----------------------------

Le Minotaure est un monstre qui apparaît au centre du labyrinthe.
Extrêmement lent, il traque le joueur en passant à-travers les murs
(sans quoi il serait souvent impossible de lui échapper).

S'il parvient à toucher le joueur, celui-ci perd la partie.
Chaque fois que le Spectre (cf spectre.py) touche le joueur, le Minotaure accélère.
"""

def creeMinotaure(labyrinthe : list) -> dict :
	
	"""
	Paramètres
	----------
		labyrinthe : matrice du labyrinthe
	
	Return
	------
		dictionnaire contenant toutes les informations du Minotaure
		
	"""
	#Dimensions du demi-labyrinthe (nombres de cases sans les murs)
	n, p = len(labyrinthe) // 4, len(labyrinthe[0]) // 4
	#On s'assure que le numéro de case soit pair (pour ne pas être sur un mur)
	n *= 2
	p *= 2

	minotaure = {
		"ID" : 100,
		"iMinotaure" : n,
		"jMinotaure" : p,
		"mouvement" : 1,
		"vitesse" : 1
		}

	return minotaure

def traquerLeJoueur(minotaure : dict, joueur : dict) -> None :
	"""
	
	Paramètres
	----------
		minotaure : dictionnaire contenant toutes les informations du minotaure
		joueur : dictionnaire contenant toutes les informations du joueur
	
	Procédure qui permet de déplacer le Minotaure de façon à toujours le rapprocher du joueur.
	Le Minotaure se déplace en ignorant les murs : en conséquence il calcule juste le chemin le plus direct, "à vol d'oiseau"

	"""
	
	iJoueur = joueur["iJoueur"]
	jJoueur = joueur["jJoueur"]
	iMinotaure = minotaure["iMinotaure"]
	jMinotaure = minotaure["jMinotaure"]
	
	#Calcul de la trajectoire
	
	iDifference = iJoueur - iMinotaure
	jDifference = jJoueur - jMinotaure
	
	#Décision du mouvement
	
	if abs(iDifference) >= abs(jDifference) :
		if iDifference < 0 :
			minotaure["iMinotaure"] += -1
		else :
			minotaure["iMinotaure"] += 1
	else :
		if jDifference < 0 :
			minotaure["jMinotaure"] += -1
		else :
			minotaure["jMinotaure"] += 1


def metAJourMinotaure(jeu : dict, minotaure : dict, joueur : dict) -> None :
	
	"""
	Paramètres
	----------
		jeu : dictionnaire contenant tous les paramètres du jeu
		minotaure : dictionnaire contenant toutes les informations du minotaure
		joueur : dictionnaire contenant toutes les informations du joueur
		
	Procédure de mise à jour du Minotaure.
	"""
	
	temps = jeu["referenceTemps"]
	
	#On met à jour la quantité de mouvement du minotaure
	minotaure["mouvement"] += minotaure["vitesse"]
	
	#On test si on est sur le joueur
	if minotaure["iMinotaure"] == joueur["iJoueur"] and minotaure["jMinotaure"] == joueur["jJoueur"] :
		jeu["perdre"] = True

	elif minotaure["mouvement"] >= temps :
		traquerLeJoueur(minotaure, joueur)
		minotaure["mouvement"] -= temps



def afficheMinotaure(minotaure : dict, brouillard : list, utiliseBrouillard : bool) -> None :
	
	"""
	Paramètres
	----------
		mintoaure : dictionnaire contenant toutes les informations du minotaure
		brouillard : matrice de 0 et de 1 marquant le brouillard sur le labyrinthe
		utiliseBrouillard : vaut True si le brouillard est actif
	
	Procédure d'affichage du minotaure
	"""

	iMinotaure = minotaure["iMinotaure"]
	jMinotaure = minotaure["jMinotaure"]

	if not utiliseBrouillard or brouillard[iMinotaure][jMinotaure] :
		couleur = affichage["minotaure"]["couleur"]
		caractere = affichage["minotaure"]["caractere"]

		# On doit faire un déccalage de 1 à cause de l'affichage de la bordure
		i = minotaure["iMinotaure"] + 1
		j = minotaure["jMinotaure"] + 1

		set_color(couleur)
		print_at_xy(j, i, caractere)
