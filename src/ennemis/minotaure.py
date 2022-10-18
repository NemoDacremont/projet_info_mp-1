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


def metAJourMinotaure(jeu : dict, minotaure : dict, joueur : dict) :
	mouvement = minotaure["mouvement"]
	temps = jeu["referenceTemps"]
	#On test si on est sur le joueur
	if minotaure["iMinotaure"] == joueur["iJoueur"] and minotaure["jMinotaure"] == joueur["jJoueur"] :
		jeu["perdre"] = True
	
	elif mouvement >= temps :
		traquerLeJoueur(minotaure, joueur)
		minotaure["mouvement"] %= temps
	
	minotaure["mouvement"] += 1
	
def afficheMinotaure(minotaure : dict, brouillard, utiliseBrouillard) -> None:
	
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
