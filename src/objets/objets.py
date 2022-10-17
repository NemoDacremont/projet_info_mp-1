
from objets.casqueObservation import *
from objets.carte import *
from random import randint

NB_MAX_CASQUES = 1
NB_MAX_CARTES = 1

def creeObjets(labyrinthe: list, joueur: dict):
	"""
	"""
	objets = []

	## Cree les casques
	nbCasques = randint(0, NB_MAX_CASQUES)
	for i in range(nbCasques):
		objets.append(creeCasque(labyrinthe, joueur))

	## Cree les cartes
	nbCartes = randint(0, NB_MAX_CARTES)
	for i in range(nbCartes):
		objets.append(creeCarte(labyrinthe, joueur))

	return objets

def utiliseObjet(objet: dict, labyrinthe: list, joueur: dict):
	"""
	"""
	i = objet["i"]
	j = objet["j"]

	if objet["id"] == 50:
		utiliseCasque(joueur)
	elif objet["id"] == 51:
		utiliseCarte(joueur)

	labyrinthe[i][j] = 0

def metAJourObjets(objets: list, labyrinthe: list, joueur: dict):
	"""
	"""
	iJoueur = joueur["iJoueur"]
	jJoueur = joueur["jJoueur"]


	for k in range(len(objets)):
		objet = objets[k]
		iObjet =  objet["i"]
		jObjet =  objet["j"]

		if iObjet == iJoueur and jObjet == jJoueur:
			utiliseObjet(objet, labyrinthe, joueur)
			objets.pop(k)
			labyrinthe[iObjet][jObjet] = 0
			return


