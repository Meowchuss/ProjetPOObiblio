#!/bin/env python3

# Module à importer : epub, PyPDF2, sys
from pathlib import Path as P
from PyPDF2 import PdfReader as Pdf
from epub import open_epub as Epub
from fitz import Document as Doc
from textblob import TextBlob

class Livre():
    # possède titre, auteur, langue, nom de fichier, contenu, format
    def __init__(self , chemin : str):
        self.path = P(chemin)
        self.format = self.path.suffix
        self.nomFichier = self.path.name

        def getToc(filepath: str):
            chapitres = {}
            with Doc(filepath) as doc:
                toc = doc.get_toc()  # [[lvl, title, page, …], …]
                for title, page in toc:
                    chapitres[page] = title
            return chapitres
        
        self.toc = getToc(chemin)
        
        if self.format == ".pdf" or self.format == ".epub":
            with Doc(chemin) as doc:
                self.titre = doc.metadata["title"]
                self.auteur = doc.metadata["author"]
                self.langue = "o"

        else:
            raise FormatError
            
    def __hash__(self):
        return hash((self.titre,self.auteur))
    def __eq__(self, Livre2):
        return self.titre == Livre2.titre and self.auteur == Livre2.auteur

class Bibliothèque():
    # possède une liste d'objet Livre
    def __init__(self):
        self.ouvrages = {} #titre, son auteur, la langue et le nom du fichier correspondant
        self.auteurs = {} #titres de ses livres et le nom des fichiers associés
    
    def ajoute(self, Livre : Livre, log = True):
        titre = Livre.titre
        auteur = Livre.auteur
        langue = Livre.langue
        fichier = Livre.nomFichier
        if Livre not in self.ouvrages:
            self.ouvrages[Livre] = [titre, auteur, langue, fichier]
        else: pass
        if auteur not in self.auteurs:
            self.auteurs[auteur] = [(titre, fichier)]
        else:
            self.auteurs[auteur].append((titre, fichier))
        
        if log == True:
            pass
    def enlève(self, Livre : Livre, log = True):
        del self.ouvrages[Livre]
        titre = Livre.titre
        auteur = Livre.auteur
        langue = Livre.langue
        fichier = Livre.nomFichier
        self.auteurs[auteur].remove((titre, fichier))
        if self.auteurs[auteur] == {}:
            del self.auteurs[auteur]
        
        if log == True:
            pass
            
        
class Rapport():
    # s'initialise avec une Bibliothèque
    # possède liste des livres (.txt, .pdf, .epub), liste des auteurs (.txt, .pdf, .epub)
    # table des matières (.txt, .pdf, .epub) pour chaque livre
    # la création/suppression crée un objet Log
    def __init__(self, Biblio):
        pass
class Log():
    # s'initialise avec un rapport 
    # La supression d'un Log ajoute ses infos dans les Logs à l'aide du path dans le fichier config
    pass
class FormatError():
    pass