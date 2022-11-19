#!/bin/env python3
import sys, re

"""
    Soit L le type liste dont les éléments sont soit tous de type int, soit tous de type L.
    Ce programme est appelé avec le nom d'un fichier sur la ligne de commande,
    ce fichier contenant des listes de type L.
    Il sort la profondeur de chaque liste.
"""
def build(l0):
    """
    Cette fonction construit la liste correspondant à sa représentation chaine de caractère fourni en argument.
    """

    def _build():
        nonlocal i
        l = []          # sous-liste courante
        while True:
            if l0[i]=="[":   # c'est une sous-liste de listes
                i+=1                 
                if i!=1:             # pour la première sous-liste, on ne fait rien
                    l.append(_build())    # sinon on construit cette sous-liste et on la met dans la sous-liste courante
            elif l0[i]=="]": # c'est la fin de la sous-liste courante,
                i+=1
                return l             # on renvoie la sous-liste courante
            else:                  # c'est une sous-liste d'entiers
                l.append(int(l0[i]))   
                i+=1
    i = 0
    res = _build()
    return res

def profondeur(l):
    """
    Cette fonction renvoie la profondeur de la liste passée en argument.
    """

    def _profondeur(l,p):
        nonlocal prof
        for i in l:
            if type(i)==int:
                if p>prof:
                    prof = p
            else:
                _profondeur(i,p+1)

    prof=float("-inf")
    _profondeur(l,1)
    return(prof)

if __name__=="__main__":
    # programme principal
    f = open(sys.argv[1], "r")
    for line in f:
        lline = re.split(r' +',line.rstrip("\n"))
        l = build(lline)                     
        print(f"{l=}")
        print(f"{profondeur(l)=}")
