#!/usr/bin/env python3

import curses
from curses import wrapper

# Quelques constantes pour les couleurs et les attributs affichés
BLANC = 1
VERT = 2
BLEU = 3
ROUGE = 4
NOIR = 5
JAUNE = 6
MAGENTA = 7
CYAN = 8


A_INVERSE = curses.A_REVERSE
A_GRAS = curses.A_BOLD
A_CLIGNOTANT = curses.A_BLINK
A_MOYEN = curses.A_DIM
A_FORT = curses.A_STANDOUT
A_SOULIGNE = curses.A_UNDERLINE

attribut = curses.A_BOLD

scr = None

def gotoxy(x,y):
    scr.move(y,x)

def print_char(c):
    scr.addstr(c,attribut + curses.color_pair(color))

def set_attribut(attr):
    global attribut
    attribut = attr

def set_color(couleur):
    global color
    color = couleur

def print_str(s):
    scr.addstr(s)

def print_at_xy(x,y,s):
    scr.addstr(y,x,s,attribut + curses.color_pair(color))

def no_delay(yes = True):
    scr.nodelay(yes)

def readkey():
    return(scr.getkey())

def keypressed():
    """Renvoie None si aucune touche n'est appuyée, la touche sinon."""
    try:
        k = scr.getkey()
        return(k)
    except:
        return(None)

def clear():
    scr.clear()

def clrtoeol():
    scr.clrtoeol()

def refresh():
    scr.refresh()

def get_maxyx():
    y,x = scr.getmaxyx()
    return(y,x)
    
def principal(stdscr,la_procedure):
    global scr, attribut, color

    scr = stdscr  # On mémorise l'écran pour les fonctions gotoxy et cie...
    scr.clear()

    curses.curs_set(0) # curseur invisible

    curses.init_pair(1,curses.COLOR_WHITE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(4,curses.COLOR_RED,curses.COLOR_BLACK)
    curses.init_pair(5,curses.COLOR_BLACK,curses.COLOR_BLACK)
    curses.init_pair(6,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    curses.init_pair(7,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    curses.init_pair(8,curses.COLOR_CYAN,curses.COLOR_BLACK)

    color = BLANC

    la_procedure()



def main(procedure):    
    wrapper(principal,procedure)


###################################################################

if __name__ == '__main__':
    print("Ce programme n'est pas destiné à être exécuté...")
