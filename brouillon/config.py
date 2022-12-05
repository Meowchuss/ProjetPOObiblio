#!/bin/env python3

import configparser as config

config = config.ConfigParser()
config["Dossier"] = {
    "Bibli" : "oui/",
    "Rapports" : "non/"
}

with open("bibli.config", "w") as f:
    config.write(f)
config.read("bibli.config")
bib = config.get("Dossier", "Bibli")
print(bib)