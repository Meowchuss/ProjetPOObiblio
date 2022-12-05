#!/bin/env python3

from module import *
from time import time
t0 = time()
bdd = P("/home/meowchuss/bdd livres/livres")
cheminLivre = P("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")
cheminLivre2 = P("/home/meowchuss/Nouveau")
truc = P("/home/meowchuss/bidule")

C = Config(cheminLivre, dossierRapports = truc)
C.startLog()

R = Rapport(cheminLivre, truc)
B1 = R.bibli
temps = int(time() - t0)
print( f"{temps = }")

Rapport2 = Rapport(cheminLivre2, truc, init = False, update = True, ancienneBibli = B1)
temps = int(time() - t0)
print(f"{temps = }")