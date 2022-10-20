
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

	no_delay(True)

	## Initialise les différents objets utilisés
	labyrinthe = genereLabyrinthe(n, p)
	brouillard = creeBrouillard(n, p)

	# Joueur ainsi que le départ et arrivée
	joueur, depart = creeJoueur(labyrinthe)
	iDepart = depart["i"]
	jDepart = depart["j"]

	iArrivee, jArrivee = selectionneCaseAleatoire(labyrinthe)
	arrivee = {
		"i": iArrivee,
		"j": jArrivee
	}

	labyrinthe[iArrivee][jArrivee] = 5
	labyrinthe[iDepart][jDepart] = 4

	# Ennemis
	spectre = creeSpectre(labyrinthe, joueur)
	minotaure = creeMinotaure(labyrinthe)

	# Objet
	objets = creeObjets(labyrinthe, joueur)

	## Correspond à la variable principale du jeu stockant toutes les informations
	game = {
		# état du jeu
		"isRunning": True,
		"gagne": False,
		"perdre" : False,

		"referenceTemps" : 10,
		"compteurMouvementsJoueurs" : 0,
		"accelerationSpectre" : 10,

		"depart": depart,
		"arrivee": arrivee,

		# structures du jeu
		"brouillard": brouillard,
		"utiliseBrouillard": True,

		"labyrinthe": labyrinthe,


		# entités
		"joueur": joueur,

		"objets": objets,

		"spectre" : spectre,
		"minotaure" : minotaure,
		"depart": depart,
		"arrivee": arrivee,

		"referenceTemps" : max(joueur["vitesse"], spectre["vitesse"], minotaure["vitesse"]),

	}

	# On met une première fois à jour le brouillard, permet de donner la vision autour du joueur au départ
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

	## Pour une simplification de notation, on fait des copies locales des variables
	labyrinthe = game["labyrinthe"]
	brouillard = game["brouillard"]
	joueur = game["joueur"]
	objets = game["objets"]
	spectre = game["spectre"]
	minotaure = game["minotaure"]
	arrivee = game["arrivee"]
	
	## Mise à jour de la référence des temps
	game["referenceTemps"] = max(joueur["vitesse"], spectre["vitesse"], minotaure["vitesse"])

	## Récupération de l'entrée (avec une valeur défaut lorsque le joueur ne joue pas)
	if joueur["mouvement"] >= game["referenceTemps"] :
		keyPressed = keypressed()

	## Traitement de l'entrée (si le joueur a la vitesse pour jouer)
	# On traite d'abord ce qui correspond à la mise à jour du jeu
		if keyPressed == "x":
			game["isRunning"] = False

		elif keyPressed == "p":
			game["utiliseBrouillard"] = not game["utiliseBrouillard"]
		
		
		metAJourJoueur(labyrinthe, joueur, game["referenceTemps"], keyPressed)

	# Joueur
	joueur["mouvement"] += joueur["vitesse"]

	# Mise à jour des ennemis APRES le joueur
	metAJourSpectre(labyrinthe, spectre, joueur, game, minotaure)
	metAJourMinotaure(game, minotaure, joueur)

	# Objet, c'est ici que la récupération d'objets est faite
	metAJourObjets(objets, game)

	## Accélération du spectre en fonction du nombre 
	game["compteurMouvementsJoueurs"] += 1

	if game["compteurMouvementsJoueurs"] >= game["accelerationSpectre"] :

		game["spectre"]["vitesse"] += 1
		game["compteurMouvementsJoueurs"] %= game["accelerationSpectre"]


	## Finalement, on met le brouillard à jour
	# valeur stockée dans joueur car est dépendante de la possession de l'objet "Carte"
	brouillardEstPersistant = joueur["brouillardEstPersistant"]

	metAJourBrouillard(brouillard, joueur, joueur["distanceVue"], brouillardEstPersistant)

	# et on teste si le joueur à gagné ou non, ie il se trouve sur la case d'arrivée
	if joueur["iJoueur"] == arrivee["i"] and joueur["jJoueur"] == arrivee["j"]:
		game["gagne"] = True

###
### Procedure affichage
###

def affichage(game):
	"""
		Type: Procédure
		paramètre:
			- game: dictionnaire au format de jeu

		Résumé:
			Met à jour l'affichage du jeu

	"""
	# on efface l'affichage précédent
	clear()

	# copie des variables pour alléger les notations
	brouillard = game["brouillard"]
	labyrinthe = game["labyrinthe"]
	utiliseBrouillard  = game["utiliseBrouillard"]
	objets = game["objets"]
	spectre = game["spectre"]
	minotaure = game["minotaure"]



	if game["perdre"] :
		print_str("You loose.")

	elif game["gagne"]:
		print_str("You win.")

	else:
		# affiche le labyrinthe
		afficheBordure(labyrinthe)
		afficheLabryinthe(labyrinthe, brouillard, utiliseBrouillard)

		## Affiche le joueur
		afficheJoueur(game["joueur"])

		## Affiche les ennemis
		afficheSpectre(spectre, brouillard, utiliseBrouillard)
		afficheMinotaure(minotaure, brouillard, utiliseBrouillard)


##
## Procédure Run
##

def run():
	"""
		Type: Procedure

		Résumé:
			Lance réellement le jeu, procédure contenant la boucle principale du programme
	"""

	game = charge(16, 75)

	## On affiche une première fois le jeu
	affichage(game)

	while game["isRunning"]:
		update(game)
		affichage(game)
		no_delay(False)

