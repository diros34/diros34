#!/usr/bin/env python3

import string
import time
import hashlib
import random

hash_mdp_atrouve = input("Quel est le Hash du mot de passe à trouver ? ")

Nombre_de_boucle = 26

longueur_mdp = 1

def mot_aleatoire(longueur_mdp):
    lettres = string.ascii_lowercase
    mot_genere = ""
    for carac in range (0,longueur_mdp):
        mot_genere = mot_genere + lettres[random.randint(0,len(lettres)-1)]
    return mot_genere

debut=time.time()

while True:
    if Nombre_de_boucle == 0:
        longueur_mdp = longueur_mdp + 1
        Nombre_de_boucle = 26 ** (longueur_mdp+1)
    mot_alea = mot_aleatoire(longueur_mdp)
    Nombre_de_boucle = Nombre_de_boucle - 1
    result_hash = hashlib.md5(mot_alea.encode())
    hash_alea = result_hash.hexdigest()


    #print("mot de passe testé : " + mot_alea)
    #print("hash testé : " + hash_alea)


    if hash_mdp_atrouve == hash_alea:
        Nbcombinaison  = 26 ** longueur_mdp
        print("Mot de passe trouvé : " + mot_alea )
        print(" Nombre de combinaison : " + str(Nbcombinaison) )
        fin = time.time() - debut
        print("Trouvé en "+ str(fin) + " seconde")
        break

