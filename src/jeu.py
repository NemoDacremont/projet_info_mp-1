
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

	text = ""
	for i in range(game["lignes"]):
		line = ""
		for j in range(game["colonnes"]):
			n = game['labyrinthe'][i][j]
			if n < -9:
				line += f"{game['labyrinthe'][i][j]},"
			elif n < -0:
				line += f"0{game['labyrinthe'][i][j]},"
			else:
				line += f"00{game['labyrinthe'][i][j]},"
		text += f"{line}\n"

	with open("./out", "a") as file:
		file.write(text)
		file.write("----------------------------------------------\n")


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

	for i in range(game["lignes"]):
		for j in range(game["colonnes"]):
			caractere = OBJETS[ game["labyrinthe"][i][j] ]["caractere"]
			couleur = OBJETS[ game["labyrinthe"][i][j] ]["couleur"]
			#caractere = str(game["labyrinthe"][i][j])

			set_color(couleur)
			print_at_xy(j, i, caractere)


def run():
	game = load(19, 76)
	draw(game)
	while game["isRunning"]:
		update(game)
		draw(game)

	for i in range(game["lignes"]):

		line = ""
		for j in range(game["colonnes"]):
			line += f"{game['labyrinthe'][i][j]},"
		print(f"[{line}]")





