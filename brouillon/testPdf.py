#!/bin/env python3

from pathlib import Path as p
from PyPDF2 import PdfReader as Pr

cheminLivre = p("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")
c = p("/.math_etu/users/2023/ds1/122000976/DepotsGithub/ProjetPOObiblio/brouillon/livres")
pdf = []
for l in c.iterdir():
    if l.suffix == ".pdf":
        pdf.append(l)
reader = Pr(pdf[4])
meta = reader.outline
print(meta)
