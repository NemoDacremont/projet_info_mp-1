
from objets.casqueObservation import *
from objets.carte import *
from objets.bottesDeSeptLieux import *

from random import randint

NB_MAX_CASQUES = 2
NB_MAX_BOTTES = 2
NB_MAX_CARTES = 1

def creeObjets(labyrinthe: list, joueur: dict):
	"""
	"""
	objets = []

	## Cree les casques
	nbCasques = randint(1, NB_MAX_CASQUES)
	for i in range(nbCasques):
		objets.append(creeCasque(labyrinthe, joueur))

	## Cree les cartes
	nbCartes = randint(1, NB_MAX_CARTES)
	for i in range(nbCartes):
		objets.append(creeCarte(labyrinthe, joueur))

	## Cree les bottes
	nbBottes = randint(1, NB_MAX_BOTTES)
	for i in range(nbBottes):
		objets.append(creeBottes(labyrinthe, joueur))

	return objets

def utiliseObjet(objet: dict, game: dict):
	"""
	"""
	i = objet["i"]
	j = objet["j"]
	labyrinthe = game["labyrinthe"]
	joueur = game["joueur"]

	if objet["id"] == 50:
		utiliseCasque(joueur)
	elif objet["id"] == 51:
		utiliseCarte(joueur)
	elif objet["id"] == 52:
		utiliseBottes(joueur, game)

	#labyrinthe[i][j] = 0

def metAJourObjets(objets: list, game: dict):
	"""
	"""
	labyrinthe = game["labyrinthe"]
	joueur = game["joueur"]

	iJoueur = joueur["iJoueur"]
	jJoueur = joueur["jJoueur"]


	for k in range(len(objets)):
		objet = objets[k]
		iObjet =  objet["i"]
		jObjet =  objet["j"]

		if iObjet == iJoueur and jObjet == jJoueur:
			utiliseObjet(objet, game)
			objets.pop(k)
			labyrinthe[iObjet][jObjet] = 0
			return


