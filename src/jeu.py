
from my_curses import *

from labyrinthe import *
from joueur import *
from brouillard import *
from ennemis.spectre import *
from ennemis.minotaure import *

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
	minotaure = creeMinotaure(labyrinthe)

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
		"perdre" : False,

		"objets": objets,

		"joueur": joueur,
		"spectre" : spectre,
		"minotaure" : minotaure,
		"depart": depart,
		"arrivee": arrivee,

		"referenceTemps" : 10,
		"mouvement" : 0,
		"vitesseSpectre" : 300
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
	
	#Mise à jour des monstres APRES le joueur
	spectre = game["spectre"]
	minotaure = game["minotaure"]

	arrivee = game["arrivee"]


	keyPressed = keypressed()

	metAJourJoueur(labyrinthe, joueur, keyPressed, game["referenceTemps"])

	if keyPressed == "x":
		game["isRunning"] = False

	if keyPressed == "p":
		game["utiliseBrouillard"] = not game["utiliseBrouillard"]
		

	metAJourSpectre(labyrinthe, spectre, joueur, game, minotaure)
	metAJourMinotaure(game, minotaure, joueur)

	metAJourObjets(objets, game)
	
	game["mouvement"] += 1
	
	if game["mouvement"] >= game["vitesseSpectre"] :
		game["spectre"]["vitesse"] += 1
		game["mouvement"] = 0

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

	if not game["gagne"] and not game["perdre"]:
		# copie des variables pour alléger les notations
		brouillard = game["brouillard"]
		labyrinthe = game["labyrinthe"]
		utiliseBrouillard  = game["utiliseBrouillard"]
		objets = game["objets"]
		spectre = game["spectre"]
		minotaure = game["minotaure"]

		afficheBordure(labyrinthe)
		afficheLabryinthe(labyrinthe, brouillard, utiliseBrouillard)
		
		afficheSpectre(spectre, brouillard, utiliseBrouillard)
		afficheMinotaure(minotaure, brouillard, utiliseBrouillard)
		
		


		## Affiche le joueur
		afficheJoueur(game["joueur"])
	
	elif game["perdre"] :
		print_str("You loose.")
		
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

