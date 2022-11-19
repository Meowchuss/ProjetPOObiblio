#!/bin/env python3

from epub import open_epub as op
from pathlib import Path as p

cheminLivre = p("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")
epub = []
for l in cheminLivre.iterdir():
    if l.suffix == ".epub":
        epub.append(l)

epub = op(epub[0])


print(epub.toc.title)