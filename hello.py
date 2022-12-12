#!/usr/bin/env python3

import random
import string
import time

mot_de_passe = "toto"

def mot_aleatoire(longueur):
    lettres = string.ascii_lowercase
    mot_genere = ""
    for carac in range (0,longueur):
        mot_genere = mot_genere + lettres[random.randint(0,len(lettres)-1)]
    return mot_genere
debut=time.time()
while True:
    mot_alea = mot_aleatoire(len(mot_de_passe))
    # print("mot de passe testé : " + mot_alea)
    if mot_de_passe == mot_alea:
        print("mot de passe trouvé : " + mot_alea)
        fin = time.time() - debut
        print("Trouvé en "+ str(fin) + " seconde")
        break

