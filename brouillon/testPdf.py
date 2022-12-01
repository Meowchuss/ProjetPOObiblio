#!/bin/env python3

from pathlib import Path as p
from PyPDF2 import PdfReader as Pr
from epub import open_epub as Epub

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
def toc(lNavPoint):
        return [ x.labels[0][0] for x in lNavPoint]
for l in bdd.iterdir():
        
        
        if l.suffix == ".pdf":
                titre = Pr(l).metadata.title
                auteur = Pr(l).metadata.author
                langue = 0
                if not titre :
                        print(l.name)
                        print(f"{titre = } \n{auteur = } \n{langue =}")
                        print()
        elif l.suffix == ".epub":
                """auteur = Epub(l).opf.metadata.creators[0][0]
                
                titre = Epub(l).opf.metadata.titles[0][0]
                langue = Epub(l).opf.metadata.languages[0]
                spine = Epub(l).toc.nav_map.nav_point
                pages = Epub(l).toc.page_list.class_name
                #print(f"{titre = } \n{auteur =} \n{langue =}")
                #print(toc(spine))
                #print(pages)
                #print()"""