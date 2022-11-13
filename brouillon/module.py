#!/bin/env python3

# Module à importer : epub, PyPDF2, glob, os, sys

class Livre():
    # possède titre, auteur, langue, nom de fichier, contenu, format
    pass
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