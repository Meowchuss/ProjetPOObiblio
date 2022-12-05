#!/bin/env python3

from epub import open_epub as op
import epub
import ebooklib
from pathlib import Path as p
from fitz import Document as Doc
import fitz
from fpdf import FPDF

cheminLivre = p("/home/meowchuss/gitperso/ProjetPOObiblio/brouillon/livres")
bdd = p("/home/meowchuss/bdd livres/livres")
truc = p("/home/meowchuss/bidule")
def getToc(filepath: str):
    chapitres = {}
    with Doc(filepath) as doc:
        toc = doc.get_toc()  # [[lvl, title, page, …], …]
        for title, page in toc:
            chapitres[page] = title
    return chapitres
def sendmeta(file1,file2):
    doc1 = Doc(file1)
    doc2 = Doc(file2)
    doc2.metadata = doc1.metadata.copy()
    
    
from module import *
B = Bibliothèque()
for livre in cheminLivre.iterdir():
    B.add(livre)

with open(truc/"ouvrages.txt", "w") as doc:
    print("Liste d'ouvrages dans cette bibliothèque", file = doc)
    for titre, auteur, langue, fichier in B.ouvrages.values():
        print(f"{fichier}\n{titre = }\n{auteur = }\n{langue = }\n\n", file = doc)

pdf = FPDF()
pdf.add_page() 
pdf.set_font("Arial", size = 15)
with open(truc/"ouvrages.txt", "r") as f:
    for x in f:
        x = x.encode('latin-1', 'replace').decode('latin-1')
        pdf.cell(200, 10, txt = x, ln = 1, align = "L")
    pdf.output(truc/"ouvrages.pdf")


for livre in cheminLivre.iterdir():
    
    l = Livre(livre)
    with open(f"{truc}/{l.titre}_toc.txt", "w") as doc:
        print("Table des matières\n", file = doc)
        for page, chap in l.toc.items():
            print(f"{page} : {chap}\n", file = doc)
    
    """pdf = FPDF()
    pdf.add_page() 
    pdf.set_font("Arial", size = 15)
    with open(f"{truc}/{l.titre}_toc.txt", "r") as f:
        for x in f:
            x = x.encode('latin-1', 'replace').decode('latin-1')
            pdf.cell(200, 10, txt = x, ln = 1, align = "L")
        pdf.output(f"{truc}/{l.titre}_toc.pdf")"""
    epub = fitz.open(filetype='epub')
    with open(f"{truc}/{l.titre}_toc.txt", "r") as f:
        texte = f.read()
        page = epub.new_page(width=400, height=600)
        page.add_text(texte)
    doc.save(f"{truc}/{l.titre}_toc.epub")