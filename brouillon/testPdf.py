#!/bin/env python3

from pathlib import Path as p
from PyPDF2 import PdfReader as Pr
import epub
from fitz import Document as Doc
import fitz
cheminLivre = p("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")
bdd = p("/home/meowchuss/bdd livres/livres")
truc = p("/home/meowchuss/bidule")
def getToc(filepath: str):
    chapitres = {}
    with Doc(filepath) as doc:
        toc = doc.get_toc()  # [[lvl, title, page, …], …]
        for level, title, page in toc:
            chapitres[page] = title
    return chapitres
import fitz

def convertir_pdf_en_epub(fichier_pdf, fichier_epub):
    # Ouvrir le fichier PDF avec la bibliothèque fitz
    document = fitz.open(fichier_pdf)

    # Créer un nouveau livre ePub
    livre = epub.EpubBook()

    # Ajouter le titre et l'auteur au livre
    livre.set_title("Mon livre")
    livre.set_author("Moi")

    # Parcourir les pages du document PDF
    for i in range(document.page_count):
        # Récupérer le texte de la page courante
        page = document[i]
        texte = page.get_text("text")

        # Créer un chapitre ePub pour la page courante
        chapitre = epub.EpubHtml(title="Chapitre {}".format(i+1), file_name="chapitre{}.xhtml".format(i+1), lang="fr")
        chapitre.content = texte

        # Ajouter le chapitre au livre
        livre.add_item(chapitre)

    # Définir les chapitres comme les chapitres principaux du livre
    livre.spine = ["nav"] + livre.items
    
    # Écrire le livre dans un fichier ePub
    epub.write_epub(fichier_epub, livre)

# Convertir un fichier PDF en ePub

""" pdf.metadata :
        Retrieve the PDF file's document information dictionary, if it exists.
        Note that some PDF files use metadata streams instead of docinfo
        dictionaries, and these metadata streams will not be accessed by this
        function.

        :return: the document information of this PDF file"""

"""def get_page_number(self, page: PageObject) -> int:
        Retrieve page number of a given PageObject
"""
from module import *

R = Rapport(cheminLivre,truc)
