#!/bin/env python3

# Module à importer : epub, PyPDF2, sys
from pathlib import Path as p
from PyPDF2 import PdfReader as Pdf
from epub import open_epub as Epub

class Livre():
    # possède titre, auteur, langue, nom de fichier, contenu, format
    def __init__(self,chemin):
        self.path = p(chemin)
        self.format = self.path.suffix
        self.nom = self.path.name
        
        def gettoc(path): # On veut un format {"Titre" : "Nom du livre", "Chapitres": {"Chapitre i" : ["Nom du chapitre", page]}}
            pass
        
        if self.format == ".pdf":
            pdf = Pdf.reader(self.path)
            self.auteur = pdf.metadata["Author"]
            self.titre = pdf.metadata["Title"]
            self.langue = 0
            self.toc = {}
        elif self.format == ".epub":
            epub = Epub(self.path)
            self.auteur = 0
            self.titre = 0
            self.langue = 0
            self.toc = {}
        
class Bibliothèque():
    # possède une liste d'objet Livre
    pass
class Rapport():
    # s'initialise avec une Bibliothèque
    # possède liste des livres (.txt, .pdf, .epub), liste des auteurs (.txt, .pdf, .epub)
    # table des matières (.txt, .pdf, .epub) pour chaque livre
    # la création/suppression crée un objet Log
    pass
class Log():
    # s'initialise avec un rapport 
    # La supression d'un Log ajoute ses infos dans les Logs à l'aide du path dans le fichier config
    pass