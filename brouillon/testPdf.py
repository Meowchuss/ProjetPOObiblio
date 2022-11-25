#!/bin/env python3

from pathlib import Path as p
from PyPDF2 import PdfReader as Pr

cheminLivre = p("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")
c = p("/.math_etu/users/2023/ds1/122000976/DepotsGithub/ProjetPOObiblio/brouillon/livres")
bdd = p("/home/meowchuss/bdd livres/livres")
pdf = []
""" pdf.metadata :
        Retrieve the PDF file's document information dictionary, if it exists.
        Note that some PDF files use metadata streams instead of docinfo
        dictionaries, and these metadata streams will not be accessed by this
        function.

        :return: the document information of this PDF file"""

"""def get_page_number(self, page: PageObject) -> int:
        Retrieve page number of a given PageObject
"""
k=0
for l in bdd.iterdir():
    if l.suffix == ".pdf":
        print(f"{k=}")
        meta = Pr(l).metadata.title
        print(meta)
        k+=1