#!/bin/env python3

from pathlib import Path as p

cheminLivre = p("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")

for l in cheminLivre.iterdir():
    print(l.name)
