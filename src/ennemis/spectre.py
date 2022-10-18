from random import randint
from ennemis.pathfinding import *
from affichage import *

def creeSpectre(labyrinthe : list, joueur : dict) -> dict :

	"""
	Pramètres :
		labyrinthe : matrice du labyrinthe considéré
		joueur : dictionnaire contenant les informations du joueur

	Return :
		Dictionnaire au format d'un Spectre

	Remarques : le Spectre va poursuivre le joueur, son dictionnaire contient donc le chemin qui le relie au joueur.
	Plutôt que de générer ses coordonnées aléatoirement, on génère un chemin depuis le joueur et on place le Spectre au bout.
	Le déplacement sera ainsi très facile à calculer en exploitant l'acyclicité du labyrinthe.
	"""

	#Dimensions du labyrinthes (nombres de cases sans les murs)
	n, p = len(labyrinthe) // 2, len(labyrinthe[0]) // 2

	#Coordonnées du joueur (pour que le monstre n'apparaisse pas à-côté)
	iJoueur = joueur["iJoueur"]
	jJoueur = joueur["jJoueur"]

	#Trouver le chemin qui reliera le joueur au Spectre
	chemin = trouverLeChemin(labyrinthe, iJoueur, jJoueur)
	#Le Spectre ne doit pas être trop proche du joueur
	while len(chemin) < (n + p) // 2 :
		chemin = trouverLeChemin(labyrinthe, iJoueur, jJoueur)

	#On récupère les coordonnées du spectre au bout du chemin et on retire sa position
	iSpectre, jSpectre = chemin.pop()

	Spectre = {
		"ID" : 101,
		"iSpectre" : iSpectre,
		"jSpectre" : jSpectre,
		"chemin" : chemin,
		"mouvement" : 0}

	return Spectre

def teleportation(labyrinthe : list, Spectre : dict, Joueur : dict) -> None :
	iJoueur = Joueur["iJoueur"]
	jJoueur = Joueur["jJoueur"]
	cheminBrut = trouverLeChemin(labyrinthe, iJoueur, jJoueur)
	chemin = []
	#On retourne le chemin pour qu'il aille du Joueur au Spectre, et pas l'inverse
	for i in range(1, len(cheminBrut)) :
		chemin.append(cheminBrut[-i]) #On ommet la dernière case qui correspond à la position du Spectre

	#On met à jour les coordonnées du joueur
	Joueur["iJoueur"] = chemin[0][0]
	Joueur["jJoueur"] = chemin[0][1]
	#On met à jour le chemin du Spectre
	Spectre["chemin"] = chemin

def metAJourSpectre(labyrinthe : list, Spectre : dict, Joueur : dict) -> None :
	iJoueur = Joueur["iJoueur"]
	jJoueur = Joueur["jJoueur"]
	chemin = Spectre["chemin"]
	#On vérifie que le joueur n'est pas à-côté du Spectre
	if len(chemin) > 1 :
		
		#Si le joueur avance vers le Spectre, le chemin devient plus petit
		if (iJoueur, jJoueur) == chemin[1] :
			Spectre["chemin"] = chemin[1 :]
		#Sinon le chemin devient plus long
		#Et on test également si le joueur reste sur place
		elif (iJoueur, jJoueur) != chemin[0] :
			Spectre["chemin"] = [(iJoueur, jJoueur)] + chemin
		#Ensuite, le sepctre avance vers le joueur (s'il a le droit de bouger)
		if Spectre["mouvement"] % 3 == 0 :
			Spectre["iSpectre"] = chemin[-1][0]
			Spectre["jSpectre"] = chemin[-1][1]
			Spectre["chemin"].pop()
		
	#Dans le cas contraire, le Spectre touche le Joueur, qui est téléporté plus loin
	else :
		Spectre["iSpectre"] = Joueur["iJoueur"]
		Spectre["jSpectre"] = Joueur["jJoueur"]
		teleportation(labyrinthe, Spectre, Joueur)
	
	#Enfin, on met à jour la variable de mouvement
	Spectre["mouvement"] += 1
	

def afficheSpectre(spectre : dict, brouillard, utiliseBrouillard) -> None:
	
	iSpectre = spectre["iSpectre"]
	jSpectre = spectre["jSpectre"]
	
	if not utiliseBrouillard or brouillard[iSpectre][jSpectre] :
		couleur = affichage["spectre"]["couleur"]
		caractere = affichage["spectre"]["caractere"]

		# On doit faire un déccalage de 1 à cause de l'affichage de la bordure
		i = spectre["iSpectre"] + 1
		j = spectre["jSpectre"] + 1

		set_color(couleur)
		print_at_xy(j, i, caractere)

