#!/bin/env python3
import sys, re

"""
    Soit L le type liste dont les éléments sont soit tous de type int, soit tous de type L.

    Ce programme lit des liste de type L sur l'entrée standard, au format
    [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
    et sort cette liste dans laquelle les sous-listes d'entiers sont triées.  
"""

def tri(l):
    """
    Cette fonction récursive tri la liste passée en argument.
    """
    if type(l[0])==int:
        l.sort()
    else:
        for i in l:
            tri(i)

def mklist():
    global i
    l = []          # liste courante
    while True:
        if lline[i]=="[":   # c'est une liste de listes
            i+=1                 # argument suivant
            if i!=1:             # pour la première liste, on ne fait rien
                l.append(mklist())    # sinon on construit cette sous-liste et on la met dans la liste courante
        elif lline[i]=="]": # c'est la fin de la liste,
            i+=1
            return l             # on renvoie la liste courante
        else:                  # c'est une liste d'entiers
            l.append(int(lline[i]))   
            i+=1

if __name__=="__main__":
    # programme principal
    while True:
        line = input("? ").rstrip("\n").strip()
        if line=="":
            break
        lline = re.split(r' +',line.rstrip("\n"))
        i = 0
        l = mklist()                      # récupération de la liste
        tri(l)
        print(f"{l=}")
