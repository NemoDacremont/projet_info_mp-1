
from labyrinthe import genereLabyrinthe
from my_curses import *

OBJETS = {
	0: {
		"couleur": BLANC,
		"caractere": " "
	},
	-1: {
		"couleur": BLANC,
		"caractere": "1"
	},
	-2: {
		"couleur": BLANC,
		"caractere": "─"
	},
	-3: {
		"couleur": BLANC,
		"caractere": "│"
	},
	-4: {
		"couleur": BLANC,
		"caractere": "┼"
	},
	-5: {
		"couleur": BLANC,
		"caractere": "├"
	},
	-6: {
		"couleur": BLANC,
		"caractere": "┤"
	},
	-7: {
		"couleur": BLANC,
		"caractere": "┬"
	},
	-8: {
		"couleur": BLANC,
		"caractere": "┴"
	},
	-9: {
		"couleur": BLANC,
		"caractere": "└"
	},
	-10: {
		"couleur": BLANC,
		"caractere": "┘"
	},
	-11: {
		"couleur": BLANC,
		"caractere": "┌"
	},
	-12: {
		"couleur": BLANC,
		"caractere": "┐"
	}
}

###
### Procedure load
###

def load(n, p):


	game = {
		"labyrinthe": genereLabyrinthe(n, p),
		"lignes": 2*n - 1,
		"colonnes": 2*p - 1,
		"isRunning": True
	}


	return game

###
### Procedure update
###

def update(game):
	"""
		Met à jour les données du jeu
	"""

	keypressed()
	game["isRunning"] = False

###
### Procedure draw
###

def draw(game):
	"""
		Affiche l'interface
	"""
	clear()

	nbLignes = game["lignes"]
	nbColonne = game["colonnes"]

	##
	## 	Affiche les bordures
	##

	# Affiche les coins
	print_at_xy(0, 0, "┌")
	print_at_xy(0, nbLignes + 1,"└")
	print_at_xy(nbColonne + 1, 0,"┐")
	print_at_xy(nbColonne + 1, nbLignes + 1,"┘")

	# Affiche les colonnes de gauche et droite
	for i in range(nbLignes):
		p = nbColonne + 1
		caractere0 = "│" # caractère sur la première colonne
		caractereP = "│" # caractère sur la colonne p

		if game["labyrinthe"][i][0] < 0:
			caractere0 = "├"
		if game["labyrinthe"][i][-1] < 0:
			caractereP = "┤"

		print_at_xy(0, i+1, caractere0)
		print_at_xy(p, i+1, caractereP)

	# Affiche les lignes du haut et bas
	for j in range(nbColonne):
		n = nbLignes + 1
		caractere0 = "─" # caractère sur la première ligne
		caractereN = "─" # caractère sur la ligne n

		if game["labyrinthe"][0][j] < 0:
			caractere0 = "┬"
		if game["labyrinthe"][-1][j] < 0:
			caractereN = "┴"

		print_at_xy(j+1, 0, caractere0)
		print_at_xy(j+1, n, caractereN)


	##
	##		Affiche le labyrinthe
	##

	for i in range(nbLignes):
		for j in range(nbColonne):
			caractere = OBJETS[ game["labyrinthe"][i][j] ]["caractere"]
			couleur = OBJETS[ game["labyrinthe"][i][j] ]["couleur"]
			#caractere = str(game["labyrinthe"][i][j])

			set_color(couleur)
			print_at_xy(j+1, i+1, caractere)


def run():
	game = load(20, 80)
	draw(game)
	while game["isRunning"]:
		update(game)
		draw(game)

	for i in range(game["lignes"]):

		line = ""
		for j in range(game["colonnes"]):
			line += f"{game['labyrinthe'][i][j]},"
		print(f"[{line}]")





