# Ce script a pour objectif de dessiner la courbe d'un profil dit 4 chiffres symétriques NACA00XX et
# d'en donner le tableau des coordonnées, il calcule aussi son épaisseur maximale et sa position.

# L'utilisateur a l'opportunité de donner les 2 chiffres 'XX' du profil, la longueur de la corde,
# le nombre de points avec lequel il souhaite discrétiser le profil et la méthode avec laquelle il veut répartir
# les points sur le profil : linéaire ou non-uniforme.

# Enfin l'utilisateur a la possibilité d'enregistrer les coordonnées sous la forme d'un fichier .txt :
# 'coordonnees_profil_NACA00XX.txt' et la courbe du profil sous la forme d'une image .png : 'profil_NACA00XX.png'.
# Ces fichiers seront enregistrés dans le même dossier que celui depuis lequel est lancé ce script.


import numpy as np
import matplotlib.pyplot as plt
from fonctions_verif import *


def main():
    # On met en place le script en expliquant ce qu'il fait
    nettoyer_ecran()
    print("Ce script vous permet d'obtenir le tracé et les coordonnées d'un profil 4 chiffres symétrique NACA00XX. ")

    # On demande le numéro 'XX' du profil NACA00XX
    nombre_profil = demander_profil()
    nettoyer_ecran()

    # On demande la longueur de la corde
    corde = demander_corde()
    nettoyer_ecran()

    # On demande le nombre de points avec lequel l'utilisateur veut discrétiser la corde
    nbre_points = demander_nbre_points()
    nettoyer_ecran()

    # On demande la distribution que l'utilisateur souhaite utiliser
    print("Quel est le type de distribution de points le long de la corde : linéaire ou non-uniforme. ")
    distribution = demander_distribution()
    nettoyer_ecran()

    # Ultime étape de vérification, si l'utilisateur remarque une erreur, il peut relancer le code avec 'modifier'
    print(f"Vous voulez étudier le profil NACA00{nombre_profil}, dont la corde mesure {corde} [m]. ")
    print(f"Le calcul se fera en suivant une distribution {distribution}, sur {nbre_points} points. ")
    print("Si vous souhaitez modifier un élément, entrez 'modifier', "
          "vous pourrez alors saisir à nouveau les informations du profil. ")
    print("Sinon entrez 'continuer'. ")
    choix_redemarrer = verifier_binaire('modifier', 'continuer')

    if choix_redemarrer == 'modifier':
        nettoyer_ecran()
        main()
        # On retourne True pour ne pas faire planter le script
        return True

    # Si l'utilisateur veut continuer
    if distribution == 'linéaire':
        xc = np.linspace(0, 1, nbre_points)  # Liste des points sur la corde unitaire
        x_up = xc * corde  # Liste des points sur la corde pour tracer l'extrados
        x_down = x_up.copy()  # Liste des points sur la corde pour tracer l'intrados
    else:
        theta = np.linspace(0, np.pi, nbre_points)  # Liste des theta pour calculer xc
        xc = .5 * (1 - np.cos(theta))  # Liste des points sur la corde unitaire
        x_up = xc * corde  # Liste des points sur la corde pour tracer l'extrados
        x_down = x_up.copy()  # Liste des points sur la corde pour tracer l'intrados

    t = nombre_profil/100  # Épaisseur maximale par définition

    # Calcul des coordonnées y du profil
    # Coordonnées pour une corde unitaire
    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    y_up = yt * corde  # Liste des points de l'extrados
    y_down = -yt * corde  # Liste des points de l'intrados

    # Localisation de l'épaisseur maximale
    liste_epaisseur = y_up - y_down
    idx_epaisseur_max = np.argmax(liste_epaisseur)
    position_epaisseur_max = x_up[idx_epaisseur_max]
    print(" ")
    print(f"L'épaisseur maximale vaut {t * corde} [m] et est atteinte à {position_epaisseur_max} [m] du bord d'attaque")
    print(" ")

    # Tracé du profil
    plt.plot(x_up, y_up, label='Extrados', color='r')
    plt.plot(x_down, y_down, label='Intrados', color='b')
    plt.title(f"Profil du NACA00{nombre_profil}")
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.legend()
    plt.grid()

    # On propose à l'utilisateur d'enregistrer le profil
    print(" ")
    print("Voulez-vous enregistrer la courbe du profil dans un fichier .png ? ")
    print("Entrez 'oui' ou 'non'. ")
    choix_enregistrer_image = verifier_binaire('oui', 'non')
    if choix_enregistrer_image == 'oui':
        plt.savefig(f'profil_NACA00{nombre_profil}.png')
        print(f"Le profil a été enregistré dans 'profil_NACA00{nombre_profil}.png'")

    # Affichage de la courbe et des listes de coordonnées
    plt.show()
    print(" ")
    print(f"Les coordonnées x_up sont : {x_up}")
    print(f"Les coordonnées x_down sont : {x_down}")
    print(f"Les coordonnées y_up sont : {y_up}")
    print(f"Les coordonnées y_down sont : {y_down}")
    print(" ")

    # On propose à l'utilisateur d'enregistrer les coordonnées du profil
    print("Voulez-vous sauvegarder les données dans un fichier .txt ? ")
    print("Entrez 'oui ou 'non'. ")
    choix_enregistrer_coordonnees = verifier_binaire('oui', 'non')
    if choix_enregistrer_coordonnees == 'oui':
        donnees = np.vstack((x_up, y_up, x_down, y_down)).T
        np.savetxt(f'coordonnees_profil_NACA00{nombre_profil}.txt', donnees,
                   header='x_up y_up x_down y_down', comments='', fmt='%.2f')
        print(f"Les coordonnées ont été enregistrées dans 'coordonnees_profil_NACA00{nombre_profil}.txt'")
    print(" ")

    # On propose à l'utilisateur d'étudier un nouveau profil.
    print("Merci d'avoir utilisé ce script. Voulez-vous étudier un autre profil ? ")
    print("Entrez 'oui ou 'non'. ")
    choix_relancer = verifier_binaire('oui', 'non')
    if choix_relancer == 'oui':
        main()
        return
    else:
        print("À bientôt !")


main()
