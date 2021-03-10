#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 08:45:52 2021

@author: Matthias Rouyer
"""

import random as ra
import matplotlib.pyplot as plt
import time

def tri_par_insertion(tableau):
    """ Implémentation d'une méthode de tri par insertion. 
    Prend en entrée un tableau d'éléments (entiers, réels) et renvoie un tuple contenant 
    le tableau trié, le nombre d'opération et le temps mis par la fonction """
    # note le temps quand on entre dans la fonction
    temps_init = time.time()
    # Initialise le compteur d'opération à 0
    compteur=0
    for parcours in range (1,len(tableau)):
        pivot = tableau[parcours]
        indice = parcours-1
        compteur+=1
        while indice >= 0 and tableau[indice] > pivot:
            compteur+=1
            tableau[indice+1] = tableau[indice]
            indice -= 1
        tableau[indice+1] = pivot
    # note le temps actuel - le temps initiale pour avoir le temps total d'exécution mis par la fonction
    temps = time.time() - temps_init
    return tableau,compteur,temps

def genere_tableau_aleatoire(distance_moyenne, taille):
    """ cette fonction prend deux paramètres et génere un tableau de nombres 
    entiers ayant une distance moyenne entre ses éléments de "distance_moyenne"
    et une taille de "taille". """
    return [int(ra.gauss(0,distance_moyenne)) for i in range(0,taille)]

def genere_tableau_aleatoire_trie(taille):
    """ cette fonction génère un tableau déjà trié de taille "taille" """
    return [i for i in range(0,taille)]

def genere_tableau_aleatoire_pas_trie(taille):
    """ cette fonction genere un tableau trié dans l'ordre décroissant de taille "taille" """
    return [i for i in range(taille,0,-1)]

def affiche_courbe(d_moy,taille_debut,taille_fin):
    """ cette fonction affiche les courbes """
    print("#######################")
    print("DIAGNOSTIC EN COURS ...")
    print("#######################")
    # caclul le temps pour exécuter la fonction finale
    temps_init = time.time()
    # pour afficher le "chargement"
    compteur=0
    # les listes contenant les valeurs des comparaisons effectuées dans les différentes configurations
    # Voir plus loin
    liste_c_trie = []
    liste_c_pas_trie = []
    liste_c_gauss = []
    
    # listes contenant les temps d'exécution pour des tableaux et des tailles différentes. Voir plus loin
    liste_t_trie = []
    liste_t_pas_trie = []
    liste_t_gauss = []
    
    # on fait une boucle qui va faire (taille_fin - taille_debut) echantillons
    for taille in range(taille_debut,taille_fin):
        tab_trie,c_trie,t_trie=tri_par_insertion(genere_tableau_aleatoire_trie(taille))
        tab_pas_trie,c_pas_trie,t_pas_trie = tri_par_insertion(genere_tableau_aleatoire_pas_trie(taille))
        tab_gauss,c_gauss,t_gauss = tri_par_insertion(genere_tableau_aleatoire(d_moy, taille))
        #print(taille, c_trie)
        liste_c_trie.append(c_trie)
        liste_c_pas_trie.append(c_pas_trie)
        liste_c_gauss.append(c_gauss)
        liste_t_trie.append(t_trie)
        liste_t_pas_trie.append(t_pas_trie)
        liste_t_gauss.append(t_gauss)
        compteur+=1
        # affiche le chargement en % pour les longues séries de données
        print(compteur/(taille_fin-taille_debut)*100, "%")
    # création de figures    
    fig_trie, ax_trie = plt.subplots()
    ax_trie.plot([i for i in range(taille_debut,taille_fin)], liste_c_trie)
    plt.title("Nombre de comparaisons pour un tableau déjà trié")
    plt.xlabel("Taille tableau")
    plt.ylabel("Nombre de comparaisons")
    
    fig_pas_trie, ax_pas_trie = plt.subplots()
    ax_pas_trie.plot([i for i in range(taille_debut,taille_fin)], liste_c_pas_trie)
    plt.title("Nombre de comparaisons pour un tableau trié dans l'ordre décroissant")
    plt.xlabel("Taille tableau")
    plt.ylabel("Nombre de comparaisons")
    
    fig_gauss, ax_gauss = plt.subplots()
    ax_gauss.plot([i for i in range(taille_debut,taille_fin)], liste_c_gauss)
    plt.title("Nombre de comparaisons pour un tableau généré \n aléatoirement avec une probabilité gaussienne")
    plt.xlabel("Taille tableau")
    plt.ylabel("Nombre de comparaisons")
    
    fig_temps_trie, ax_temps_trie = plt.subplots()
    ax_temps_trie.plot([i for i in range(taille_debut,taille_fin)], liste_t_trie)
    plt.title("Évolution du temps d'exécution avec des tailles \nde tableaux différentes pour des tableaux triés")
    plt.xlabel("Taille tableau")
    plt.ylabel("Temps d'exécution (en secondes)")
    
    fig_temps_pas_trie, ax_temps_pas_trie = plt.subplots()
    ax_temps_pas_trie.plot([i for i in range(taille_debut,taille_fin)], liste_t_pas_trie)
    plt.title("Évolution du temps d'exécution avec des tailles de tableaux \n différentes pour des tableaux triés dans l'ordre décroissant")
    plt.xlabel("Taille tableau")
    plt.ylabel("Temps d'exécution (en secondes)")
    
    fig_temps_gauss, ax_temps_gauss = plt.subplots()
    ax_temps_gauss.plot([i for i in range(taille_debut,taille_fin)], liste_t_gauss)
    plt.title("Évolution du temps d'exécution avec des tailles de tableaux\n différentes pour des tableaux généré aléatoirement avec proba gaussienne")
    plt.xlabel("Taille tableau")
    plt.ylabel("Temps d'exécution (en secondes)")
    
    temps_finale = time.time() - temps_init
    
    print("DIAGNOSTIC FINI")
    print("####################### \n")
    print("Le diagnostic s'est exécuté en {} secondes ! ".format(temps_finale))
    
