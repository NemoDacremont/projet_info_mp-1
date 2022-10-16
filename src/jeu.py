
from my_curses import *

from labyrinthe import *
from joueur import *
from brouillard import *

# Donne l'affichage des caractères
from affichage import *


###
### Fonction charge
###

def charge(n, p):
	"""
		Type: Fonction
		paramètres:
			- n: entier, correspond au nombre de lignes contenant des chemins avant la destruction de murs
			- p: entier, correspond au nombre de colonnes contenant des chemins avant la destruction de murs

		Retourne: un dictionnaire au format de jeu
	"""

	nbLignes = 2*n - 1
	nbColonnes = 2*p - 1

	no_delay(True)

	joueur = creeJoueur(n, p)

	game = {
		"labyrinthe": genereLabyrinthe(n, p),
		"brouillard": creeBrouillard(n, p),
		"lignes": nbLignes,
		"colonnes": nbColonnes,
		"utiliseBrouillard": True,
		"isRunning": True,

		"joueur": joueur
	}

	metAJourBrouillard(game["brouillard"], joueur["iJoueur"], joueur["jJoueur"], joueur["distanceVue"])


	return game

###
### Procedure update
###

def update(game):
	"""
		Type: Procédure
		paramètre:
			- game: dictionnaire au format de jeu

		Résumé:
			Met à jour les données du jeu
	"""

	labyrinthe = game["labyrinthe"]
	brouillard = game["brouillard"]
	joueur = game["joueur"]


	keyPressed = keypressed()

	metAJourJoueur(labyrinthe, joueur, keyPressed)

	if keyPressed == "x":
		game["isRunning"] = False

	if keyPressed == "p":
		game["utiliseBrouillard"] = not game["utiliseBrouillard"]

	metAJourBrouillard(brouillard, joueur["iJoueur"], joueur["jJoueur"], joueur["distanceVue"])

###
### Procedure draw
###

def draw(game):
	"""
		Type: Procédure
		paramètre:
			- game: dictionnaire au format de jeu

		Résumé:
			Met à jour l'affichage du jeu

	"""
	clear()

	# copie des variables pour alléger les notations
	brouillard = game["brouillard"]
	labyrinthe = game["labyrinthe"]
	utiliseBrouillard  = game["utiliseBrouillard"]

	afficheBordure(labyrinthe)
	afficheLabryinthe(labyrinthe, brouillard, utiliseBrouillard)

	afficheJoueur(game["joueur"])




def run():
	game = charge(20, 80)

	## On affiche une première fois le jeu
	draw(game)

	while game["isRunning"]:
		update(game)
		draw(game)
		no_delay(False)

