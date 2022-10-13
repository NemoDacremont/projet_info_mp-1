
from random import randint

def genereCase(i: int, j: int, n: int, p: int) -> int:
	# Intersection mur
	if i%2==1 and j%2==1:
		return -2

	# Mur
	if i%2==(j+1)%2:
		return -1
	
	# chemin
	if i%2==0 and j%2==0:
		return i*p + j

	return -5


def genererLabyrintheBrut(n: int, p: int) -> list[list[int]]:
	"""
		n: nombre de lignes du labyrinthe
		p: nombre
		Génère un labyrinthe de dimension n*p
	"""

	colonnes = p*2 -1
	lignes = n*2 -1

	lab = [[genereCase(i, j, lignes, colonnes) for j in range(colonnes)] for i in range(lignes)]

	return lab

def genereLabyrinthe(n: int, p: int) -> list[list[int]]:
	labyrinthe = genererLabyrintheBrut(n, p)

	for i in range(n*p - 1):
		percerUnMur(labyrinthe, n, p)


	return lab

lab = genererLabyrintheBrut(5, 5)
for i in range(len(lab)):
	line = ""
	for j in range(len(lab[0])):
		line += f"{lab[i][j]},"
	print(f"[{line}]")
