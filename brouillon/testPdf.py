#!/bin/env python3

from pathlib import Path as p
from PyPDF2 import PdfReader as Pr

cheminLivre = p("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")
pdf = []
for l in cheminLivre.iterdir():
    if l.suffix == ".pdf":
        pdf.append(l)
reader = Pr(pdf[1])
page = reader.pages[7]
print(reader.outlines)
