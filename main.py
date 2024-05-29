# Ce script permet ....

import numpy as np
import matplotlib.pyplot as plt
from fonctions_verif import *


def main():
    nettoyer_ecran()
    print("Ce script vous permet d'obtenir le tracé et les coordonnées d'un profil 4 chiffres symétrique NACA00XX. ")

    nombre_profil = demander_profil()
    nettoyer_ecran()

    corde = demander_corde()
    nettoyer_ecran()

    nbre_points = demander_nbre_points()
    nettoyer_ecran()

    print("Quel est le type de distribution de points le long de la corde : linéaire ou non-uniforme. ")
    distribution = demander_distribution()
    nettoyer_ecran()

    print(f"Vous voulez étudier le profil NACA00{nombre_profil}, dont la corde mesure {corde} [m]. ")
    print(f"Le calcul se fera en suivant une distribution {distribution}, sur {nbre_points} points. ")
    print("Si vous souhaitez modifier un élément, entrez 'modifier', "
          "vous pourrez alors saisir à nouveau les informations du profil. ")
    print("Sinon entrez 'continuer'. ")
    choix_redemarrer = verifier_binaire('modifier', 'continuer')

    if choix_redemarrer == 'modifier':
        nettoyer_ecran()
        main()
        return True

    if distribution == 'linéaire':
        xc = np.linspace(0, 1, nbre_points)
        x_up = xc * corde
        x_down = x_up.copy()
    else:
        theta = np.linspace(0, np.pi, nbre_points)
        xc = .5 * (1 - np.cos(theta))
        x_up = xc * corde
        x_down = x_up.copy()

    t = nombre_profil/100

    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)
    y_up = yt * corde
    y_down = -yt * corde

    epaisseur = y_up - y_down
    idx_epaisseur_max = np.argmax(epaisseur)
    epaisseur_max = epaisseur[idx_epaisseur_max]
    position_epaisseur_max = x_up[idx_epaisseur_max]
    print(" ")
    print(f"L'épaisseur maximale vaut {t * corde} [m] et est atteinte à {position_epaisseur_max} [m] du bord d'attaque")
    print(" ")

    plt.plot(x_up, y_up, label='Extrados', color='r')
    plt.plot(x_down, y_down, label='Intrados', color='b')
    plt.title(f"Profil du NACA00{nombre_profil}")
    plt.xlabel('x [m]')
    plt.ylabel('y [m]')
    plt.legend()
    plt.grid()

    print(" ")
    print("Voulez-vous enregistrer la courbe du profil dans un fichier .png ? ")
    print("Entrez 'oui' ou 'non'. ")
    choix_enregistrer_image = verifier_binaire('oui', 'non')
    if choix_enregistrer_image == 'oui':
        plt.savefig(f'profil_NACA00{nombre_profil}.png')
        print(f"Le profil a été enregistré dans 'profil_NACA00{nombre_profil}.png'")

    plt.show()
    print(" ")
    print(f"Les coordonnées x_up sont : {x_up}")
    print(f"Les coordonnées x_down sont : {x_down}")
    print(f"Les coordonnées y_up sont : {y_up}")
    print(f"Les coordonnées y_down sont : {y_down}")
    print(" ")

    print("Voulez-vous sauvegarder les données dans un fichier .txt ? ")
    print("Entrez 'oui ou 'non'. ")
    choix_enregistrer_coordonnees = verifier_binaire('oui', 'non')
    if choix_enregistrer_coordonnees == 'oui':
        donnees = np.vstack((x_up, y_up, x_down, y_down)).T
        np.savetxt(f'coordonnees_profil_NACA00{nombre_profil}.txt', donnees, header='x_up y_up x_down y_down', comments='', fmt='%.2f')
        print(f"Les coordonnées ont été enregistrées dans 'coordonnees_profil_NACA00{nombre_profil}.txt'")
    print(" ")

    print("Merci d'avoir utilisé ce script. Voulez-vous étudier un autre profil ? ")
    print("Entrez 'oui ou 'non'. ")
    choix_relancer = verifier_binaire('oui', 'non')
    if choix_relancer == 'oui':
        main()
        return
    else:
        print("À bientôt !")


main()
