
from random import randint
from my_curses import *
from objets.objets import utiliseObjet

from utils import selectionneCaseAleatoire

from affichage import *


##
## creeJoueur
##

def creeJoueur(labyrinthe: list, distanceVue = 4):
	"""
		Type: Fonction
		Paramètre:
			- n: entier, correspond au nombre de lignes contenant des chemins avant la destruction de murs
			- p: entier, correspond au nombre de colonnes contenant des chemins avant la destruction de murs

		Return:
			Un dictionnaire du format d'un joueur
	"""

	iJoueur, jJoueur = selectionneCaseAleatoire(labyrinthe)

	joueur = {
		"iJoueur": iJoueur,
		"jJoueur": jJoueur,
		"distanceVue": distanceVue,
		"brouillardEstPersistant": False,
		"vitesse": 10,
		"mouvement": 0,
		"godmode": False
	}

	depart = {
		"i": iJoueur,
		"j": jJoueur
	}

	return joueur, depart

##
## 	Mise à jour
##

def metAJourJoueur(labyrinthe, joueur, keyPressed, referenceTemps):
	"""
		Type: Procédure
		paramètre:
			- labyrinthe: labyrinthe
			- joueur: joueur
			- keyPressed: valeur renvoyée par keypressed()

		Résumé:
			Met à jour le joueur:
				- Met à jour les déplacements du joueur

	"""

	## Pour une simplification de notation, on fait des copies locales des variables
	nbLignes = len(labyrinthe)
	nbColonnes = len(labyrinthe[0])

	iJoueur = joueur["iJoueur"]
	jJoueur = joueur["jJoueur"]
	godmode = joueur["godmode"]


	# On calcule la quantité de mouvement permettant de déterminer si il peut se déplacer
	joueur["mouvement"] += joueur["vitesse"]

	# Si le joueur n'avait pas assez de vitesse, il ne joue pas
	if joueur["mouvement"] < referenceTemps:
		return

	joueur["mouvement"] = joueur["mouvement"] % referenceTemps


	## Gestion des entrées utilisateurs

	# Dictionnaire permettant de facilement gérer les touches
	controles = {
		"droite": ["d", "D", "KEY_RIGHT"],
		"gauche": ["q", "Q", "KEY_LEFT"],
		"haut": ["z", "Z", "KEY_UP"],
		"bas": ["s", "S", "KEY_DOWN"],
		"godMode": ["g", "G"]
	}

	## Se déplace vers le bas
	if keyPressed in controles["bas"]:
		if iJoueur + 1 < nbLignes and (labyrinthe[iJoueur + 1][jJoueur] >= 0 or godmode):
			joueur["iJoueur"] += 1

	## Se déplace vers le haut
	elif keyPressed in controles["haut"]:
		if iJoueur - 1 >= 0 and (labyrinthe[iJoueur - 1][jJoueur] >= 0 or godmode):
			joueur["iJoueur"] -= 1

	## Se déplace vers la gauche
	elif keyPressed in controles["gauche"]:
		if jJoueur - 1 >= 0 and (labyrinthe[iJoueur][jJoueur - 1] >= 0 or godmode):
			joueur["jJoueur"] -= 1

	## Se déplace vers la droite
	elif keyPressed in controles["droite"]:
		if jJoueur + 1 < nbColonnes and (labyrinthe[iJoueur][jJoueur + 1] >= 0 or godmode):
			joueur["jJoueur"] += 1


	## Godmode, permet de passer à travers les murs
	if keyPressed in controles["godMode"]:
		joueur["godmode"] = not godmode


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

	# On doit faire un décalage de 1 à cause de l'affichage de la bordure
	i = joueur["iJoueur"] + 1
	j = joueur["jJoueur"] + 1

	set_color(couleur)
	print_at_xy(j, i, caractere)



