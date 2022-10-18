
from my_curses import *

from labyrinthe import *
from joueur import *
from brouillard import *
from ennemis.spectre import *

from utils import selectionneCaseAleatoire

# Donne l'affichage des caractères
from objets.objets import *


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

	labyrinthe = genereLabyrinthe(n, p)
	brouillard = creeBrouillard(n, p)

	joueur, depart = creeJoueur(labyrinthe)
	iDepart = depart["i"]
	jDepart = depart["j"]
	
	spectre = creeSpectre(labyrinthe, joueur)
	
	iArrivee, jArrivee = selectionneCaseAleatoire(labyrinthe)

	labyrinthe[iArrivee][jArrivee] = 5
	labyrinthe[iDepart][jDepart] = 4

	arrivee = {
		"i": iArrivee,
		"j": jArrivee
	}

	objets = creeObjets(labyrinthe, joueur)

	game = {
		"brouillard": brouillard,
		"utiliseBrouillard": True,

		"labyrinthe": labyrinthe,
		"lignes": nbLignes,
		"colonnes": nbColonnes,

		"isRunning": True,
		"gagne": False,

		"objets": objets,

		"joueur": joueur,
		"spectre" : spectre,
		"depart": depart,
		"arrivee": arrivee
	}

	metAJourBrouillard(game["brouillard"], joueur, joueur["distanceVue"])


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
	objets = game["objets"]

	spectre = game["spectre"]

	arrivee = game["arrivee"]


	keyPressed = keypressed()

	metAJourJoueur(labyrinthe, joueur, keyPressed)

	if keyPressed == "x":
		game["isRunning"] = False

	if keyPressed == "p":
		game["utiliseBrouillard"] = not game["utiliseBrouillard"]

	metAJourSpectre(labyrinthe, spectre, joueur)

	metAJourObjets(objets, labyrinthe, joueur)

	brouillardEstPersistant = joueur["brouillardEstPersistant"]

	metAJourBrouillard(brouillard, joueur, joueur["distanceVue"], brouillardEstPersistant)

	if joueur["iJoueur"] == arrivee["i"] and joueur["jJoueur"] == arrivee["j"]:
		game["gagne"] = True

###
### Procedure draw
###

def affichage(game):
	"""
		Type: Procédure
		paramètre:
			- game: dictionnaire au format de jeu

		Résumé:
			Met à jour l'affichage du jeu

	"""
	clear()

	if not game["gagne"]:
		# copie des variables pour alléger les notations
		brouillard = game["brouillard"]
		labyrinthe = game["labyrinthe"]
		utiliseBrouillard  = game["utiliseBrouillard"]
		objets = game["objets"]
		spectre = game["spectre"]

		afficheBordure(labyrinthe)
		afficheLabryinthe(labyrinthe, brouillard, utiliseBrouillard)

		afficheSpectre(spectre)


		## Affiche le joueur
		afficheJoueur(game["joueur"])

	else:
		print_str("You win.")

##
## Procédure Run
##

def run():
	"""
		Type: Procedure

		Résumé:
			Lance réellement le jeu
	"""

	game = charge(16, 75)

	## On affiche une première fois le jeu
	affichage(game)

	while game["isRunning"]:
		update(game)
		affichage(game)
		no_delay(False)

