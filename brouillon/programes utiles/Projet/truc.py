#!/bin/env python3
import sys, re

def construire():
    #Prend les arguments du shell, si ils sont de la forme liste de l'énoncé, retourne une liste python
    def _construire():
        """
        Cette fonction récursive construit la liste 
        à partir des arguments fournis sur la ligne de commande.
        Elle retourne la liste construite.
        """

        nonlocal i  
        l = []          
        while True:
            if sys.argv[i]=="[":   
                i+=1               
                if i!=2:                  # pour la première liste, on ne fait rien
                    l.append(_construire()) 
            elif sys.argv[i]=="]":        # c'est la fin de la liste,
                i+=1
                return l                  # on renvoie la liste constuite
            else:                         # c'est une liste d'entiers
                l.append(int(sys.argv[i]))   
                i+=1
    i = 1                              # indice pour parcourir les arguments
    return _construire()

def mklist():
    #En initialisant un i=0 global, lit les caractères issus d'un input nommé "lline = re.split(r' +',line.rstrip("\n"))" pour en faire une liste python
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

def build(l0):
    #Pareil que mklist mais avec une ligne de fichier en argument
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