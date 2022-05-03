# -*- coding: utf-8 -*-
"""
Script pour calculer l'indice de masse corporel
Version 1.0
@author: Eric Chabot
"""

from os import system
# Fonction de conversion

def conversionLbsKg(masseLbs):
    masseKg = float(masseLbs) * 0.45359237
    return masseKg

def conversionPiedsM(taillePieds):
    tailleM = float(taillePieds) * 0.3048
    return tailleM

def indiceMasseCorp(masseKg, tailleM):
    imc = masseKg / tailleM ** 2
    return imc

depart = 0

# Interface utilisateur

while (depart < 1):

    systeme = input("Utiliséz-vous le système métrique (m) ou impérial (i): ")
    
    if (systeme == "i"):
        poids = input("Entez votre poids en livres: ")
        taillePieds = input("Entrez votre taille en pieds: ")
        
        masseKg = conversionLbsKg(poids)
        tailleM = conversionPiedsM(taillePieds)
        imc = indiceMasseCorp(masseKg, tailleM)
        
        print("\nVotre indice de masse corporel (imc) est:", imc)
        
        depart = depart + 1
        
    elif (systeme == "m"):
        masseKg = input("Entez votre poids en Kg: ")
        tailleM = input("Entrez votre taille en mètre: ")
        
        imc = indiceMasseCorp(float(masseKg), float(tailleM))
        
        print("\nVotre indice de masse corporel (imc) est:", imc)
        
        depart = depart + 1
        
    else:
        depart = 0
        
print("\n\nIMC < 18,5 = Poids insuffisant -> Risque accru d'avoir des probèmes de santé.")
print("IMC entre 18,5 et 24,9 = Poids normal -> Risque moindre d'avoir des probèmes de santé.")
print("IMC entre 25,0 et 29,9 = Excès de poids -> Risque accru d'avoir des probèmes de santé.")
print("IMC entre 30,0 - 34,9 = Obésité, classe I -> Risque élevé d'avoir des probèmes de santé.")
print("IMC entre 35,0 - 39,9 = Obésité, classe II -> Risque très élevé d'avoir des probèmes de santé.")
print("IMC >= 40,0 = Obésité, classe III -> Risque extrêmement élevé d'avoir des probèmes de santé.\n\n")     

system("pause")


