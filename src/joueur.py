
from random import randint
from my_curses import *

from affichage import *


##
## creeJoueur
##

def creeJoueur(n, p, distanceVue = 4):
	"""
		Type: Fonction
		Paramètre:
			- n: entier, correspond au nombre de lignes contenant des chemins avant la destruction de murs
			- p: entier, correspond au nombre de colonnes contenant des chemins avant la destruction de murs


		Return:
			Un dictionnaire du format d'un joueur
	"""

	joueur = {
		"iJoueur": randint(0, n) * 2,
		"jJoueur": randint(0, p) * 2,
		"distanceVue": distanceVue
	}

	return joueur

##
## 	Update
##

def metAJourJoueur(labyrinthe, joueur, keyPressed):
	"""
		Type: Procédure
		paramètre:
			- labyrinthe: labyrinthe
			- joueur: joueur
			- keyPressed: valeur renvoyée par keypressed()

		Résumé:
			Met à jour le joueur:
				- Met à jour les déplacements du joueur

				TO-DO:
					Ramassage d'objets

	"""
	## Pour une simplification de notation
	nbLignes = len(labyrinthe)
	nbColonnes = len(labyrinthe[0])

	iJoueur = joueur["iJoueur"]
	jJoueur = joueur["jJoueur"]


	## Se déplace vers le bas
	if keyPressed == "s" or keyPressed == "KEY_DOWN":
		if iJoueur + 1 < nbLignes and labyrinthe[iJoueur + 1][jJoueur] >= 0:
			joueur["iJoueur"] += 1

	## Se déplace vers le haut
	elif keyPressed == "z" or keyPressed == "KEY_UP":
		if iJoueur - 1 >= 0 and labyrinthe[iJoueur - 1][jJoueur] >= 0:
			joueur["iJoueur"] -= 1

	## Se déplace vers la gauche
	elif keyPressed == "q" or keyPressed == "KEY_LEFT":
		if jJoueur - 1 >= 0 and labyrinthe[iJoueur][jJoueur - 1] >= 0:
			joueur["jJoueur"] -= 1

	## Se déplace vers la droite
	elif keyPressed == "d" or keyPressed == "KEY_RIGHT":
		if jJoueur + 1 < nbColonnes and labyrinthe[iJoueur][jJoueur + 1] >= 0:
			joueur["jJoueur"] += 1


def afficheJoueur(joueur):
	"""
		Type: procédure
		Paramètres:
			- joueur: type: joueur

		Résumé:
			Affiche le joueur
	"""

	couleur = affichage["joueur"]["couleur"]
	caractere = affichage["joueur"]["caractere"]

	# On doit faire un déccalage de 1 à cause de l'affichage de la bordure
	i = joueur["iJoueur"] + 1
	j = joueur["jJoueur"] + 1

	set_color(couleur)
	print_at_xy(j, i, caractere)



