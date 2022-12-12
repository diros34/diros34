#!/usr/bin/env python3

import string
import time
import hashlib
import random

hash_mdp_atrouve = "f71dbe52628a3f83a77ab494817525c6"

mot_de_passe = "abcd"

def mot_aleatoire(longueur):
    lettres = string.ascii_lowercase
    mot_genere = ""
    for carac in range (0,longueur):
        mot_genere = mot_genere + lettres[random.randint(0,len(lettres)-1)]
    return mot_genere

debut=time.time()

while True:
    mot_alea = mot_aleatoire(len(mot_de_passe))
    result_hash = hashlib.md5(mot_alea.encode())
    hash_alea = result_hash.hexdigest()
    #print("mot de passe testé : " + mot_alea)
    #print("hash testé : " + hash_alea)
    if hash_mdp_atrouve == hash_alea:
        print("mot de passe trouvé : " + mot_alea)
        fin = time.time() - debut
        print("Trouvé en "+ str(fin) + " seconde")
        break

