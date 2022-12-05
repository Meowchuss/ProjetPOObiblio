#!/bin/env python3

from pathlib import Path as P
from fitz import Document as Doc
import fitz
from epub import open_epub as Epub
from fpdf import FPDF
from langdetect import detect
from langdetect.lang_detect_exception import LangDetectException
import configparser as cp
import logging
from aspose.words import Document as awd

class Livre():
    # possède titre, auteur, langue, nom de fichier, contenu, format
    def __init__(self , chemin : str):
        self.path = P(chemin)
        self.format = self.path.suffix
        self.nomFichier = self.path.name

        def getToc(chemin: str):
            chapitres = {}
            with Doc(chemin) as doc:
                toc = doc.get_toc()  # [[lvl, title, page, …], …]
                for level, title, page in toc:
                    chapitres[page] = title
            return chapitres
        
        if self.format == ".pdf" or self.format == ".epub":
            self.toc = getToc(chemin)
            with Doc(chemin) as doc:
                self.titre = doc.metadata["title"] if doc.metadata["title"] else ""
                self.auteur = doc.metadata["author"] if doc.metadata["author"] else ""
            with fitz.open(chemin) as f:
                if self.format == ".pdf":
                    contenu = ""
                    k = 0
                    self.langue = ""
                    try:
                        while contenu == "":
                            contenu = f.get_page_text(k)
                            k += 1
                        self.langue = detect(str(contenu))
                    except (IndexError, LangDetectException):
                        self.langue = ""
                    
                else:
                    self.langue = Epub(chemin).opf.metadata.languages[0]
        else:
            raise FormatError
    
    def print_toc(self,chemin : str, epub = False):
        p = P(chemin)
        if "/" in self.titre:
            self.titre = "".join(self.titre.split("/"))
            
        with open(p/f"{self.titre}_toc.txt", "w") as doc:
            print("Table des matières\n", file = doc)
            for page, chapitre in self.toc.items():
                print(f"{page} - {chapitre}\n", file = doc)
            print(f"Emplacement :\n{self.path}", file = doc)

        pdf = FPDF()
        pdf.add_page() 
        pdf.set_font("Arial", size = 15)
        with open(f"{chemin}/{self.titre}_toc.txt", "r") as f:
            for x in f:
                x = x.encode('latin-1', 'replace').decode('latin-1')
                pdf.cell(200, 10, txt = x, ln = 1, align = "L")
            pdf.output(f"{chemin}/{self.titre}_toc.pdf")
        if epub:
            doc = awd(f"{chemin}/{self.titre}_toc.pdf")
            doc.save(f"{chemin}/{self.titre}_toc.epub")
    
    def __str__(self) -> str:
        return f"{self.titre} de {self.auteur}"
    def __repr__(self) -> str:
        return f"{self.titre} de {self.auteur}"  
    def __hash__(self):
        return hash((self.titre,self.auteur))
    def __eq__(self, Livre2):
        if isinstance(Livre2, Livre):
            return self.titre == Livre2.titre and self.auteur == Livre2.auteur
        else:
            raise ValueError
    def del_toc(self, chemin : str):
        txt = P(f"{chemin}/{self.titre}_toc.txt")
        pdf = P(f"{chemin}/{self.titre}_toc.pdf")
        epub = P(f"{chemin}/{self.titre}_toc.epub")
        if txt.exists():
            txt.unlink()
        if pdf.exists():
            pdf.unlink()
        if epub.exists():
            epub.unlink()

class Bibliothèque():
    # possède une liste d'objet Livre
    def __init__(self):
        self.ouvrages = {} #{objet Livre : [titre, auteur, langue, fichier], …}
        self.auteurs = {} #{auteur : [(titre, fichier), …], ...}
    
    def add(self, livre : str, log = True):
        book = Livre(livre)
        titre = book.titre
        auteur = book.auteur
        langue = book.langue
        fichier = book.nomFichier
        
        if book not in self.ouvrages:
            self.ouvrages[book] = [titre, auteur, langue, fichier]
        else: pass
        
        if auteur not in self.auteurs:
            self.auteurs[auteur] = [(titre, fichier)]
        else:
            self.auteurs[auteur].append((titre, fichier))
        
        if log == True:
            logging.info(f"{book} a été ajouté")
    
    def remove(self, livre : str, log = True):
        book = Livre(livre)
        del self.ouvrages[book]
        titre = book.titre
        auteur = book.auteur
        fichier = book.nomFichier
        self.auteurs[auteur].remove((titre, fichier))
        if self.auteurs[auteur] == {}:
            del self.auteurs[auteur]
        
        if log == True:
            logging.info(f"{book} a été enlevé")
    
    def is_vide(self):
        return self.ouvrages == self.auteurs == {}
    
    def print_ouvrages_auteurs(self, dossierRapport, epub = False):
        with open(dossierRapport/"ouvrages.txt", "w") as doc:
            print("Liste d'ouvrages dans cette bibliothèque", file = doc)
            for titre, auteur, langue, fichier in self.ouvrages.values():
                print(f"{fichier}\n{titre = }\n{auteur = }\n{langue = }\n\n", file = doc)     
        
        pdf = FPDF()
        pdf.add_page() 
        pdf.set_font("Arial", size = 15)
        with open(dossierRapport/"ouvrages.txt", "r") as f:
            for x in f:
                x = x.encode('latin-1', 'replace').decode('latin-1')
                pdf.cell(200, 10, txt = x, ln = 1, align = "L")
            pdf.output(dossierRapport/"ouvrages.pdf")
        if epub:
            doc = awd(dossierRapport/"ouvrages.pdf")
            doc.save(dossierRapport/"ouvrages.epub")
        
        with open(dossierRapport/"auteurs.txt", "w") as doc:
            print("Liste des auteurs dans cette bibliothèque", file = doc)
            for auteur, listeTitres in self.auteurs.items():
                print(f"{auteur} a écrit :\n", file = doc)
                for titre, fichier in listeTitres:
                    print(f"{titre} - qui est situé dans - {fichier}", file = doc)
        
        pdf = FPDF()
        pdf.add_page() 
        pdf.set_font("Arial", size = 15)
        with open(dossierRapport/"auteurs.txt", "r") as f:
            for x in f:
                x = x.encode('latin-1', 'replace').decode('latin-1')
                pdf.cell(200, 10, txt = x, ln = 1, align = "L")
            pdf.output(dossierRapport/"auteurs.pdf")
        if epub:
            #ne marche pas sur certains pc (le mien) à cause du manque d'un certain libssl que je n'ai pas pu regler
            doc = awd(dossierRapport/"auteurs.pdf")
            doc.save(dossierRapport/"auteurs.epub")
    
            
class Rapport():
    # s'initialise avec une bibliothèque
    
    def __init__(self, livres : str, dossierRapport : str, init = True, update = False, ancienneBibli = Bibliothèque()):
        B = Bibliothèque()
        self.dossierRapport = dossierRapport
        if init:
            update = False
            for livre in P(livres).iterdir():
                try :
                    l = Livre(livre)
                    B.add(livre)
                    l.print_toc(dossierRapport)
                except FormatError as e:
                    logging.info(f"{l} n'est pas accepté")
            print("Initialisation finie")
        if update:
            for livre in P(livres).iterdir():
                try :
                    l = Livre(livre)
                    if l not in ancienneBibli.ouvrages.keys():
                        B.add(livre)
                        l.print_toc(dossierRapport)
                    else:
                        B.add(livre, log = False)
                        ancienneBibli.remove(livre, log = False)
                except FormatError:
                    logging.info(f"{l} n'est pas accepté")
                             
            if not ancienneBibli.is_vide():
                
                for L in list(ancienneBibli.ouvrages.keys()).copy():
                    try:
                        livre = L.path
                        ancienneBibli.remove(livre)
                        L.del_toc(dossierRapport)
                    except FileNotFoundError:
                        pass
            print("Maj finie")
        B.print_ouvrages_auteurs(dossierRapport)
        self.bibli = B

    
class Config():
    def __init__(self,bibli, file = "bibli.config", dossierRapports = None, fichierLogs = P.cwd()/"bibli.log" ) -> None:
        self.fichierConfig = P.cwd()/file
        if dossierRapports:
            Rapports = dossierRapports
        else:
            Rapports = P.cwd()/"Rapports"
            Rapports.mkdir()
        config = cp.ConfigParser()
        config["Dossier"] = {
            "Bibli" : bibli,
            "Rapports" : Rapports,
            "Logs" : fichierLogs
        }
        with open(self.fichierConfig, "w") as f:
            config.write(f)
        
        config.read(self.fichierConfig)
        self.dossierRapports = config.get("Dossier", "Rapports")
        self.dossierBibli = config.get("Dossier", "Bibli")
        self.fichierLogs = config.get("Dossier", "Logs")
            
    def startLog(self):
        logging.basicConfig(filename = self.fichierLogs, level=logging.DEBUG)

class FormatError(ValueError):
    pass


