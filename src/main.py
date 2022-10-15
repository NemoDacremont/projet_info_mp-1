
import jeu
from my_curses import *

main(jeu.run)
'''
game = jeu.load(10,10)
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
	print(f"[{line}]")






'''