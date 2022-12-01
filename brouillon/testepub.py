#!/bin/env python3

from epub import open_epub as op
from pathlib import Path as p
from fitz import Document as Doc

cheminLivre = p("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")
bdd = p("/home/meowchuss/bdd livres/livres")

def getToc(filepath: str):
    chapitres = {}
    with Doc(filepath) as doc:
        toc = doc.get_toc()  # [[lvl, title, page, …], …]
        for title, page in toc:
            chapitres[page] = title
    return chapitres
for livre in cheminLivre.iterdir():
    with Doc(livre) as doc:
        titre = doc.metadata["title"]
        auteur = doc.metadata["author"]
        langue = "o"
        print(f"{titre = }\n{auteur = }\n")
        print()