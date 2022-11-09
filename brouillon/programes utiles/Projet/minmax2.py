#!/bin/env python3
import sys, truc

"""
    Soit L le type liste dont les éléments sont soit tous de type int, soit tous de type L.
    Par exemple, l = [ [1,2], [ [2,3,4], [5,4,3,2], [[3,1],[2]]], [0,9] ] est de type L.  

    Ce programme est appelé avec une liste de type L sur la ligne de commande,
    et sort le min des max de ses sous-listes.  

    Avec la liste l ci-dessus, la liste des max est [2, 4, 5, 3, 2, 9] donc le programme sort 2.

    La liste doit être fournie sous la forme : [ [ 1 2 ] [ [ 2 3 4 ] [ 5 4 3 2 ] [ [ 3 1 ] [ 2 ] ] ] [ 0 9 ] ]
"""


def minmax(l):
    """
    Cette fonction récursive retourne le minmax de la liste passée en argument.
    """
    if type(l[0])==int:
        maxi.append(max(l))
    else:
        for i in l:
            minmax(i)

if __name__=="__main__":
    # programme principal
    if len(sys.argv)<2:
        while True:
            line = input("que voulez vous envoyer ? ").rstrip("\n").strip()
            if line=="":
                break
            elif len(line)==1:
                f = open(sys.argv[1], "r")
                for line in f:
                    lline = re.split(r' +',line.rstrip("\n"))
                    l = build(lline)

                    maxi = []
                    minmax(l)
                    print(min(maxi))
            else:
                lline = re.split(r' +',line.rstrip("\n"))
                i = 0
                l = mklist()

                maxi = []
                minmax(l)
                print(min(maxi))
    elif len(sys.argv)==2:
        f = open(sys.argv[1], "r")
        for line in f:
            lline = re.split(r' +',line.rstrip("\n"))
            l = build(lline)

        maxi = []
        minmax(l)
        print(min(maxi))
